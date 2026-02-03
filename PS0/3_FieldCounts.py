import csv

fileReader = open("tables/loans_B_unlabeled.csv", "rt", encoding="utf8")
dictReader = csv.DictReader(fileReader)

dTable = dict()

for dcObservation in dictReader:
    # 1. 获取国家 (Categorizing by countries)
    cCountry = dcObservation["country"]

    # 2. 获取贷款金额，并转化为浮点数 (Hint: use float(x))
    # 注意：这里假设你的CSV里金额列名叫 "loan_amount"
    # 如果报错 KeyError，请检查列名是否为 "loan_amount"
    cAmount = float(dcObservation["loan_amount"])

    if cCountry not in dTable:
        # 如果是第一次遇到这个国家，初始值就是当前的贷款金额
        dTable[cCountry] = cAmount
    else:
        # 如果已经存在，则累加金额
        dTable[cCountry] += cAmount

fileReader.close()

# 专门打印 Haiti 的结果回答 Q9
haiti_total = dTable.get("Haiti", 0)

print(f"Total value of loans to Haiti: {haiti_total}")
