import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('../jobApplications.xlsx', sep=',', header=0)

dataset = df.values
#get the values in appropriate arrays
heardArray = dataset[:,3].astype(int)
interVarray = dataset[:,4].astype(int)
offerArray = dataset[:,5].astype(int)

numApps = dataset.shape[0]  # gives number of row count

#count_row = df.shape[0]  # gives number of row count THIS CAN ALSO BE DONE WITH NUMPY ARRAYS!!!
#count_col = df.shape[1]  # gives number of col count SUCH AS DATASET

numHeard = 0
numInter = 0
numOffer = 0

for x in heardArray:
	if x == 1:
		numHeard += 1
for x in interVarray:
	if x == 1:
		numInter += 1
for x in offerArray:
	if x == 1:
		numOffer += 1

#here we calculate fractions for the pie chart
print("data set size: {}".format(numApps))
heardFrac = numHeard / numApps
interFrac = numInter / numApps
offerFrac = numOffer / numApps
noneFrac = (numApps - (numHeard + numInter + numOffer)) / numApps

fracs = [heardFrac, interFrac, offerFrac, noneFrac]
labels = ["heard back", "interviewed", "offers", "none"]
explode = (0.7, 0.5, 0.2, 0)  # only "explode" the 1st, 2nd, 3rd slices (i.e. 'Hogs')

fig, axs = plt.subplots()
axs.pie(fracs, explode=explode, labels=labels, autopct='%0.1f%%',
        shadow=False, startangle=150)
axs.set_title("Current Job Application Situation ({} Applications)".format(numApps) )
axs.axis('equal')
plt.show()


