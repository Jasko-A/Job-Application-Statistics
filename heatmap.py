# import numpy as np
# import pandas as pd
# import calmap
 

# all_days = pd.date_range('1/15/2014', periods=700, freq='D')
# days = np.random.choice(all_days, 500)
# events = pd.Series(np.random.randn(len(days)), index=days)



# calmap.calendarplot(events)

import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import calmap

# Import Data
df = pd.read_excel("../jobApplications18.xlsx", parse_dates=['Date'], date_format = '%Y-%m-%d')
# df.set_index('Date', inplace=True)
# print(df)
print(df)
currDate = ""
numPerDay = 0

# newArray = np.array([[currDate, 0]])
nArr = []
for index, row in df.iterrows():
     # access data using column names
     print(index)
     if(index == 0):
     	currDate = row['Date']
     elif(index == 233):
     	if currDate == row['Date'] :
     		numPerDay = numPerDay + 1
     		nArr.append([currDate, numPerDay + 1])
     	else:
     		nArr.append([currDate, numPerDay])
     		nArr.append(row['Date'], 1)
     elif((row['Date'] != currDate and numPerDay >= 1)):
     	print(currDate)
     	print(numPerDay)

     	nArr.append([currDate, numPerDay + 1])
     	#np.concatenate((newArray, newList), axis= 0)

     	#print(newList)
     	#print(len(newList))
     	#np.append(newArray, newList, axis= 0)
     	currDate = row['Date']
     	#first must assign the 
     	numPerDay = 0
     	
     else:
     	numPerDay = numPerDay + 1
     	

print(nArr)

newArray = np.asarray(nArr)

print(newArray)

df = pd.DataFrame({'Date': newArray[:,0], 'AppNum': newArray[:,1]})

print(df)

df.set_index('Date', inplace=True)
# Plot
plt.figure(figsize=(16,10), dpi= 80)
calmap.calendarplot(df['2018']['AppNum'], fig_kws={'figsize': (16,10)}, yearlabel_kws={'color':'black', 'fontsize':14}, subplot_kws={'title':'2018 Diligence of Sending Applications'})
plt.show()
