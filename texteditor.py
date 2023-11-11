import os

try:
  f = open("/Users/Shared/temppp.txt", "r")
  con = f.read()
  if con == "a\n":
    con = "untitled.txt"
  elif con == "\n":
    con = "untitled.txt"
  else:
    ls = [*con]
    ls.remove("a")
    ls.remove("\n")
    con = ""
    for i in range(len(ls)):
      con = con + ls[i]
  f.close()
except:
  con = "untitled.txt"

buffer = ["test"]
file  = con
state = "--normal--"
prg = True
cursor = 0

def displayfilef(file, cursor, buffer):
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print(file + "\n********************************************************************************")
  for i in range(len(buffer)):
    bfr = buffer[i]
    if i == cursor:
      bfr = str(i) + " > " + bfr
    else:
      bfr = str(i) + "   " + bfr
    print(bfr, end="")
  print("********************************************************************************")

try:
  fs = open(file, "r")
except:
  fs = open(file, "x")
  fs.close()
  fs = open(file, "r")

if fs.read() == "":
  buffer[0] = "\n"
else:
  buffer = fs.readlines()
fs.close()
while prg:
  while state == "--normal--":
    print(state)
    inp = input()
    if inp == "t":
      state = "--edit--"
    elif inp == "e":
      prg = False
      state = ""
    elif inp == "r":
      file = input()
      if os.path.isfile(file):
        fs = open(file, "r")
        buffer = fs.readlines()
        fs.close()
    elif inp == "s":
      print(buffer)
      f = open(file, "w")
      f.truncate(0)
      f.close()
      f = open(file, "a")
      if buffer[0] != "\n":
        f.write("\n")
      for i in range(len(buffer)):
        f.write(buffer[i])
        print("gg")
      f.close()
    else:
      print("Error:\n" + inp + " is not a command")
  while state == "--edit--":
    displayfilef(file, cursor, buffer)
    print(state)
    inp = input()
    if inp == "^[[A":
      cursor -= 1
      if cursor < 0:
        cursor = 0
    elif inp == "^[[B":
      cursor += 1
      if cursor >= len(buffer):
        cursor = len(buffer) - 1
    elif inp == "\e":
      state = "--normal--"
    elif inp == "\w":
      cursor -= 1
      if cursor < 0:
        cursor = 0
    elif inp == "\s":
      cursor += 1
      if cursor >= len(buffer):
        cursor = len(buffer) - 1
    elif inp == "\\f":
      cursor = int(input())
    elif inp == "\\n":
      buffer.insert((cursor + 1), "\n")
    else:
      buffer[cursor] = inp + "\n"

buffer = []
