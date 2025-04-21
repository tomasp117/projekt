from parser.MyLangVisitor import MyLangVisitor
from parser.MyLangParser import MyLangParser

class CodeGeneratorVisitor(MyLangVisitor):
    def __init__(self):
        self.instructions = []
        self.symbols = {}  # varName -> type
        self.label_counter = -1

    def emit(self, instr):
        self.instructions.append(instr)

    def new_label(self):
        self.label_counter += 1
        return self.label_counter

    def write_to_file(self, path="output.stack"):
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(self.instructions))

    def visitProgram(self, ctx: MyLangParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitDeclaration(self, ctx: MyLangParser.DeclarationContext):
        typ = ctx.TYPE().getText()

        for id_node in ctx.ID():
            var_name = id_node.getText()
            self.symbols[var_name] = typ

            default_push = {
                "int": "push I 0",
                "float": "push F 0.0",
                "bool": "push B false",
                "string": 'push S ""',
                "FILE": None  # zatím neřešíme FILE
            }.get(typ)

            if default_push:
                self.emit(default_push)
                self.emit(f"save {var_name}")

    def visitPrimary(self, ctx: MyLangParser.PrimaryContext):
        if ctx.INT():
            val = ctx.INT().getText()
            self.emit(f"push I {val}")
            return "int"
        elif ctx.FLOAT():
            val = ctx.FLOAT().getText()
            self.emit(f"push F {val}")
            return "float"
        elif ctx.BOOL():
            val = ctx.BOOL().getText()
            self.emit(f"push B {val}")
            return "bool"
        elif ctx.STRING():
            val = ctx.STRING().getText()[1:-1]  # bez uvozovek
            self.emit(f'push S "{val}"')
            return "string"
        elif ctx.ID():
            name = ctx.ID().getText()
            self.emit(f"load {name}")
            return self.symbols.get(name, "unknown")
        elif ctx.expression():
            return self.visit(ctx.expression())

    def visitWriteStatement(self, ctx: MyLangParser.WriteStatementContext):
        count = len(ctx.expression())
        for expr in ctx.expression():
            self.visit(expr)
        self.emit(f"print {count}")

    def visitAssignment(self, ctx: MyLangParser.AssignmentContext):
        if ctx.ASSIGN():
            left = ctx.getChild(0)
            right = ctx.assignment()

            var_name = left.getText()
            right_type = self.visit(right)

            var_type = self.symbols.get(var_name)
            if var_type == "float" and right_type == "int":
                self.emit("itof")

            self.emit(f"save {var_name}")
            self.emit(f"load {var_name}")
            return var_type
        else:
            return self.visit(ctx.logic_or())
        
    def visitAddition(self, ctx: MyLangParser.AdditionContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.getChild(0))

        left_type = self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        right_type = self.visit(ctx.getChild(2))

        if op == ".":
            self.emit("concat")
            return "string"

        float_result = left_type == "float" or right_type == "float"
        if float_result:
            if left_type == "int":
                self.instructions.insert(len(self.instructions) - 2, "itof")
            if right_type == "int":
                self.emit("itof")

        instr = "add" if op == "+" else "sub"
        instr += " F" if float_result else " I"
        self.emit(instr)

        return "float" if float_result else "int"

    def visitExpressionStatement(self, ctx: MyLangParser.ExpressionStatementContext):
        self.visit(ctx.expression())
        self.emit("pop") 

    def visitWriteFileStatement(self, ctx: MyLangParser.WriteFileStatementContext):
        file_var = ctx.ID().getText()
        self.emit(f"load {file_var}")
        for expr in ctx.expression():
            self.visit(expr)
            self.emit("concat")
        self.emit("print 1")

