#creates a double bar graph of average weekly violent crime rate during dry weather and precipitation

#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random
import math
import numpy as np

fig, ax = plt.subplots()
def plot(crimes, dryMeans, precipMeans):
    N = 8
    ind = np.arange(N)+2  # the x locations for the groups
    width = 0.35        # the width of the bars

    rects1 = ax.bar(ind, dryMeans, width, color='b')

    rects2 = ax.bar(ind + width, precipMeans, width, color='r')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Crimes Committed')
    ax.set_title('Average Weekly Violent Crime Rate in Dry Weather and Precipitation')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels((crimes), fontsize = 6)

    ax.legend((rects1[0], rects2[0]), ('Precipitation', 'Dry'))
    autolabel(rects1)
    autolabel(rects2)

    # Save the plot into a PDF file
    fig.savefig("plot.pdf")
    
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.2f' % float(height),
                ha='center', va='bottom', fontsize = 5)
