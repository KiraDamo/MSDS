#Written by Kira Damo
#Submitted June 7th
#I have not given or received any unauthorized assistance on this assignment.
#https://www.youtube.com/watch?v=bkIMWmMBc38

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

try:
    hw_df = pd.read_csv('Heights_and_Weights.csv', sep=',')
except FileNotFoundError:
    print('File not found. Please try again')
    exit()

#sorting data into female and male
female_heights = hw_df[hw_df['Sex'] == 'Female']['Height']
male_heights = hw_df[hw_df['Sex'] == 'Male']['Height']

#printing the mode and mean
print('Female Heights Mode: ', female_heights.mode())
print('Female Heights Mean: ', female_heights.mean())
print('Male Heights Mode: ', male_heights.mode())
print('Male Heights Mean: ', male_heights.mean())

#number of bins
bin_width = 5
bins=range(int(min(hw_df['Height'])), int(max(hw_df['Height'])) + bin_width, bin_width)

#plotting both histograms
plt.hist(female_heights, bins=bins, density=True,
         alpha= 0.75, color='pink', label='Female Heights')
plt.hist(male_heights, bins=bins, density=True,
         alpha= 0.75, color='tab:blue', label='Male Heights')

#vertical lines for the mean
plt.axvline(female_heights.mean(), color='r', label='Female Height Mean')
plt.axvline(male_heights.mean(), color='g', label='Male Height Mean')

#calculates area under the histogram
female_hist_vals, female_bin_edges = np.histogram(female_heights, bins=bins, density=True)
female_area = np.sum(female_hist_vals * np.diff(female_bin_edges))
print('Area under female height histogram: ', female_area)

male_hist_vals, male_bin_edges = np.histogram(male_heights, bins=bins, density=True)
male_area = np.sum(male_hist_vals * np.diff(male_bin_edges))
print('Area under male height histogram: ', male_area)

plt.legend(fontsize=8, loc=2)
plt.xlabel('Height (cm)')
plt.ylabel('Density Values')

plt.show()
