import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import calmap

# Import Data
excelSheets = ["../jobApplications18.xlsx", "../jobApplications19.xlsx"]
year = ["2018", "2019"]
for i in range(0,2):

	df = pd.read_excel(excelSheets[i], parse_dates=['Date'])
	# df.set_index('Date', inplace=True)
	# print(df)
	numRows = df.shape[0] #gets number of rows in dataframe
	print(numRows)
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
	     elif(index == numRows - 1):
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
	calmap.calendarplot(df[year[i]]['AppNum'], fig_kws={'figsize': (16,10)}, yearlabel_kws={'color':'black', 'fontsize':14}, subplot_kws={'title':'{} Diligence of Sending Applications'.format(year[i])})
	plt.show()
