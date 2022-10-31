import csv
import matplotlib.pyplot as plt

File = open('data/coding-environment-exercise.csv')
exampleReader = csv.reader(File)
exampleData = list(exampleReader)
len = len(exampleData)
x = list()
y = list()

for i in range(1, len):
    x.append(exampleData[i][0])
    y.append(exampleData[i][1])

plt.plot(x, y)
plt.show()
