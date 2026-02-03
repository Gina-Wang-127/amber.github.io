import csv
import random

fileReader = open("tables/loans_B_unlabeled.csv", "rt", encoding="utf8")
csvReader = csv.reader(fileReader)


fileWriter = open(
    "tables/loans_B_unlabeled_subset.csv", "w", encoding="utf8", newline=""
)
csvWriter = csv.writer(fileWriter)

acHeader = next(csvReader)
csvWriter.writerow(acHeader)

random.seed(10025)

for acRow in csvReader:
    if random.random() < 0.01:
        csvWriter.writerow(acRow)

fileReader.close()
fileWriter.close()
