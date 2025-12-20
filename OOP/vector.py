class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def __add__(self, vector):
        return Vector((self.__x + vector.getX()), self.__y + vector.getY())
    
    def __sub__(self, vector):
        return Vector(self.__x - vector.getX(), self.__y - vector.getY())
    
    def __mul__(self, vector):
        return Vector(self.__x * vector.getX(), self.__y * vector.getY())
    
    def __eq__(self, vector):
        return self.__x == vector.getX() and self.__y == vector.getY()
    
    def __repr__(self):
        return f"Vector({self.__x}, {self.__y})"
    
v1 = Vector(1,1)
v2 = Vector(2,2)

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print((v1 * v2) == (v1 * v2))
print(v1)