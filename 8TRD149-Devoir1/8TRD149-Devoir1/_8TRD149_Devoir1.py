#Requêtes à faire
#c) La liste de tous les titres de livres publiés en 2012.
#e) La liste de tous les exemplaires du livre X qui sont présentement disponibles pour emprunt.
#f) Le nom de tous les membres qui ont présentement un exemplaire du livre X en leur possession.
#g) Le nom de tous les membres ayant un livre présentement en leur possession.

#fonctionalités nécessaires
#Projection: sélectionner UNE colonne d'une table
#Select : sélectionner des lignes d'une table selon UNE condition
#HalfJoint : Sélectionner les lignes d'une table selon celle d'une autre table

import csv
from TableManip import *

with open("Book.csv", 'r', newline='') as bookFile:
    bookReader = csv.reader(bookFile, delimiter=',', quotechar='"')
    booktable = [['ISBN', 'title', 'edition', 'year']]
    for row in bookReader:
        booktable.append(row)

with open("BookCopy.csv", 'r', newline='') as bookCopyFile:
    bookCopyReader = csv.reader(bookCopyFile, delimiter=',', quotechar='"')
    bookCopyTable = [['copyNo', 'ISBN', 'available']]
    for row in bookCopyReader:
        bookCopyTable.append(row)

with open("BookLoan.csv", 'r', newline='') as bookLoanFile:
    bookLoanReader = csv.reader(bookLoanFile, delimiter=',', quotechar='"')
    bookLoanTable = [['copyNo', 'dateOut', 'dateDue', 'borrowerNo']]
    for row in bookLoanReader:
        bookLoanTable.append(row)

with open("Borrower.csv", 'r', newline='') as borrowerFile:
    borrowerReader = csv.reader(borrowerFile, delimiter=',', quotechar='"')
    borrowerTable = [['borrowerNo', 'borrowerName', 'borrowerAddress']]
    for row in borrowerReader:
        borrowerTable.append(row)



# Question C
for row in booktable:
	if row[3] == "2012":
		print(row)

# Question E
buffer = input("Titre du livre: ")
date = input("Date d'auj: [yyyy-mm-dd]")
ISBN = ""
Copies = []
for row in booktable:
	if row[1] == buffer:
		ISBN = row[0];
		break

for row in bookCopyTable:
	if row[1] == ISBN:
		Copies.append(row[0])

count = len(Copies)
year_t = date[:4]
month_t = date[5:7]
day_t = date[8:]

for row in bookLoanTable:
	for copyNo in Copies:
		if row[0] == copyNo:
			year = row[2][:4]
			month = row[2][5:7]
			day = row[2][8:]

			if int(year_t) < int(year):
				count -= 1
				break
			elif int(year_t) == int(year):
				if int(month_t) < int(month):
					count -=1 
					break
				elif int(month_t) == int(month):
					if int(day_t) < int(day):
						count -= 1
						break

			break

	if count == 0:
		break

print("Exemplaire disponible: ", count)

# Question f
buffer = input("Titre du livre: ")
date = input("Date d'auj: [yyyy-mm-dd]")
members = []
for row in booktable:
	if row[1] == buffer:
		ISBN = row[0];
		break

for row in bookCopyTable:
	if row[1] == ISBN:
		Copies.append(row[0])

year_t = date[:4]
month_t = date[5:7]
day_t = date[8:]

for row in bookLoanTable:
	for copyNo in Copies:
		if row[0] == copyNo:
			year = row[2][:4]
			month = row[2][5:7]
			day = row[2][8:]

			if int(year_t) < int(year):
				members.append(row[3])
				break
			elif int(year_t) == int(year):
				if int(month_t) < int(month):
					members.append(row[3])
					break
				elif int(month_t) == int(month):
					if int(day_t) < int(day):
						members.append(row[3])
						break

			break
	if len(members) == len(Copies):
		break


used = []
for row in borrowerTable:
	for borrowNo in members:
		if row[0] == borrowNo:
			used.append(row)

for i in used:
	print(i)

# Question g
date = input("Date d'auj: [yyyy-mm-dd]")
year_t = date[:4]
month_t = date[5:7]
day_t = date[8:]
out = []
for row in bookCopyTable:
	if row[2] == "false":
		out.append(row[0])

nDispo = []
for row in bookLoanTable:
	for i in out:
		if row[0] == i:
			year = row[2][:4]
			month = row[2][5:7]
			day = row[2][8:]

			if int(year_t) < int(year):
				nDispo.append(row[3])
				break
			elif int(year_t) == int(year):
				if int(month_t) < int(month):
					nDispo.append(row[3])
					break
				elif int(month_t) == int(month):
					if int(day_t) < int(day):
						nDispo.append(row[3])
						break

	if len(nDispo) == len(out):
		break

for row in borrowerTable:
	for i in nDispo:
		if row[0] == i:
			print(row)