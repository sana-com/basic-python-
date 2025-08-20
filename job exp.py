age = int(input("Enter your age: "))
job_experience = float(input("Enter your job experience in years: "))

if age > 26:
    if job_experience < 1:
        print("Not eligible for any position with less than 1 year experience.")
    elif job_experience == 1:
        print("Appointed as Junior SDE Trainee.")
    elif job_experience == 2:
        print("Appointed as Junior SDE 1.")
    elif job_experience == 3:
        print("Appointed as Junior SDE 2.")
    elif job_experience >= 4:
        print("Appointed as Senior SDE.")
else:
    print("Not eligible to apply due to age criteria (must be above 26).")

