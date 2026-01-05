# this is for testing branch
from day12 import progress_report
# import day12
# from day12 import *

eng = int(input("enter a eng marks"))
nep = int(input("enter a nep marks"))
math = int(input("enter a math marks"))
name = input("enter a name ")



print(progress_report(
    name, eng, nep, math
))