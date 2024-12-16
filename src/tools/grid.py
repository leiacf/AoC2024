def neighbours_uneven(ver, hor, vsize, hsize):
    
    neighbours = []

    if ver > 0:
        neighbours.append((ver-1, hor)) 
    if hor > 0:
        neighbours.append((ver, hor-1))
    if hor < hsize-1:
        neighbours.append((ver,hor+1))
    if ver < vsize-1:
        neighbours.append((ver+1, hor))
    
    return neighbours

def neighbours(ver, hor, size):
    
    neighbours = []

    if ver > 0:
        neighbours.append((ver-1, hor)) 
    if hor > 0:
        neighbours.append((ver, hor-1))
    if hor < size-1:
        neighbours.append((ver,hor+1))
    if ver < size-1:
        neighbours.append((ver+1, hor))
    
    return neighbours