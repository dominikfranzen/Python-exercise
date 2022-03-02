from datetime import date

def age(birthdate):
    today = date.today()
    yearDifference = today.year - birthdate.year
    hadBirthdaythisyear = (today.month, today.day) < (birthdate.month, birthdate.day)
    if hadBirthdaythisyear :
        return yearDifference - 1
    return yearDifference