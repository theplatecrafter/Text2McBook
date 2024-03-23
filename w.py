file = open("hm.txt","r")
w = file.readlines()

import pyperclip as p
for i in w:
  p.copy(i)
  input("next")