import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

with open("survey_data.csv", 'r') as sur:
    x = list(csv.reader(sur))
    fields = np.asarray(x[0])[1:]
    dat = np.asarray(x[1:]).T[1:]

col = ['Essential', 'Nice to have', 'Dont care one way or another', 'Utterly useless']

index = range(len(fields))

dat1 = []

for i, f in enumerate(fields):
    fields[i] = f[:15]+".." if len(f) > 15 else f


for t in dat:
    dat2 = []
    for c in col:
        dat2.append(list(t).count(c))
    dat1.append(dat2)

df = pd.DataFrame(data=dat1, columns=col)

df.plot.bar(stacked=True, figsize=(10, 10))

plt.xticks(index, fields, fontsize=5, rotation=30)

plt.savefig('hists.png')

