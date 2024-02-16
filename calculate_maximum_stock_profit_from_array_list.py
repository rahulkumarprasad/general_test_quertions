def profit(data):
    min_val = data[0]
    max_val = data[0]
    min_day = 1
    max_day = 1
    i=1
    
    for num in data:
        if num < min_val:
            min_val = num
            min_day = i
        
        if num > max_val:
            max_val = num
            max_day = i
        
        if min_day > max_day:
            max_val = num
            max_day = i
            
        i+=1
    
    if min_day >= max_day:
        return 0
    else:
        return max_val - min_val

print(profit([7,  5, 3, 6, 4, 1]))
print(profit([7,  1, 5, 3, 6, 4, 1]))
    
