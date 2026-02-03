import collections
import csv

import numpy as np

fileReader = open("tables/loans_B_unlabeled.csv", "rt", encoding="utf8")
dictReader = csv.DictReader(fileReader)

acPositive = ["progress", "success", "profit", "well", "good"]
acNegative = ["patience", "fear", "wait", "unexpected", "delay"]

anSentiment = []


for dcObservation in dictReader:
    acRepaymentComments = dcObservation["description"].lower()

    nSentiment = 0

    for cWord in acPositive:
        nSentiment += acRepaymentComments.count(cWord)

    # FOR YOU TO DO: update the sentiment score for negative words
    for cWord in acNegative:
        nSentiment -= acRepaymentComments.count(cWord)

    anSentiment.append(nSentiment)


fileReader.close()

freq = dict(collections.Counter(anSentiment))
freq = {x: freq[x] for x in sorted(freq.keys())}


print("Sentiment Frequency:\n", freq)
