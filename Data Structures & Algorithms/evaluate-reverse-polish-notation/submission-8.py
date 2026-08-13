class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop()+stack.pop())
            elif t == "-":
                y = stack.pop()
                x = stack.pop()
                stack.append(x-y)
            elif t == "*":
                stack.append(stack.pop()*stack.pop())
            elif t == "/":
                y = stack.pop()
                x = stack.pop()
                stack.append(int(x/y))
            else:
                stack.append(int(t))
        return stack.pop()
        