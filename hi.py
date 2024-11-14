import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
vector=[]
df = pd.read_csv("2024-10-30-001-alltracks.csv")
x = pd.DataFrame(df)
diffco = x[[' Diffusion Co']]/100
particleID = x[['Particle ID']]
diffco.std()
i=0

array2 = []
for j in range(np.size(particleID['Particle ID'])):
    array2.append(int(particleID['Particle ID'][j]))

array = np.where(np.roll(array2,1)!=array2)[0]
for i in range(np.size(array)):
    vector.append(diffco[' Diffusion Co'][array[i]])
    myvector = set(vector)
print('Mean: ' + str(np.mean(vector)))
print('Std: ' + str(np.std(vector)))
counts, bins = np.histogram(diffco)
plt.xlabel('D in $\mu m^2/s$')
plt.ylabel('Partikelanzahl')

plt.xticks(range(0,30,5))
plt.yticks(range(0,1000,100))#changes x and y labels
plt.hist(vector, bins=110, range=(0,25), density=False, histtype='bar', align='mid', edgecolor='black' )
plt.text(20, 800, 'Messung', fontdict=None)
plt.text(20, 750, '$\overline{D}=6.28$', fontdict=None)
plt.text(20, 700, '$s_D=8.19$', fontdict=None) #changes where text is

plt.show()
