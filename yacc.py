def evaluate(expr):
    try:
        result = eval(expr)
        return result
    except:
        return "Invalid Expression"

# main function
expr = input("Enter the arithmetic: ")
allowed = "0123456789+-*/(). "

valid = True
for ch in expr:
    if ch not in allowed:
        valid = False
        break

if not valid:
    print("Invalid Expression")
else:
    result = evaluate(expr)
    print("Resukt: ",result)
    