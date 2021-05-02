
arr.sort()
lft = sorted(arr[::2], reverse=True)
rt = arr[1::2]
lft.extend(rt)

#above can be written as 
#a = sorted(a)
#return a[::2][::-1] + a[1::2]