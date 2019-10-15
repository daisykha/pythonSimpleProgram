class Vector(object):
    def __init__(self, data = None):
        self._vector = []
        if (data is not None):
            for value in data:
                self._vector.append(float(value))
    def __str__(self):
        if len(self._vector) == 0:
            return "<>"
        else:
            output = "<"
            for value in self._vector[:-1]:
                output += str(value) + ", "
            output += str(self._vector[-1]) +">"
            return output
    def dim(self):
        return len(self._vector)
    def get(self,i):
        return self._vector[i]
    def set(self,index,value):
        self._vector[index]=value
    def scalar_product(self, scalar):
        product = []
        for value in self._vector:
            product.append(scalar * value)
        new_vector = Vector(product)
        return  new_vector
    def add(self, vector2):
        added = []
        for index in len(vector2):
            self.added.append(self._vector[index]+vector2[index])
        new_vector = Vector(added)
        return new_vector
    
my_vector=Vector([1,2,3])
empty_vector = Vector()
print(my_vector)
print(empty_vector)
print(my_vector.dim())
print(empty_vector.dim())
print(my_vector.get(1))
print(my_vector.set(1,3))
print(my_vector.scalar_product(2))
vector1 = Vector([1, 2, 3])
vector2 = Vector([0, 1, 3])
print(vector1.add(vector2))
