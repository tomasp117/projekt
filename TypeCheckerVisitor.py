from PLCParser import PLCParser
from PLCVisitor import PLCVisitor

class TypeCheckerVisitor(PLCVisitor):
    def __init__(self):
        self.symbols = {}  # variable name -> type
        self.errors = []

    def visitProgram(self, ctx: PLCParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)

        if self.errors:
            print("❌ Type errors:")
            for error in self.errors:
                print(" -", error)
            exit(1)
        else:
            print("✅ Type check passed.")

    def visitBlock(self, ctx: PLCParser.BlockContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitDeclaration(self, ctx: PLCParser.DeclarationContext):
        typ = ctx.TYPE().getText()
        for id_token in ctx.ID():
            name = id_token.getText()
            if name in self.symbols:
                self.errors.append(f"Variable '{name}' is already declared.")
            else:
                self.symbols[name] = typ

    def visitAssignment(self, ctx: PLCParser.AssignmentContext):
        if ctx.ASSIGN():
            left = ctx.logic_or()
            right = ctx.assignment()

            var_name = left.getText()
            if var_name not in self.symbols:
                self.errors.append(f"Variable '{var_name}' is not declared.")
                return "error"

            left_type = self.symbols[var_name]
            right_type = self.visit(right)

            if left_type == "float" and right_type == "int":
                return "float"
            if left_type != right_type:
                self.errors.append(f"Cannot assign type '{right_type}' to variable '{var_name}' of type '{left_type}'.")
            return left_type
        else:
            return self.visit(ctx.logic_or())

    def visitPrimary(self, ctx: PLCParser.PrimaryContext):
        if ctx.INT(): return "int"
        if ctx.FLOAT(): return "float"
        if ctx.BOOL(): return "bool"
        if ctx.STRING(): return "string"
        if ctx.ID():
            name = ctx.ID().getText()
            if name not in self.symbols:
                self.errors.append(f"Variable '{name}' is not declared.")
                return "error"
            return self.symbols[name]
        return self.visit(ctx.expression())

    def visitAddition(self, ctx: PLCParser.AdditionContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))

        if op == "." and left == "string" and right == "string":
            return "string"
        if left in ("int", "float") and right in ("int", "float"):
            return "float" if "float" in (left, right) else "int"

        self.errors.append(f"Operator '{op}' not supported for types '{left}' and '{right}'.")
        return "error"

    def visitMultiplication(self, ctx: PLCParser.MultiplicationContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))

        if op == "%" and ("float" in (left, right)):
            self.errors.append("Modulo '%' is only valid for integers.")
            return "error"

        if left in ("int", "float") and right in ("int", "float"):
            return "float" if "float" in (left, right) else "int"

        self.errors.append(f"Operator '{op}' not supported for types '{left}' and '{right}'.")
        return "error"

    def visitComparison(self, ctx: PLCParser.ComparisonContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        if left in ("int", "float") and right in ("int", "float"):
            return "bool"
        self.errors.append(f"Invalid comparison between '{left}' and '{right}'.")
        return "error"

    def visitEquality(self, ctx: PLCParser.EqualityContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        if left == right and left in ("int", "float", "string"):
            return "bool"
        self.errors.append(f"Invalid equality check between '{left}' and '{right}'.")
        return "error"

    def visitLogic_and(self, ctx: PLCParser.Logic_andContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        if left == right == "bool":
            return "bool"
        self.errors.append("Logical AND requires boolean operands.")
        return "error"

    def visitLogic_or(self, ctx: PLCParser.Logic_orContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        if left == right == "bool":
            return "bool"
        self.errors.append("Logical OR requires boolean operands.")
        return "error"

    def visitUnary(self, ctx: PLCParser.UnaryContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.getChild(0))
        op = ctx.getChild(0).getText()
        operand = self.visit(ctx.getChild(1))
        if op == "-" and operand in ("int", "float"):
            return operand
        if op == "!" and operand == "bool":
            return "bool"
        self.errors.append(f"Unary operator '{op}' not valid for type '{operand}'.")
        return "error"

    def visitExpressionStatement(self, ctx: PLCParser.ExpressionStatementContext):
        self.visit(ctx.expression())

    def visitWriteStatement(self, ctx: PLCParser.WriteStatementContext):
        for expr in ctx.expression():
            self.visit(expr)

    def visitIfStatement(self, ctx: PLCParser.IfStatementContext):
        condition_type = self.visit(ctx.expression())
        if condition_type != "bool":
            self.errors.append(f"'if' condition must be of type 'bool', got '{condition_type}'")
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitWhileStatement(self, ctx: PLCParser.WhileStatementContext):
        condition_type = self.visit(ctx.expression())
        if condition_type != "bool":
            self.errors.append(f"'while' condition must be of type 'bool', got '{condition_type}'")
        self.visit(ctx.statement())
