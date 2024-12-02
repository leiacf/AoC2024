def strings_to_ints(data):
    
    ints = []

    for line in data:
        
        temp = []
        strings = line.split()

        for string in strings:
            temp.append(int(string))

        ints.append(temp)

    return ints