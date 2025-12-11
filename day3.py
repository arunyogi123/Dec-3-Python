# # if(70>=80):
# #     print("dis")
# #     a = 10
# #     b = 11
# #     print(a+b)
# # else:
# #     print("fail")

# if(1==1):
#     print("if condition")
# elif(1>10):
#     print("elif condition")
# elif(1==10):
#     print("2nd else condiiton")
# else:
#     print("else")


# percentage = "71.25"


# '''
# logical
# comparison
# if
# string or int

# input ['optional']
# '''

# a = True
# if(a):
#     print("True")
# else:
#     print("False")


# age = 2
# citizenship = "Nepal"

# if age >= 18:
#     print("You are an adult.")

#     if citizenship == "Nepal":
#         print("You are eligible to vote in Nepal.")
#     else:
#         print("You are not a Nepali citizen.")
# else:

#     print("You are not an adult yet.")

citizenship = "Nepals"

if citizenship == "Nepal":
    print("You are eligible to vote in Nepal.")
else:
    print("You are not a Nepali citizen.")


message = (
    "You are eligible to vote in Nepal."
    if citizenship == "Nepal"
    else "You are not a Nepali citizen."
)
print(message)


experience = 4
rating = 2
attend = 60