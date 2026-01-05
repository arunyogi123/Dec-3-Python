# read, r
# write, w
# append, a


# f = open('jan1.py','r')
# print(f.read())

# f = open('jan1.py','w')
# f.write("this is from python code")
# f.close()

# f = open('jan5.txt','a')
# f.write("\n a = this is from python code")
# f.close()

import datetime

time = datetime.datetime.now()

def handle_error(file_name, message):
    f = open(file_name, "a")
    f.write(f'\n {time} - {message}')
    f.close()


try:
    a = 10
    b = 11
    c = a/0
except TypeError as e:
    handle_error('typeerror.txt',str(e))
except NameError as e:
    handle_error('nameerror.txt',str(e))
except ZeroDivisionError as e:
    handle_error('zeroerror.txt',str(e))