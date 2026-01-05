def add(name,*marks):
    print(name)
    print(marks)


# add("sudan",2,5,3,4)


def progress_report(name, *marks):
    sum = 0
    len_marks = len(marks)
    for i in marks:
        sum = sum +i

    return f'{name} percentage is {sum/len_marks} where total subject is {len_marks}'

# print(progress_report(
#     "Sudan", 50,100,12,0
# ))


def test(**kwargs):
    print(type(kwargs))

test(name="sudan", address="dang")


def testing(*args, **kwargs):
    print(args)
    print(kwargs)


testing(1,"byd",1,1,1,1,name="testing",hello = "greeting")