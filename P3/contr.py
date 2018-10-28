import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import log2

with open("survey_data.csv", 'r') as sur:
    x = list(csv.reader(sur))
    fields = np.asarray(x[0])[1:]
    dat = np.asarray(x[1:]).T[1:]

col = ['Essential', 'Nice to have', 'Dont care one way or another', 'Utterly useless']

index = range(len(fields))

dat1 = []

for i, f in enumerate(fields):
    fields[i] = f[:20]+".." if len(f) > 20 else f


for t in dat:
    ent = 0
    for c in col:
        p = (list(t).count(c))/len(t)
        if p != 0:
            ent = ent - (p*log2(p))
    dat1.append(ent)

# print(len(fields)-len(dat1))
dat2 = {fields[i]: dat1[i] for i in range(len(fields))}

# print(dat2['Shell Scripting..'])
df = pd.DataFrame.from_dict(data=dat2, orient='index', columns=['Entropy'])

df.sort_values(by='Entropy').plot.bar(figsize=(10, 10))
plt.xticks(fontsize=5, rotation=30)

plt.savefig('contr.png')
