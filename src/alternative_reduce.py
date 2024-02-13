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
args = parser.parse_args()

# imports
import os
import json
import glob
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from collections import Counter,defaultdict
from datetime import datetime

# load each of the paths
total = defaultdict(lambda: Counter())
path = glob.glob('outputs/geoTwitter*.zip*')

for p in path:
    with open(p) as f:
        tmp = json.load(f)
        name = os.path.basename(p)
        date = name[10:18]
        for key in args.keys:
            if key in tmp:
                if key not in total:
                    total[key] = {}
                if date not in total[key]:
                    total[key][date] = []
                total[key][date].append(sum(tmp[key].values()))

fig, ax = plt.subplots()

for key in args.keys:
    days = sorted(total[key].keys())
    vals = [sum(total[key][date]) for date in days]
    day = [datetime.strptime(date, '%y-%m-%d') for date in days]
    ax.plot(day, vals, label=key)

ax.set_xlabel('Date (Year-Month-Day)')
ax.set_ylabel('Number of Tweets')
ax.set_title('Number of Tweets per Day')
ax.legend()


plt.savefig('line_plot.png', bbox_inches='tight')







plt.xlabel("Day of 2020")
plt.ylabel("Number of Tweets")
plt.title("Number of Tweets that use # during 2020")
plt.legend()
plt.xticks([0, 60, 121, 182, 244, 305], ["Jan", "Mar", "May", "Jul", "Sep", "Nov"])
plt.savefig("line_plot.png", bbox_inches="tight")


