
vvod=str(input())
vvod=vvod.replace('.',' ').replace(',',' ').replace('-',' ').replace(':',' ').replace(';',' ').replace('_',' ')
print(vvod)
dlin= str(vvod).split()
s=max(dlin, key=len)
print('самое длинное',s)
from collections import Counter 
  

chasto = vvod.split() 
Counter = Counter(chasto )   
chastovst = Counter.most_common(1) 
print('самое chastoe',chastovst[0][0])
print('yjdjt')