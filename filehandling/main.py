import csv
# with open("test.txt",'r') as file:
#     print(file.read())

# with open('demo.txt','w+') as file:
#     file.write('Hello roshan.')

data = [["Name", "course", "Fee"],
       ["Ajay", "DS", "1000"],
       ["Bijay", "ML", "2000"]]

with open('csvdata.csv', 'w') as file:
    File = csv.writer(file)
    for i in data:
        File.writerow(i)
