class Shape:
    @staticmethod
    def area(height, width):
        return height * width

w = int(input())
h = int(input())

print(Shape.area(w, h))
