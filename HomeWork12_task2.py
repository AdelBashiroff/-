def is_valid_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False  # Закрывающая скобка без соответствующей открывающей
            stack.pop()
    return len(stack) == 0  # Стек должен быть пуст в конце

# Примеры использования:
examples = [
    "0",        # True
    "(0)0",     # True
    "00",       # True
    "((0))",    # True
    ")0",       # False
    "0)(0",     # False
    "0))))",    # False
    "((0",      # False
]

for expr in examples:
    print(f"{expr:10} -> {is_valid_parentheses(expr)}")
