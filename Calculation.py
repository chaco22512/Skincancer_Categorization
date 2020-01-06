# -*- coding: utf-8 -*-

from Segment import*
from data import*

Benign = load_pc("Benign")

SB=segment(Benign)

SB.info()
SB1 = SB[SB['Seg']>0]

Malignant = load_pc("Malignant")

MB = segment(Malignant)

MB.info()
MB1 = MB[MB['Seg']>0]

print(SB1.describe())

print(MB1.describe())

A = np.arange(SB1.shape[0])
print(A)
SB1.index = A

# labeling and concatenation

# In order to fix the number of the sample between the Benign(129) and malignant(71), we delete the benign data randomly.

dif = SB1.shape[0]-MB1.shape[0]
print(dif)

indi = np.random.choice(SB1.shape[0],dif, replace=False) 
print(indi)

SB1.drop(index=indi, inplace=True)
SB1.info()

#labeling
SB1['label'] = 'B'
MB1['label'] = 'M'

# Concatanation and shuffling
Data = pd.concat([SB1, MB1])

#shuffling
Data = Data.sample(frac=1, random_state=0)
Data

Data.to_csv(r'C:/Users/admin/Desktop/MachineLearning/Miniproject/data2.csv', index = False)

