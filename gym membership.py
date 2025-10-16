def gym_mem(age):
    if age>18:
        print("your plan: ",plan,"discount: ",discount)
        return age
    else:
        print("your plan: ", plan, "discount: no discount")
        return age
age=int(input("enter your age: "))
print("plans \n","1.monthly=1000\n","2.quaterly=2500\n","3.yearly=9000\n")
plan= int(input("enter your plan:(1-3) "))
if plan==1:
    discount= 1000-(1000*0.18)
elif plan==2:
    discount = 2500 - (2500 * 0.18)
else:
    discount = 9000 - (9000 * 0.18)