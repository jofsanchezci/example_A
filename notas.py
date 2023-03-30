import random

def cali(l):
  cal=l.copy()
  for i in range(len(l)):
    if l[i]>4.5:
      cal[i]='E'
    if l[i]>=4 and l[i]<=4.5:
      cal[i]='B'
    if l[i]>=3.5 and l[i]<=3.9:
      cal[i]='A'
    if l[i]>=3.0 and l[i]<=3.4:
      cal[i]='R'
    if l[i]>=2.5 and l[i]<=2.9:
      cal[i]='D'
    if l[i]>=0 and l[i]<=2.4:
      cal[i]='I'
  return cal

l=[]
for i in range(11):
  num=round(random.random()*5,1)
  l.append(num)

print(l)
print(cali(l))