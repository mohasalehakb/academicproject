class Expression:

    def __init__(self, expression):
        self.expr = expression
        self.Explist = []

    def calcu_exp(self):

        for char in self.expr:
            if char.isdigit():
                self.Explist.append(int(char))
            else:
                b = self.Explist.pop()
                a = self.Explist.pop()

                if char == '+':
                    self.Explist.append(a + b)
                elif char == '-':
                    self.Explist.append(a - b)
                elif char == '*':
                    self.Explist.append(a * b)
                elif char == '/':
                    self.Explist.append(a / b)

        return self.Explist[-1]


def main():
    expression = input("enter expression: ")
    expr = Expression(expression)
    infix = expr.calcu_exp()
    print(infix)


if __name__ == '__main__':
    main()
