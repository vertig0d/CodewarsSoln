def square_sum(numbers):
    arr = []
    for item in numbers:
        arr.append(pow(item,2))
    return sum(arr)