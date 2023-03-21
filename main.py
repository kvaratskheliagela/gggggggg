#first homework
#class Rectangle:
#    def __init__(self, width,  length, color):
#        self.width = width
#        self.length = length
#        self.color = color
#    def perimeter(self):
#        return 2 * (self.width + self.length)
#    def area (self):
#        return (self.width * self.length)
#obj1=Rectangle(5,1,"blue")
#print(obj1.width)
#print(obj1.length)
#print(obj1.color)
#print(obj1.perimeter())
#print(obj1.area())
#obj2=Rectangle(3,3,"green")
#obj3=Rectangle(3,7,"purple")
# twice homwork
# class Car:
#    def __init__(self, color, brend, model):
#        self.color = color
#        self.brend = brend
#        self.model = model
#    def __str__(self):
#        return f"manqnis brendi aris: {self.brend}, manqnis modelis {self.model}, manqnis feria {self.color} "
# mashina=Car("red","ford","mustang")
# print(mashina.brend)
# print(mashina.model)
# print(mashina.color)
# mashina_2=Car("red","ford","mustang")
# mashina_3=Car("red","ford","mustang")
#mesame ar maxsovs rogoraa
class Dog:
    def __init__(self,breed="maltese" ,size= "small" , age=2 ,color= "white" ):
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color
    def sleep(self):
        return  "dzagls dzinavs"
    def run(self):
        return "dzagli darbis"
    def eat(self):
        return "dzagli wams"
    def sit (self):
        return"dzagli zis"
rect_one=Dog("neapolitan mastiff" , "large" , 5 , "black")
print(rect_one.breed)
print (rect_one.size)
print (rect_one.color)
print(rect_one.age)
rect_two=Dog()
rect_three=Dog("chow chow" , "medium" , 3 ,"brown")
