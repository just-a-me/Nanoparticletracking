import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
vector=[]
df = pd.read_csv("Gold_Shutter483_dur90-002-alltracks.csv")
x = pd.DataFrame(df)
diffco = x[[' DiffusionCo']]/100
particleID = x[['ParticleID']]
diffco.std()
for i  in range(1, 2242):
    for j in range(np.size(particleID)):
        if i == particleID['ParticleID'][j]:
            candidate = j
            break
    vector.append(diffco[' DiffusionCo'][candidate])
    myvector = set(vector)
print('Mean' + str(np.mean(vector)))
print('Std' + str(np.std(vector)))
counts, bins = np.histogram(diffco)
plt.xlabel('D in $\mu m^2/s$')
#print(np.std(myvector))
plt.xticks(range(0,20,5))
plt.yticks(range(0,250,50))
plt.hist(myvector, bins=110, range=(0,20), density=False, histtype='bar', align='mid', edgecolor='black' )
plt.text(17, 191, 'Messung', fontdict=None)
plt.text(17, 180, '$\overline{D}=2.49$', fontdict=None)
plt.text(17, 169, '$s_D=0.57$', fontdict=None)

plt.show()
print(diffco.std())