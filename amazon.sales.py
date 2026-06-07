#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 16:49:42 2026
-How many sales have they made with amount more than 1000
-how many sales have they made that belong to the Category "Tops" and have a Quantity of
-The Total Sales by Category 
-Average Amount by Category and Status
-Total Sales by Fulfilment and Shipment Type
@author: autymncannon
"""
import pandas as pd
import numpy as np
#loading data into pandas DataFrame
sales_data = pd.read_excel('/Users/autymncannon/Desktop/Amazon Sales Project/sales_data.xlsx')

sales_data.info() #can also check data types here

sales_data.describe()

#looking at columns 
print(sales_data.columns)

#look at first rows
print(sales_data.head())

#check data types of the columns
print(sales_data.dtypes)


#=====================
#cleaning the data
#===================

#missing values in our sales data
sales_data.isnull()
print(sales_data.isnull().sum())

sales_data_dropped = sales_data.dropna()

#drop rows with missing amounts based on the amount column 
sales_data_cleaned = sales_data.dropna(subset = ['Amount'])

print(sales_data_cleaned)


#drop rows with missing amounts based on the amount column 
sales_data_cleaned = sales_data.dropna(subset = ['Amount'])

print(sales_data_cleaned.isnull().sum())
# =============================================================================
# slicing and filtering data
# =============================================================================
category_data = sales_data[sales_data['Category']== 'Top']
print(category_data)

#select a subset of data where amount is > 1000
high_amount_data = sales_data[sales_data['Amount'] > 1000]
print(high_amount_data)

#select a subset of data based on multiple conditions
filtered_data = sales_data[(sales_data["Category"] == 'Top') & (sales_data['Qty'] == 3)]


# =============================================================================
# # Aggregating data 
# =============================================================================

#total sales by category 
category_totals = sales_data.groupby('Category')['Amount'].sum()
category_totals = sales_data.groupby('Category', as_index=False)['Amount'].sum()
category_totals = category_totals.sort_values('Amount', ascending=False)

#calculte the avergae amount by category and fulfilment
fulfilment_averages = sales_data.groupby(
    ['Category', 'Fulfilment'], as_index=False
)['Amount'].mean()
fulfilment_averages = fulfilment_averages.sort_values('Amount', ascending=False)

#calculating the av amnt by category and status
status_averages = sales_data.groupby(['Category', 'Status'], as_index=False)['Amount'].mean()
status_averages = status_averages.sort_values('Amount', ascending=False)


#total sales by shippment and fulfilment
total_sales_shipandfufil = sales_data.groupby(['Courier Status', 'Fulfilment'], as_index=False)['Amount'].sum()
total_sales_shipandfufil = total_sales_shipandfufil.sort_values('Amount', ascending=False)


total_sales_shipandfufil.rename(columns={'Courier Status': 'Shippment'}, inplace = True)
# =============================================================================
# Exporting the data
# =============================================================================

status_averages.to_excel('average_sales_by_category_and_staus.xlsx', index=False)
total_sales_shipandfufil.to_excel('total_sales_by_ship_and_fulfil.xlsx', index=False)






