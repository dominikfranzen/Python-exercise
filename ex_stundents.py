import csv
from datetime import datetime
from datetime import date
from time import strptime

def age(birthdate):
    today = date.today()
    yearDifference = today.year - birthdate.year
    hadBirthdaythisyear = (today.month, today.day) < (birthdate.month, birthdate.day)
    if hadBirthdaythisyear :
        return yearDifference - 1
    return yearDifference

def writeuserdatatofile(data):
    with open('students.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

def print_user_data():
    print("These students are registered:")
    with open('students.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

student_surname = input("Dear student, how can I call you?")
student_lastname = input("Dear student, what is your lastname?")
student_birthdate = input("Dear student, what is your birthdate?")
formattedBirthdate = datetime.strptime(student_birthdate, '%d.%m.%Y')

if age(formattedBirthdate) > 17:
    writeuserdatatofile([student_surname, student_lastname, student_birthdate])
else:
    print("Sorry dude, you must be 18 years or older to proceed :/")
print("Thanks, " + student_surname + " " + student_lastname + ", you birthdate is " + student_birthdate)

print_user_data()



