#!/usr/bin/env python3
"""
visualize.py should generate a bar graph of results & store bar graph as a png file
- horizontal axis of graph should be the keys of the input file
- vertical axis should be the values of the input file
- final results should be sorted from low to high 
- includes at least the top 10 keys
"""



# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

# only the first 10 items
ten_items = items[:10]
keys = [ten_items[0] for ten_items in ten_items]
values = [ten_items[1] for ten_items in ten_items]
# reverse keys and values
keys = keys[::-1]
values = values[::-1]


# create bar graph
fig = plt.figure(figsize = (10,5))
plt.bar(range(len(keys)), values)
plt.xticks(range(len(keys)), keys)

if args.input_path[-1] == 'g':
    plt.xlabel('Language')
else:
    plt.xlabel('Country')

if args.percent:
    plt.ylabel('Percent of Tweets')
else:
    plt.ylabel('Number of Tweets')

if args.input_path[-1] == 'g':
    plt.savefig(args.key[1:] + '_lang.png')
else:
    plt.savefig(args.key[1:] + '_country.png')

print(f"Bar graph saved.")
