class StackInterpreter:
    def __init__(self):
        self.stack = []
        self.variables = {}
        self.labels = {}
        self.instructions = []
        self.ip = 0  # instruction pointer

    def run(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            self.instructions = [line.strip() for line in f if line.strip()]
        self._preprocess_labels()

        while self.ip < len(self.instructions):
            instr = self.instructions[self.ip]
            if not self._execute(instr):
                self.ip += 1

    def _preprocess_labels(self):
        for idx, line in enumerate(self.instructions):
            if line.startswith("label"):
                _, label_id = line.split()
                self.labels[int(label_id)] = idx

    def _execute(self, instr):
        parts = instr.split()
        op = parts[0]

        if op == "label":
            return False
        elif op == "jmp":
            self.ip = self.labels[int(parts[1])]
            return True
        elif op == "fjmp":
            cond = self._pop()
            if not cond:
                self.ip = self.labels[int(parts[1])]
                return True
        elif op == "push":
            t, val = parts[1], " ".join(parts[2:])
            if t == "I":
                self.stack.append(int(val))
            elif t == "F":
                self.stack.append(float(val))
            elif t == "B":
                self.stack.append(val == "true")
            elif t == "S":
                self.stack.append(val.strip('"'))
        elif op == "pop":
            self._pop()
        elif op == "load":
            self.stack.append(self.variables.get(parts[1], 0))
        elif op == "save":
            self.variables[parts[1]] = self._pop()
        elif op == "add":
            b, a = self._pop(), self._pop()
            self.stack.append(a + b)
        elif op == "sub":
            b, a = self._pop(), self._pop()
            self.stack.append(a - b)
        elif op == "mul":
            b, a = self._pop(), self._pop()
            self.stack.append(a * b)
        elif op == "div":
            b, a = self._pop(), self._pop()
            self.stack.append(a / b)
        elif op == "mod":
            b, a = self._pop(), self._pop()
            self.stack.append(a % b)
        elif op == "uminus":
            a = self._pop()
            self.stack.append(-a)
        elif op == "concat":
            b, a = self._pop(), self._pop()
            self.stack.append(str(a) + str(b))
        elif op == "and":
            b, a = self._pop(), self._pop()
            self.stack.append(a and b)
        elif op == "or":
            b, a = self._pop(), self._pop()
            self.stack.append(a or b)
        elif op == "gt":
            b, a = self._pop(), self._pop()
            self.stack.append(a > b)
        elif op == "lt":
            b, a = self._pop(), self._pop()
            self.stack.append(a < b)
        elif op == "eq":
            b, a = self._pop(), self._pop()
            self.stack.append(a == b)
        elif op == "not":
            a = self._pop()
            self.stack.append(not a)
        elif op == "itof":
            a = self._pop()
            self.stack.append(float(a))
        elif op == "print":
            n = int(parts[1])
            vals = [self._pop() for _ in range(n)][::-1]
            print("".join(str(v) for v in vals))
        elif op == "read":
            t = parts[1]
            raw = input().strip()
            try:
                if t == "I":
                    value = int(raw)
                    self.stack.append(value)
                elif t == "F":
                    value = float(raw)
                    self.stack.append(value)
                elif t == "B":
                    if raw.lower() not in ["true", "false"]:
                        raise ValueError("Expected 'true' or 'false'")
                    self.stack.append(raw.lower() == "true")
                elif t == "S":
                    self.stack.append(raw)
                else:
                    raise ValueError(f"Unknown type: {t}")
            except ValueError as e:
                print(f"Invalid input for type '{t}': '{raw}' → {e}")
                return False
        elif op == "fwrite":
            file = self._pop()
            value = self._pop()
            try:
                with open(file, "a", encoding="utf-8") as f:
                    f.write(str(value))
            except Exception as e:
                print(f"Error writing to file '{file}': {e}")

        
        return False

    def _pop(self):
        return self.stack.pop() if self.stack else 0
