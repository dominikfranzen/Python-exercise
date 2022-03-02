from datetime import datetime
import handlinguserdata
import whatsmyageagain

student_surname = input("Dear student, how can I call you?")
student_lastname = input("Dear student, what is your lastname?")
student_birthdate = input("Dear student, what is your birthdate?")
formattedBirthdate = datetime.strptime(student_birthdate, '%d.%m.%Y')

if whatsmyageagain.age(formattedBirthdate) > 17:
    handlinguserdata.writeuserdatatofile([student_surname, student_lastname, student_birthdate])
else:
    print("Sorry dude, you must be 18 years or older to proceed :/")
print("Thanks, " + student_surname + " " + student_lastname + ", you birthdate is " + student_birthdate)

handlinguserdata.print_user_data()



