import re

morse = {}
out = []

with open("morse.txt", "r") as f:
  for line in f.read().split("\n"):
    line = re.sub(" +", " ", line).strip().split(" ")
    if (len(line) == 2):
      morse[line[0]] = line[1].lower()

with open("vstup.txt", "r") as f:
  for line in f.read().split("\n"):
    for symbol in line.split("/"):
      if symbol == "":
        out.append(" ")
      elif symbol in morse:

        out.append(morse[symbol])

    out.append("\n")

out.pop()print("".join(out), file=open("vystup.txt", "w"))
