def fibbo(n=5):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fibbo(n - 1)


print(fibbo(10))


def test():
    pass


# class Car():
#     wheel = 4

#     def test():
#         pass

#     def car():
#         test()


class Car:
    wheel = 4


data1 = Car()
data1.door = 10
print(data1.door)


data = Car()
print(data.wheel)

del data


class Math:
    a = 10
    b = 11

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def result(self):
        return {"add": self.add(), "sub": self.sub()}


obj = Math()
print(obj.result())


class Family():

    def __init__(self, **family_name):
        self.family_name = family_name

    def myinfo(self):
        return f'my name is {self.family_name["fname"]} {self.family_name["lname"]}'

    def father_info(self):
        return f"my father name is. {self.family_name['father_name']}"

    def overall_info(self):
        return f"{self.myinfo()}   {self.father_info()}"


obj = Family(fname="sudan", lname="bhandari", father_name="rishiraj")
print(obj.overall_info())


class Car:
    def __init__(self):
        print("i am here")

    def test(self):
        print("i am from test")

    a = 10


obj = Car()