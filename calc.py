from operator import pow, truediv, mul, add, sub

is_rome = False

operators = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': truediv
}

rome_digits= {
    'I': 1,
    'II': 2,
    'III': 3,
    'IV': 4,
    'V': 5,
    'VI': 6,
    'VII': 7,
    'VIII': 8,
    'IX': 9

}
def calculate(s):
    if s.isdigit():
        return float(s)
    elif s in rome_digits.keys():
        is_rome = True
        s = rome_digits.get(s)
        #print(s)
        return float(s)
    else:
        print("Please enter the valid input")
    for c in operators.keys():
        left, operator, right = s.partition(c)Ш
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))

calc = input("Type calculation:\n")
print("Answer: " + str(calculate(calc)))
