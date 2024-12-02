def strings_to_ints(data):
    
    ints = []

    for line in data:
        
        temp = [int(x) for x in line.split()]
        ints.append(temp)

    return ints