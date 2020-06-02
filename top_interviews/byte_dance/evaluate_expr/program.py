def eval(exprs): 
        exprs = exprs.replace('(','(,').replace(')', ',)').split(',')
        # print(exprs)
        
        def evaluate_expr(stack):
            if len(stack) == 1:
                return stack[0]

            command = stack[0]
            if command == "NOT":
                return not stack[-1]
            n = len(stack)
            res = stack[1]
            for i in range(2, n):
                if command == "AND":
                    res &= stack[i]
                elif command == "OR":
                    res |= stack[i]
                elif command == "XOR":
                    res ^= stack[i]
            # print(stack, res)
            return res
        
        stack = []
        for expr in exprs:
            if expr == ")":
                temp = []
                while stack and stack[-1] != "(":
                    temp.append(stack.pop())
                if stack[-1] == "(":
                    stack.pop()
                stack.append(evaluate_expr(temp))
                
            elif expr == "True":        
                stack.append(True)
            elif expr == "False":
                stack.append(False)
            else:
                stack.append(expr)
        return evaluate_expr(stack)


if __name__ == "__main__":
    print("-"* 25)
    expr = "(True)"
    res = eval(expr)
    print("expr:", expr, "result:", res, '\n')

    print("-"* 25)
    expr = "(True,False,True,AND)"  # False
    res = eval(expr)
    print("expr:", expr, "result:", res, '\n')

    print("-"* 25)
    expr = "(True,False,True,False,OR)"  # True
    res = eval(expr)
    print("expr:", expr, "result:", res, '\n')

    print("-"* 25)
    expr = "(True,False,True,False,True,XOR)"  # True
    res = eval(expr)
    print("expr:", expr, "result:", res, '\n')
    
    print("-"* 25)
    expr = "(False,False,XOR)"  # True
    res = eval(expr)
    print("expr:", expr, "result:", res, '\n')

    print("-"*25)
    expr = "(True,(False,True,XOR),XOR)"  # False
    res = eval(expr)
    print("expr:", expr, "result:", res, '\n')

    print("-"*25)
    expr = "((True,(False,NOT),True,AND),(True,NOT),XOR)"
    res = eval(expr)
    print("expr:", expr, "result:", res, '\n')
