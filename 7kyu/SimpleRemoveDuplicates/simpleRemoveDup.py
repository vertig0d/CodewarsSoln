def solve(arr): 
    arr_invert = arr[::-1]
    res=[]
    [res.append(i) for i in arr_invert if i not in res]
    return res[::-1]