a = ["sudan", "bhandari"]
print(len(a))
data = {
    "fname": "sudan",
    "lname": "bhandari",
}

print(data)
print(type(data))
print(len(data))


print(data["fname"])
print(data.keys())
print(data.values())

# method for adding add in dict
test = {
    "name":"hello",
    "address":['nepal','uae']
}

test['number']="1"
test['address']=1
print(test)

# {'Name': 'Ali', 'Age': 21, 'Weight': 68, 'City': 'Peshawar','Religion': 'Muslim'}
data1 = {
    "message":"hello"
}
data1.update({'message': 'Ali', 'age': 21, 'weight': 68, 'city': 'Peshawar','religion': 'Muslim'})

print(data1)
 # data deleting ways form dict

del data1['age']
# del data1


# pop
data1.pop('city')

#popitem
data1.popitem()


#clear
data1.clear()
print(data1)



# .keys
# .values
# .get

person = {
    "name": "Sudan",
    "age": 25,
    "city": "dang",
    "skills": ["Python", "Django", "Data Analysis"],
    "is_employed": False,
    "phone":[
        {
            "type":"ntc",
            "num":"9844"
        },
        {
            "type":"ncell",
            "num":"98062"
        }
    ]
}

print("Sudan ntc number is 9844")