# This script assumes that the csv files in question are structured fname,lastname,email. It also assumes that fname, lname, and email are present
# It essentially will create a new csv combining the two lists without duplicates using the email as duplicate criteria.
# If there are duplicate emails, the first name and last name on the second csv are the ones that will be prefered.

import csv

peoplefile1 = open('final_1.csv', 'r')
peoplecsv1 = csv.reader(peoplefile1)

peoplefile2 = open('final_2.csv', 'r')
peoplecsv2 = csv.reader(peoplefile2)

peopledic = {}

# Add the people from the first list to the dict
for personcsv in peoplecsv1:
    if personcsv[2] == '':
        print("The following person doesn't have an email")
        print(personcsv)
        continue
    if personcsv[0] == '' or personcsv[1] == '':
        print("The following person doesn't have a name")
        print(personcsv)
        continue
    peopledic[personcsv[2]] = [personcsv[0], personcsv[1]]

# Add the people from the second list to the dict. If the email already exists as a key in the dict, the entry will be re defined. 
for personcsv in peoplecsv2:
    if personcsv[2] == '':
        print("The following person doesn't have an email")
        print(personcsv)
        continue
    if personcsv[0] == '' or personcsv[1] == '':
        print("The following person doesn't have a name")
        print(personcsv)
        continue
    peopledic[personcsv[2]] = [personcsv[0], personcsv[1]]

peoplefile1.close()
peoplefile2.close()

# Write the un-duplicated list to a new csv
masterfile = open('final.csv', 'w')
for person in peopledic:
    linetemplate = "{first},{last},{email}\n"
    line = linetemplate.format(first=peopledic[person][0], last=peopledic[person][1], email=person)
    masterfile.write(line)
masterfile.close()