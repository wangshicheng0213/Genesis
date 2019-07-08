import csv
# with open('0102.csv','rt') as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader, None)
#     column = [row[1] for row in reader]
# print(column)

import networkx as nx
import matplotlib.pyplot as plt
# import csv
#
# with open('node-8.csv', 'r',encoding='UTF-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     column = [row['b'] for row in reader]
#     # id_tag0 = [row['id'] for row in reader]
# print (column)

with open('node-8.csv', 'rt',encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    column1 = [row['b'] for row in reader]
    id_tag1 = [row['id'] for row in reader]
print (column1)
print(type(column1[1]))
