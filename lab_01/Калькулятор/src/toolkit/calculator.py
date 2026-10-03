def tokenize_char(expr:str): 
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1 
        elif expr[i].isdigit() or expr[i] == '.': 
            num_str = expr[i] 
            i += 1
            while i < len(expr) and (expr[i].isdigit() or expr[i]=='.'): 
                num_str += expr[i]
                i += 1
            tokens.append(('NUMBER', float(num_str) if '.' in num_str else int(num_str)))
            continue
        elif expr[i] in '+-*/()': 
            if expr[i] in '+-': 
                is_unary = False
                if not tokens: 
                    is_unary = True
                else:
                    prev_type = tokens[-1][0]
                    if prev_type in ('OPERATOR','LPAREN','UNARY'): 
                            is_unary = True
                if is_unary: 
                    tokens.append(('UNARY', expr[i]))   
                    i += 1
                    continue
                else: 
                    tokens.append(('OPERATOR', expr[i]))
                    i += 1
                    continue

            if expr[i] == '(':
                tokens.append(('LPAREN', expr[i]))
                i += 1
                continue
            if expr[i] == ')':
                tokens.append(('RPAREN', expr[i]))
                i += 1
                continue
            if expr[i] in '*/':
                tokens.append(('OPERATOR', expr[i]))
                i += 1
                continue
            raise ValueError(f"Неизвестный символ: {expr[i]}")
    return tokens


def to_rpn(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2,'u+': 3, 'u-': 3}
    output = []
    stack = []

    for token in tokens:
        first_element, second_element = token

        if first_element == 'NUMBER': 
            output.append(token)

        elif first_element == 'UNARY': 
            op_name = 'u' + second_element 
            while (stack and stack[-1][0] == 'OPERATOR_OR_UNARY' and precedence[op_name] <= precedence[stack[-1][1]]):output.append(stack.pop())
            stack.append(('OPERATOR_OR_UNARY', op_name))

        elif first_element == 'OPERATOR':
            op_name = second_element
            while (stack and stack[-1][0] == 'OPERATOR' and precedence[op_name] <= precedence[stack[-1][1]]):
                output.append(stack.pop())
            stack.append(('OPERATOR_OR_UNARY',op_name))

        elif first_element == 'LPAREN':
            stack.append(('LPAREN', second_element))

        elif first_element == 'RPAREN':
            while stack and stack[-1][0] != 'LPAREN':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Несбалансированные скобки: лишняя ')'")
            stack.pop()   
        else:
            raise ValueError(f"Неизвестный токен: {token}")
    while stack:
        output.append(stack.pop())

    return output


def calculator(rpn_tokens):
    ops = {'+': lambda a,b: a+b,
           '-': lambda a,b: a-b,
           '*': lambda a,b: a*b,
           '/': lambda a,b: a/b,
           'u+': lambda a: +a,
           'u-': lambda a: -a,
           }
    stack = []
    for token in rpn_tokens:
        if token[0] == 'NUMBER':
            stack.append(token[1])
        elif token[0] in ('OPERATOR_OR_UNARY',):
            op = token[1]
            if op in ('u+', 'u-'):
                if len(stack) < 1:
                    raise ValueError("Недостаточно операндов для унарной операции")
                a = stack.pop()
                stack.append(ops[op](a))
            else:
                if len(stack) < 2:
                    raise ValueError("Недостаточно операндов для бинарной операции")
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[op](a, b))
        else:
            raise ValueError(f"Неизвестный токен в RPN: {token}")

    if len(stack) != 1:
        raise ValueError("Ошибка вычисления: в стеке не один результат")
    return stack[0]


def calculate(expr: str):
    tokens = tokenize_char(expr)
    rpn = to_rpn(tokens)
    return calculator(rpn)