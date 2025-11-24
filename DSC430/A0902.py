#Written by Kira Damo
#I have not given or received any unauthorized assistance on this assignment
#Submitted June 7th
#https://youtu.be/LCMHEO61AC8

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

try:
    hw_df = pd.read_csv('Heights_and_Weights.csv', sep=',')
except FileNotFoundError:
    print('File not found. Please try again')
    exit()

#divided Male and Female heights
female_df = hw_df[hw_df['Sex'] == 'Female']
female_heights = female_df['Height']
female_weights = female_df['Weight']

male_df = hw_df[hw_df['Sex'] == 'Male']
male_heights = male_df['Height']
male_weights = male_df['Weight']

plt.figure(figsize=(10,6))

#y=0.28 x + 23.2, line of best fit with two points
x = [min(hw_df['Height']), max(hw_df['Height'])]
y1 = 0.28 * min(hw_df['Height']) + 23.2
y2 = 0.28 * max(hw_df['Height']) + 23.2
y = [y1, y2]

plt.plot(x,y,'ro-', label='Line of Regression')

#bounds for outliers
weight_upper = hw_df['Weight'].mean() + 2.5 * hw_df['Weight'].std()
weight_lower = hw_df['Weight'].mean() - 2.5 * hw_df['Weight'].std()
height_upper = hw_df['Height'].mean() + 2.5 * hw_df['Height'].std()
height_lower = hw_df['Height'].mean() - 2.5 * hw_df['Height'].std()

plt.axvline(height_upper, color='black', ls='--')
plt.axvline(height_lower, color='black', ls='--')
plt.axhline(weight_upper, color='black', ls='--')
plt.axhline(weight_lower, color='black', ls='--')
    
#height = x, weight = y
plt.scatter(male_heights, male_weights, marker='o', alpha=0.75,
            color='tab:blue', ls='', label='Male Height and Weight')
plt.scatter(female_heights, female_weights, marker='o', alpha=0.75,
            color='tab:pink', ls='', label='Female Height and Weight')

#marking outliers
outliers = hw_df[
    ((hw_df['Height'] < height_lower) | (hw_df['Height'] > height_upper)) &
    ((hw_df['Weight'] < weight_lower) | (hw_df['Weight'] > weight_upper))]
for _, row in outliers.iterrows():
    plt.text(row['Height'], row['Weight'], 'outlier', fontsize=8, color='red')

plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.legend(loc=2)
plt.show()

