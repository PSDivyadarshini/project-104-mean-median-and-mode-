from collections import Counter
import csv

with open("data.csv",newline='') as f:
    reader= csv.reader(f)
    file_data=list(reader)


file_data.pop(0) 

new_data=[]

for i in range(len(file_data)):
    n_num=file_data[i][2]
    new_data.append(float(n_num)) 

n=len(new_data)
new_data.sort()

