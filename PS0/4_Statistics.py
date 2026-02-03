import csv

import numpy as np
import scipy as sp

fileReader = open("tables/loans_B_unlabeled.csv", "rt", encoding="utf8")
dictReader = csv.DictReader(fileReader)

afLoanAmount = list()

afPictured = list()

for dcObservation in dictReader:
    fLoanAmount = float(dcObservation["loan_amount"])

    try:
        fPictured = float(dcObservation["pictured"])

    except ValueError:
        fPictured = 0

    afLoanAmount.append(fLoanAmount)
    afPictured.append(fPictured)

fileReader.close()

afLoanAmount = np.array(afLoanAmount)
afPictured = np.array(afPictured)

const = np.ones(len(afPictured))
X_with_const = np.vstack([const, afPictured]).T
results = np.linalg.lstsq(X_with_const, afLoanAmount)


print("Mean(Loan Amount): ", np.mean(afLoanAmount))
print("Standard Deviation(Loan Amount): ", np.std(afLoanAmount))
print("Pearson correlation(Loan Amount): ", sp.stats.pearsonr(afLoanAmount, afPictured))
print(results)
