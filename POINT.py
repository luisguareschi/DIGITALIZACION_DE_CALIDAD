class Point:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


point1 = Point(0, 'Luis', 20)

print('ID:', str(point1.id),'\nName:', point1.name, '\nAge:', point1.age)
