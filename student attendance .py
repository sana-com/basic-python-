total_class=int(input("Enter total classes : "))
class_attended=int(input("Enter total number of classes attended: "))
attendance_percentage= (class_attended/ total_class)*100
print("attendance percentage",attendance_percentage,"%")
if(attendance_percentage<75):
    print("Not eligible for exam")
else:
    print("Eligible for exam")