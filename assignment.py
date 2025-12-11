percentage = input("Enter your percentage")

# if(percentage.isalpha()):
#     print("percentage is alpha")
# else:
#     percentage = int(percentage)
#     if(percentage>100 or percentage<0):
#         print("invalid")
#     elif(percentage<=100 and percentage>=80):
#         print("Distinction")
#     elif(percentage<80 and percentage>=70):
#         print("First Division")
#     elif(percentage<70 and percentage>=60):
#         print("Second Division")
#     elif((percentage<60 and percentage>=50)):
#         print("Third Division")
#     else:
#         print("fail")


# # logical (or) and string method .lower

# has_vech = input("do you have car")
# has_vech = has_vech.lower()


# if has_vech=="yes":
#     print("")


# b = input("Enter your age ")
# if not b.isdigit():
#     print("Enter your age in number")
# else:
#     b = int(b)
#     license = input("Do you have a driving license? yes/no ").lower()
#     ride = input("Do you have your own ride? yes/no ").lower()
#     # is_license = True if license == "yes" else False
#     # is_ride = True if ride == "yes" else False
#     if b >= 18:
#         if license=="yes":
#             if ride=="yes":
#                 print("You are allowed to drive alone")
#             else:
#                 print("You have a license but not a ride")
#         else:
#             print("You are not allowed to drive")



#age=int(input("enter age"))
#license=input("has driving iscense").lower
#vehicle=input("has vehicle").lower
#is_liscense="true" if license=="yes" else False
#is_vehicle="true" if vehicle=="yes" else False
#if age>=18:
 #   if license=="yes":
  #   if vehicle=="yes":
   #     print("you are allowed to drive")
    # else:
     #   print("you have liscense but not vehicle")
    #else:
     #  print("you are not allowed")

# experience=int(input("enter experience"))
# performance_rating=int(input("enter performance rating"))
# attendance_rating=int(input("enter attendace rating"))

# if(experience>=5):
#    if(performance_rating>=4.5):
#       if(attendance_rating>=95):
#          print("Your experience is", experience, "and rating is", performance_rating ,"and attendance is ", attendance_rating, "Daimond")
#       elif(attendance_rating>=85):
#          print("Gold")
#       else:
#         print("Bronze")
#    elif(performance_rating>=3.5):
#       if(attendance_rating>=90):
#          print("Platinum")
#       else:
#          print("Silver")
#    else:
#       print("Not eligible")



experience = 5
rating = 5.5
attendance = 95

if experience >= 5:
    if rating >= 4.5:
        if attendance >= 95:
            print("Your experience is",experience,"years", "rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Platinum")
        elif attendance >= 85:
            print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Gold")
        else:
            print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Silver")
    elif rating >= 3.5:
        if attendance >= 90:
            print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Silver")
        else:
            print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Bronze")
    else:
        print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is No Bonus")

elif experience >= 2:
    if rating >= 4:
        print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Silver")
    elif rating >= 3:
        print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is Bronze")
    else:
        print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","Your Bonus is No Bonus")
else:
    print("Your experience is",experience,"years",", rating is ",rating,"and attendance is ",attendance,"%",".","You are not eligible")