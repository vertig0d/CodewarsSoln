def count_developers(lst):
    # Your code here
    count =0
    for item in lst:
        if item['language'] =='JavaScript' and item['continent']=='Europe':
            count=count+1
    return count