name = input("enter name")
if len(name)<=3:
    print("Name must be more than 3 char")
elif len(name)>50:
    print("name can be a max of 50 char")
else:
    print("good name")