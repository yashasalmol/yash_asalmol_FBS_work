# Write a program to check if entered year is a leap year or not. 
def CheckLeap(years):
    if(years%4==0 or years%100==0 and years%400==0):
        return True
    else:
        return False


years = int(input("Enter the year : "))
num = CheckLeap(years)
if num:
    print("The year is Leap")
else:
    print("The year is Not Leap")