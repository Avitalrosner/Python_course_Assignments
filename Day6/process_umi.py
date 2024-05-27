#Defining functions for loading the data and calculating the log10 for the sum of UMI's:

import pandas as pd
import numpy as np

def load_data(file_path):
    return pd.read_csv(file_path)

def calculate_log10(data, column_name):
    data['log10_' + column_name] = np.log10(data[column_name])
    return data

if __name__ == "__main__":
    file_path = "C:/python/Python_course_Assignments/Day6/umi.csv"
    data = load_data(file_path)
    data = calculate_log10(data, 'sum_of_umis')
    print(data)

