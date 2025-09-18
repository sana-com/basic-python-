print("--GYM MEMBERSHIP-- \n""Monthly membership Rs.1000 \n"
      "Quartly membership Rs.2500 \n""Yearly membership Rs.9000 \n"
      "if age is less than 18 get a discount of 20%")
plan=int(input("Enter the plan (1.Monthly/2.Quartly/3.Yearly): "))
age=int(input("Enter your age: "))
if(plan==1):
    print("plan cost: Rs.1000")
    if(age<18):
        discount= 1000*(20/100)
        cost= 1000-discount
        print("plan cost: Rs.",cost)
elif(plan==2):
    print("plan cost: Rs.2500")
    if (age < 18):
        discount = 2500 * (20 / 100)
        cost = 2500 - discount
        print("plan cost: Rs.", cost)
elif(plan==3):
    print("plan cost: Rs.9000")
    if (age < 18):
        discount = 9000 * (20 / 100)
        cost = 9000 - discount
        print("plan cost: Rs.", cost)
