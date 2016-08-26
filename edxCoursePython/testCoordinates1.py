class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, n):
        if self.x == n.getX() and self.y == n.getY():
            return True
        else:
            return False

    def __repr__(self):
        return self.__class__.__name__ + "(" + str(self.getX()) + ", " + str(self.getY()) + ")"


a = Coordinate(1, 2)
print a.getX(), a.getY()
b = Coordinate(2, 2)
print repr(a)
c = eval(repr(a))
print eval(repr(a)) == a
