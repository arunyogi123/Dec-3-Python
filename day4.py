a = [1,1,2,3,4,"hello",5,6,7, True,.1]
print(type(a))
print(a[5])

print(len(a))
print(a[10], a[-11])


print(a[5:9])


# append
# insert
# extend
# concat
data = ['hello','hi']
data.append("namaste")
print(data)

# insert
data2 = ["sudan","ramesh",'hari']
data2.insert(100000,"bhandari")
print(data2)


# extends
data1 = [1,2,3]
data3 = [4,5,6]
data3.extend(data1)
print(data3)

# concat
a = [1,2]
b = ["hello","hi"]
c = a+b
print(c)


# 2 input
# add input marks in list
# add list item using index value
# percentage = total /2
# percentage = int(percentage)
marks=[]
eng = int(input("enter a marks"))
math = int(input("enter a marks"))
marks.append(eng)
marks.append(math)
total = marks[0]+marks[1]
percentage = total/2