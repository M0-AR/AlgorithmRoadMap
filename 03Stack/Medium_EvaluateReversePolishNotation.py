def evaluate_reverse_polish_notation(tokens):
    stack = []

    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b / a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(b / a)
        else:
            stack.append(int(c))

    return stack[0]


print(evaluate_reverse_polish_notation(["2", "1", "+", "3", "*"])) # Output: 9