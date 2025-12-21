'''

for <variable> in <mutlple data>:
    <varibale>
'''


# for i in [61,33,45,12,545,23423,32452]:
#     print(i+i )
#     print(f'{i} loop')
#     if i ==4:
#         print("its 4")
odd = []
even = []

for i in [61,33,45,12,545,23423,32452]:

    if (i%2==0):
        even.append(i)
    else:
        odd.append(i)
even.sort()
odd.sort()
print(even, "Even")
print(odd, "ODD")
print

for i in range(2,10,1):
    if (i%2==0):
        print(i, "even")

for i in range(2,10,1):
    if (i%2==0):
        print(i, "even")
for i in range(10,-1,-1):
    print(i)

print(",,,,,,,,,,,,,,,,")

for i in range(10,-1,-1):
    if i ==7:
        continue
    print(i)

print("....."*30)

a = [1,2,6,"sudna","hari",4,"ad","ASdasd",35]
for i in a:
    if isinstance(i, int):
        continue
    print(i)



for i in [1,2,3]:
    for j in [4,5,6]:
        print(i,j)
    print(".....")


random_num = 77
guess_time = 0
num2 = int(input("enter num2 for guess time"))
for i in range(0,num2,1):
    num = int(input("enter a number "))
    guess_time = guess_time +1
    if num == random_num:
        print(f'number match in {guess_time} time')
        break
else:
    if guess_time <=5:
        print("random number was", random_num)


name = "hahahaha"
letter = "a"
letter_position = 0
for i in name:
    if (i == letter):
        letter_position = letter_position +1
        print("letter found in", letter_position)
print(letter_position)