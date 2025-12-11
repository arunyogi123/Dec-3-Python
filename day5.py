# del
# remove
# pop
# clear
data = [1,2,3,4,5,6,7,8,9,9,"sudan"]
del data[3]



# remove
data.remove("sudan")
data.remove(9)

print(data)

# pop
data2 = ["hello",'hi']
data2.pop(0)
print(data2)

# clear

a = [1,1,2,3,4,"hello",5,6,7, True,.1]
a.clear()
print(a)

a = [1,1,2,3,4,["hello","hi"],5,6,7, True,.1]

print(a[5][0])
a[5].remove("hello")
print(a)