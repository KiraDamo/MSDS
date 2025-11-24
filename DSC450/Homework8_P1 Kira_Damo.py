#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 8
Due November 9th
Kira Damo
2007841
"""

import pandas as pd

employee_df = pd.read_csv('/Users/kiradamo/Documents/DSC 450/Employee.txt',
                         header = None, names = [
                             'first_name', 'middle_initial', 'last_name',
                             'ssn', 'birth_date', 'address', 'city', 'state',
                             'gender', 'salary', 'supperssn', 'dno'])

#Question 1

male_employees = employee_df[employee_df['gender'] == 'M']
print('All Male Employees: ')
print(male_employees)

female_employees = employee_df[employee_df['gender'] == 'F']
highest_female_salary = female_employees['salary'].max()
print('The highest female salary: ${:,}'.format(highest_female_salary))

salary_groups_mi = employee_df.groupby('middle_initial')['salary'].agg(list)
print(salary_groups_mi)

