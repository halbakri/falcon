!/usr/bin/env python
# coding: utf-8

# # Wine
# ### Using chemical analysis determine the origin of wines
# ![Wine](http://archive.ics.uci.edu/ml/assets/MLimages/Large109.jpg)
# 
# ### Source:
# 
# Original Owners:
# 
# Forina, M. et al, PARVUS -
# An Extendible Package for Data Exploration, Classification and Correlation.
# Institute of Pharmaceutical and Food Analysis and Technologies, Via Brigata Salerno,
# 16147 Genoa, Italy.
# 

# ## Data Set Information:
# 
# |classification context|
# |-----------------|
# |  Alcohol        |
# | Malic acid      |
# |  Ash            |
# |Alcalinity of ash|
# | Magnesium       |
# |  Total phenols  |
# |  Flavanoids     |
# |Nonflavanoid phenols|
# |Proanthocyanins |
# |Color intensity  |
# | Hue             |
# |OD280/OD315 of diluted wines|
# |Proline          |
# 

# ## Import Libraries


import urllib3
import shutil
from numpy import genfromtxt
from os import remove
from halcon import search
from time import time
from sys import exit


# This example uses the wine dataset from
# 
# Machine Learning Repository
# Center for Machine Learning and Intelligent Systems
# http://archive.ics.uci.edu/ml/datasets/Wine

# [Wine Link click here](http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data)

# ## Using feature vectors as query wine set and use the rest to finid similar images





url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
filename = 'data.csv'

http = urllib3.PoolManager()
with open(filename, 'wb') as out:
    r = http.request('GET', url, preload_content=False)
    shutil.copyfileobj(r, out)

data = genfromtxt( filename, delimiter=',' )

print("I will use the first three feature vectors as my query wine set")
query_wines = []
query_wines.append(['wine0', 1, data[0]])
query_wines.append(['wine1', 1, data[1]])
query_wines.append(['wine2', 1, data[2]])

print("\nAnd I will use the rest of the feature vectors to find the most similar images")


# ## Displaying top 10 results



dataset = []
counter = 1
for datum in data:
	dataset.append([ 'wine' + str(counter), 1, datum ])
	counter = counter + 1

t = time()
[iids, scores] = search.query( query_wines, dataset, metric='cityblock', normalization='standard' )
t = time() - t
print("Elapsed time: " + str(t) + " seconds\n")

#icaoberg: i will only display the top ten results
iids = iids[0:10]
scores = scores[0:10]

#icaoberg: just in case people do not have the tabulate package
try:
	from tabulate import tabulate
	rank = 0
	table = []

	for index in range(len(iids)):
		table.append([str(rank), str(iids[index]), str(scores[index])])
		rank = rank + 1

	print(tabulate(table, headers=["Ranking","Identifier", "Score"]))
except:
	print("rank\tiid\t\tscore")

	rank = 0
	for iid, score in zip(iids,scores):
		print(str(rank) + "\t" + str(iid) + "\t\t" + str(score))
		rank = rank + 1

remove(filename)

#icaoberg: this line is neccesary so i can test this example in travis/jenkins
if iids[0] == 'wine1':
 	exit(0)
else:
	exit("\nTop match was not query image. Something went wrong with this example")


!/usr/bin/env python
# coding: utf-8

# # Wine
# ### Using chemical analysis determine the origin of wines
# ![Wine](http://archive.ics.uci.edu/ml/assets/MLimages/Large109.jpg)
# 
# ### Source:
# 
# Original Owners:
# 
# Forina, M. et al, PARVUS -
# An Extendible Package for Data Exploration, Classification and Correlation.
# Institute of Pharmaceutical and Food Analysis and Technologies, Via Brigata Salerno,
# 16147 Genoa, Italy.
# 

# ## Data Set Information:
# 
# |classification context|
# |-----------------|
# |  Alcohol        |
# | Malic acid      |
# |  Ash            |
# |Alcalinity of ash|
# | Magnesium       |
# |  Total phenols  |
# |  Flavanoids     |
# |Nonflavanoid phenols|
# |Proanthocyanins |
# |Color intensity  |
# | Hue             |
# |OD280/OD315 of diluted wines|
# |Proline          |
# 

# ## Import Libraries



import urllib3
import shutil
from numpy import genfromtxt
from os import remove
from halcon import search
from time import time
from sys import exit


# This example uses the wine dataset from
# 
# Machine Learning Repository
# Center for Machine Learning and Intelligent Systems
# http://archive.ics.uci.edu/ml/datasets/Wine

# [Wine Link click here](http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data)

# ## Using feature vectors as query wine set and use the rest to finid similar images



url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
filename = 'data.csv'

http = urllib3.PoolManager()
with open(filename, 'wb') as out:
    r = http.request('GET', url, preload_content=False)
    shutil.copyfileobj(r, out)

data = genfromtxt( filename, delimiter=',' )

print("I will use the first three feature vectors as my query wine set")
query_wines = []
query_wines.append(['wine0', 1, data[0]])
query_wines.append(['wine1', 1, data[1]])
query_wines.append(['wine2', 1, data[2]])

print("\nAnd I will use the rest of the feature vectors to find the most similar images")


# ## Displaying top 10 results



dataset = []
counter = 1
for datum in data:
	dataset.append([ 'wine' + str(counter), 1, datum ])
	counter = counter + 1

t = time()
[iids, scores] = search.query( query_wines, dataset, metric='cityblock', normalization='standard' )
t = time() - t
print("Elapsed time: " + str(t) + " seconds\n")

#icaoberg: i will only display the top ten results
iids = iids[0:10]
scores = scores[0:10]

#icaoberg: just in case people do not have the tabulate package
try:
	from tabulate import tabulate
	rank = 0
	table = []

	for index in range(len(iids)):
		table.append([str(rank), str(iids[index]), str(scores[index])])
		rank = rank + 1

	print(tabulate(table, headers=["Ranking","Identifier", "Score"]))
except:
	print("rank\tiid\t\tscore")

	rank = 0
	for iid, score in zip(iids,scores):
		print(str(rank) + "\t" + str(iid) + "\t\t" + str(score))
		rank = rank + 1

remove(filename)

#icaoberg: this line is neccesary so i can test this example in travis/jenkins
if iids[0] == 'wine1':
 	exit(0)
else:
	exit("\nTop match was not query image. Something went wrong with this example")



