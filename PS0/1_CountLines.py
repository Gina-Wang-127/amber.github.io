import csv

fileReader = open("tables/loans_B_unlabeled.csv", "rt", encoding="utf8")
csvReader = csv.reader(fileReader)

acHeader = next(csvReader)


nObservations = 0

for acRow in csvReader:
    nObservations += 1

fileReader.close()
print("Total Number of Loans", nObservations)
