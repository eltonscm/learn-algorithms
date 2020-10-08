from data_structures.stack import Stack


def postfix_calculator(expression: str) -> int:
    stack = Stack()
    for char in expression.split(" "):
        if char.isdigit():
            stack.push(int(char))
        else:
            # I'm assuming that user input is valid. In "real world" project
            # it's necessary to check if is a valid operator.
            right = stack.pop()
            left = stack.pop()
            result = eval(f"{left}{char}{right}")
            stack.push(result)

    return stack.peek()
