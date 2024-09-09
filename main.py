class ExpressionSolver:
    def __init__(self, expression):
        # Initialize with the expression
        self.expression = expression
    
    def solve(self):
        try:
            # Evaluate the expression safely
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error in solving expression: {e}"

    def print_result(self):
        # Get the result and print it
        result = self.solve()
        print(f"The result of the expression '{self.expression}' is: {result}")

# Create an instance of ExpressionSolver
expression = input("Enter a mathematical expression: ")
solver = ExpressionSolver(expression)

# Solve and print the result
solver.print_result()
