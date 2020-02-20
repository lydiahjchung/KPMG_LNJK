import pandas as pd
import csv

#origin_csv = pd.read_csv("Action/training/data.csv")
#print(origin_csv.head())

#class_name = input("training class name: ")

origin_csv = open("\Action\training\data.csv", 'w', newline='', encoding='utf-8')
wr = csv.writer(origin_csv)

with open('origin_data.txt', 'r') as train_txt:
    line = train_txt.readline()
    while line != '':
        line = line.split('\t')
        line.append(class_name)
        print(line)
        line = train_txt.readline()
        
