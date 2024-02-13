# alternative reduce
"""
Input (on command line): a list of hashtags
Output: a line plot where,
1. There is one line per input hashtag
2. The x-axis is the day of the year.
3. The y-axis is the number of tweets that use that hashtag during the year.
"""

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--keys',nargs='+',required=True)
parser.add_argument('--input_paths', required=True)
args = parser.parse_args()

# imports
import os
import json
import glob
import numpy as np
import matplotlib
mstplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from collections import Counter,defaultdict


# load each of the paths
total = defaultdict(lambda: Counter())
filepath = glob(args.input_dir + '/*')
file_path = sorted(filepath)

for key in args.keys:
    y_axis = []
    total = defaultdict(lambda: Counter())

    for path in file_path:
        with open(path) as f:
            temp = json.load(f)
            counts = 0
            try:
                for k in temp[key]:
                    counts += temp[key][k]
            except:
                pass
            y_axis.append(counts)
    plt.plot(np.arange(len(y_axis)), y_axis, label=key)

plt.xlabel("Day of 2020")
plt.ylabel("Number of Tweets")
plt.title("Number of Tweets that use # during 2020")
plt.legend()
plt.xticks([0, 60, 121, 182, 244, 305], ["Jan", "Mar", "May", "Jul", "Sep", "Nov"])
plt.savefig("line_plot.png", bbox_inches="tight")


