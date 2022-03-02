import csv 

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