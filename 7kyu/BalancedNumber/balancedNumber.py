#a = [9, 5, 9]
number = 1024
a = list(map(int, str(number)))
if len(a)%2 == 0:
    l = sum(a[:len(a)//2 -1])
    r = sum(a[len(a)//2 + 1:])
    d = 'balanced' if l == r else 'not balanced'
else:
    l = sum(a[:len(a)//2])
    r = sum(a[len(a)//2 + 1:])
    d = 'balanced' if l == r else 'not balanced'
print(d)
