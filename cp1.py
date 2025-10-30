number=[]
for i in range (5):
    num=int(input(f"Enter number {i+1}: "))
    number.append(num)
total_sum=sum(number)
average= total_sum/len(number)
maximum= max(number)
minimum= min(number)
print("The total sum is=",total_sum)
print("The average is=",average)
print("The max number is=",maximum)
print("The min number is=",minimum)