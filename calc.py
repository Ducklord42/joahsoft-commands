inp = "" #input for the calc, example: "12x3"

def numorchar(ino):
  icc = ino.isnumeric()
  if icc:
    return "n"
  elif ino == " ":
    return "b"
  else:
    return "c"

ans = 0
c_char = "b"
last_char = "b"
while True:
  inp = input()
  if inp == "exit":
    break
  else:
    inpa = inp.split(" ")
    a = inpa[0]
    b = int(inpa[2])
    op = inpa[1]
    if a == "ans":
      a = ans
    else:
      a = int(a)
    if op == "/":
      ans = a / b
    elif op == "x":
      ans = a * b
    elif op == "*":
      ans = a * b
    elif op == "+":
      ans = a + b
    elif op == "-":
      ans = a - b
    print(str(ans))