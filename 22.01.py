from typing import Counter
 
t=[]
t=input()
s=[]
for word in t.split():
    c=""
    for letter in word:
        if letter.isalpha():#проверяет это слово или нет ибо эта команда проверяет символ буква или нет
            c+=letter.lower()#делает все заглавные буквы прописнми
    s.append(c)
d=Counter(s)
f={
    value: key
    for key , value
    in d.items()
}
#a=list(d)
print('переменая д',d)
print('переменая f',f)
a=list(f)
maxa=max(a)
print('переменая maxa',maxa)
 
print('чаще всего')
print(f.get(maxa))
m=f.get(maxa)
print('переменая m',m)
print('длинее всего')
print(max(d, key=len))
#