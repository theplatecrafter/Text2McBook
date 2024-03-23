subject = 2
deaths = open("waysToDie.txt","r").readlines()
txt = open("text.txt","w")
import random as r

h = 10
m = 22
s = 4
yy = 2515
mm = 5
dd = 21

def ats(array):
  srt = ""
  for i in array:
    srt += i +"\n"
  
  return srt

def change(num):
  if len(str(num)) == 1:
    return "0" + str(num)
  elif len(str(num)) == 2:
    return str(num)
  
txt.write("""2514.02.27
17:22:23 - BOOTING

17:23:02 - CHAMBER\nINIT 100%

17:23:10 - CHAMBER OS\nACTIVE

17:23:12 - PREPARING\nRESOURCES... 100%

17:23:13 - JOINING\nWORLD...

17:23:15 - LOADING\nTERRAIN...

17:23:17 - LOADING\nADDONS...

17:23:20 - READY FOR\nTEST SUBJECT

17:23:22 - SUBJECT 1\nJOINED THE WORLD\nWITH UUID OF 2

17:23:23 - BEGIN TEST\n1

2514.10.22
02:05:23 - SUBJECT 1\n TERMINATED DETAILS:
<"SUBJECT1":\n"too close to border">

02:06:23 - REGENERATE\nWORLD

02:06:24 - LOADING\nTERRAIN...

02:06:25 - READY FOR\nTEST SUBJECT

02:06:26 - SUBJECT 2\nJOINED THE WORLD\nWITH UUID OF 3

02:06:27 - BEGIN TEST\n2

2515.05.22
10:21:02 - SUBJECT 2\nTERMINATED DETAILS:
<"SUBJECT2":\n"tryed to escape chamber">

10:21:50 - REGENERATE\nWORLD

10:22:02 - LOADING\nTERRAIN...

10:22:03 - READY FOR\nTEST SUBJECT\n\n""")

for i in range(0,100):
  yy+=r.randint(1,90)
  mm = r.randint(1,12)
  dd = r.randint(1,30)
  subject+=1
  txt.write(f"{change(h)}:{change(m)}:{change(s+31)} - SUBJECT {subject}\nJOINED THE WORLD\nWITH UUID OF {subject+1}\n\n")
  txt.write(f"{change(h)}:{change(m)}:{change(s+32)} - BEGIN TEST\n{subject}\n\n")
  txt.write(f"{yy}.{change(mm)}.{change(dd)}\n")
  h = r.randint(0,23)
  m = r.randint(0,60)
  s = r.randint(0,20)
  txt.write(f"""{change(h)}:{change(m)}:{change(s)} - SUBJECT {subject}\nTERMINATED DETAILS:
<"SUBJECT{subject}":\n"{deaths[r.randint(0,len(deaths)-1)][:-1]}">\n\n""")
  txt.write(f"{change(h)}:{change(m)}:{change(s+r.randint(2,12))} - REGENERATE\nWORLD\n\n")
  txt.write(f"{change(h)}:{change(m)}:{change(s+r.randint(13,24))} - LOADING\nTERRAIN...\n\n")
  txt.write(f"{change(h)}:{change(m)}:{change(s+r.randint(25,30))} - READY FOR\nTEST SUBJECT\n\n")


import pyperclip

txt.close()
out = open("text.txt","r")
hm = out.readlines()
a = 0
while a < len(hm):
  r.clipboard_clear()
  r.clipboard_append(ats(hm[a:a+14]))
  r.update()
  print(hm[a:a+14])
  a+=14
  input("next")

r.destroy()