# class Laptop:
#     def __init__(self):
#         print("hello world")
#         pass
#     def config(self):
#         print("asus","17","1TB")
# laptop1=Laptop()
# laptop2=Laptop()
# # Laptop.config(laptop1)
# # Laptop.config(laptop2)
# laptop1.config()
# laptop2.config()



# class student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
        
#     def info(self):
#         print("name is:",self.name,"rollno.:",self.rollno)
# s1=student("jacb","65")
# s2=student("tony","87")
# s1.info()  
# s2.info()      

# print(id(s1))
# print(id(s2))
# class person:
#     def __init__(self):
#         self.name="ishan"
#         self.number=32
#     def compare(self,other):
#         if(self.number==other.number):
#             return True
#         else:
#             return False

# p1=person()
# p2=person()  
# p1.name="ashwin"  #this way we can change the output results
# if p1.compare(p2):
#     print("same")
# else:
#     print("different")    

# print(p1.name)
# print(p2.name)
   





# class car:
#     wheel=4
#     #static or class variable-values are constant(for car ,tyre etc)
#     #instance variables-value varies from obj to obj
#     def __init__(self):
#         self.company="bmw"
#         self.mileage=10

# c1=car()
# c2=car()

# print(c1.company,c1.wheel)
# print(c2.company)
# print(c1.mileage)
# print(c2.mileage)

class students:
    collegename="LPU"
    def __init__(self,python,web,math):
        self.sub1=python
        self.sub2=web
        self.sub3=math
    def avg(self,python,web,math):
        print((python+web+math)/3)
    @classmethod 
    def collegedetails(cls):
        return cls.collegename



s1=students(4,7,8)
s1.avg(4,7,8)
s2=students(3,5,3)
s2.avg(3,5,3)
print(students.collegedetails())



















