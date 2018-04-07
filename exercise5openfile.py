with open("data/iris.csv") as f:
  for line in f:
   column = (line.split(',')[:4])
   print(column)
