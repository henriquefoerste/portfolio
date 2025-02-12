# Step 1: Define the Abstract Expression Interface
class Expression:
    def interpret(self):
        pass

# Step 2: Create Terminal Expressions (Numbers)
class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value

# Step 3: Create Non-Terminal Expressions (Operations)
class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

class Multiply(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() * self.right.interpret()

class Divide(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() / self.right.interpret()

# Step 4: Create a Parser to Build the Abstract Syntax Tree (AST)
class Parser:
    def __init__(self, expression):
        self.tokens = expression.split()
        self.current_token = None
        self.next_token()

    def next_token(self):
        if self.tokens:
            self.current_token = self.tokens.pop(0)
        else:
            self.current_token = None

    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        # Parse the left operand
        left = self.parse_term()

        # Parse the operator and right operand
        while self.current_token in ("+", "-"):
            operator = self.current_token
            self.next_token()
            right = self.parse_term()
            if operator == "+":
                left = Add(left, right)
            else:
                left = Subtract(left, right)

        return left

    def parse_term(self):
        # Parse the left operand
        left = self.parse_factor()

        # Parse the operator and right operand
        while self.current_token in ("*", "/"):
            operator = self.current_token
            self.next_token()
            right = self.parse_factor()
            if operator == "*":
                left = Multiply(left, right)
            else:
                left = Divide(left, right)

        return left

    def parse_factor(self):
        # Parse a number or a nested expression
        if self.current_token.isdigit():
            value = int(self.current_token)
            self.next_token()
            return Number(value)
        else:
            raise ValueError(f"Invalid token: {self.current_token}")

# Step 5: Test the Interpreter Pattern
if __name__ == "__main__":
    # Input arithmetic expression
    expression = "2 + 3 * 4 - 6 / 2"

    # Parse and evaluate the expression
    parser = Parser(expression)
    ast = parser.parse()
    result = ast.interpret()

    print(f"Expression: {expression}")
    print(f"Result: {result}")


    # Explanation:

    # Abstract Expression Interface (Expression):

    #     Defines the interpret method that all expressions must implement.

    # Terminal Expressions (Number):

    #     Represents a number in the expression.

    #     The interpret method returns the numeric value.

    # Non-Terminal Expressions (Add, Subtract, Multiply, Divide):

    #     Represents arithmetic operations.

    #     Each operation has a left and right operand, which are also expressions.

    #     The interpret method computes the result of the operation.

    # Parser:

    #     Parses the input expression and builds an Abstract Syntax Tree (AST).

    #     The AST is a tree structure where each node is an expression (terminal or non-terminal).

    #     The parser handles operator precedence (e.g., multiplication before addition).

    # Client Code:

    #     Takes an arithmetic expression as input.

    #     Uses the parser to build the AST.

    #     Evaluates the AST to compute the result.