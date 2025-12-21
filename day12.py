# def add(a,b,c):
#     print(a+b+c)

# add(1,5,3)
# add(1,15,3)
# add(1,53,3)
# add(1,115,3)
# add(1121,531,3)
# add(112,5,3)


def si(p,t,r):
    value = ((p*t*r)/100)
    return value

print(si(4,2,100))
print(si(13200,2,4))
print(si(100,22,4))
print(si(101120,2,412))
print(si(101210,2,412))

def user_info1(fname, lname):
    return f'my name is {fname} {lname}'

print(user_info1("bhandari","sudan"))


# keyword
def user_info(fname, lname):
    return f'my name is {fname} {lname}'

print("keyword",user_info(fname="sudan",lname="bhandari"))



def process_order(item, price, discount=5):
    if discount>100 or discount<0:
        return "invalid argument"
    discount_amount = price*(discount/100)
    final_price = price - discount_amount
    return f'Final price of {item} is {final_price} and received flat {discount_amount} discount'

print(process_order("macbook",450000))
print(process_order(item = "macbook",discount=4, price=10))



def force(a,g=9.8):
    print("the value of g is ",g)

force(2,99)