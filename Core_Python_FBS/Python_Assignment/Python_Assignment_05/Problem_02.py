num = int(input("Enter a number of students : "))
totaal_percentage = 0
for i in range(1,num+1):
    m1 = int(input("Enter marks 1: "))
    m2 = int(input("Enter marks 2: "))
    m3 = int(input("Enter marks 3: "))
    m4 = int(input("Enter marks 4: "))
    m5 = int(input("Enter marks 5: "))
    total_marks = m1 + m2 + m3 + m4 + m5
    percentage = (total_marks/500)*100
    totaal_percentage+=percentage
    print(f"percentage of student {i} : {percentage}%")
average = totaal_percentage/num
print(f"Average percentage of student : {average}")