first_name= input("Please enter your first name: ")
last_name= input("Please enter your last name: ")
age= int(float(input("Please enter your age: ")))
date_of_birt= int(float(input("Please enter your date of birt (just year): ")))
mylist= [first_name, last_name, age, date_of_birt]
for x in mylist:
  if age < 18:
    print("You can't go out because it's too dangerous")
else:
    print("You can go out to the street.")
