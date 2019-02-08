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

resultTable = Selection(borrowerTable, 'borrowerNo', lambda colVal : int(colVal) >= 600)

for i in range(len(resultTable)):
    print(resultTable[i])