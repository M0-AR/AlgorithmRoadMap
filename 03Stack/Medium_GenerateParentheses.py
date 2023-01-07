def generate_parenthesis(n):
    stack = []
    res = []

    def back_track(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return

        if openN < n:
            stack.append("(")
            back_track(openN + 1, closedN)
            stack.pop()

        if closedN < openN:
            stack.append(")")
            back_track(openN, closedN + 1)
            stack.pop()

    back_track(0, 0)
    return res


print(generate_parenthesis(3))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
