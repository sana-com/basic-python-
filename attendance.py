def attendance(a):
    if a>= 75:
        print("attendance percentage:", a,"eligibility: yes")
        return a
    else:
        print("attendance percentage:", a,"eligibility: no")
        return a
total_class= int(input("total classes taken: "))
att_class= int(input("classes attended: "))
a= (att_class/total_class)*100
print("attendance percentage: ",attendance(a))