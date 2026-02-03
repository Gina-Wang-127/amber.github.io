import csv

fileReader = open("tables/loans_B_unlabeled.csv", "rt", encoding="utf8")
dictReader = csv.DictReader(fileReader)

nIncludeChicken = 0

for dcObservation in dictReader:
    cDesc = dcObservation["description"]
    if "chicken" in cDesc.lower():
        nIncludeChicken += 1


fileReader.close()
print("Number including chicken: ", nIncludeChicken)
