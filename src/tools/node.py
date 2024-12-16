class Node:
    
    value = ""
    neighbours = []
    point = ()
    visited = False

    def __init__(self, value, ver, hor):
        self.set_value(value)
        self.set_point(ver, hor)

    def set_value(self, value):
        self.value = value
    
    def get_value(self):
        return self.value
    
    def set_neighbours(self, neighbours):
        self.neighbours = neighbours

    def get_neighbours(self):
        return self.neighbours

    def get_point(self):
        return self.point

    def set_point(self, ver, hor):
        self.point = (ver,hor)

    def get_visited(self):
        return self.visited

    def set_visited(self, visited):
        self.visited = visited

    def __str__(self):
        return ("Value: {} Point {}".format(self.value, self.point))