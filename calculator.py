print("Welcome to the GPA Calculator")
print("Enter grades and credits for 10 subjects")
print("Enter 00 for calculating GPA")
tt = 0
tc = 0
gi = 0
for i in range(1, 11):
    ai = (input("Enter grades in subject {}: ".format(i)))
    ci = (input("Enter credits for subject {}: ".format(i)))
    if ai == "A+" or ai == "a+":
        gi = 10
    elif ai == "A" or ai == "a":
        gi = 9
    elif ai == "B+" or ai == "b+":
        gi = 8
    elif ai == "B" or ai == "b":
        gi = 7
    elif ai == "C+" or ai == "c+":
        gi = 6
    elif ai == "C" or ai == "c":
        gi = 5
    elif ai == "D" or ai == "d":
        gi = 4

    if any(char.isdigit() for char in ai) and ai != "00":
        print("Invalid Input, Numeric grades not supported, Please try again")
        break
    
    ti = gi * int(ci)
    
    tt = tt + ti
    tc = tc + int(ci)

    if ai == "00":
    
        print(f'total_weighted_grades = ', tt)
        print(f'total_credits = ', tc)   
        gpa = tt / tc
        print(f'GPA = ', gpa)
        break
    elif int(ci) < 0:
        print("Invalid Input, Negative values not supported, Please try again")
        break
   
else :
    print("Input limit reached")

