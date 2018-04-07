# Martyna Miskiewicz
# Exercise 5 on how to open a file in a desired format. File was copied from Fishers iris data http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data 

with open("data/iris.csv") as f:  # this line opens the file from forlder called data
  for line in f:
   column = (line.split(',')[:4]) # this opens the first 4 columns 
   print(column)
