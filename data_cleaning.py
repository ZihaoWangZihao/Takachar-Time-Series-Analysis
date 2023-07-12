import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

file_path = "/Users/zihaowang/PycharmProjects/Time-Series-Analysis/Takachar-Time-Series-Analysis/Hot_Test_15/NSTPROR00006-2023-06-22 (1).xlsx"
df = pd.read_excel(file_path)

col_letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
               'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
               'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

fan_cols = ["C", "D", "E", "F", "G", "H"]


def fan_data(columns):
    """
    :param columns: <list> fan columns in letter-based format
    :param file: <str> file_path
    :return: Excel file edited
    """

    for letter in columns:
        col_to_change = df.iloc[:, col_letters[letter]]
        for i, value in enumerate(col_to_change):
            if value[-1] == "R":
                new_value = value.split("-")
                df.iloc[i, col_letters[letter]] = int(new_value[0])  # Set the value in the current cell
            else:
                new_value = 0
                df.iloc[i, col_letters[letter]] = new_value

    df.to_excel(file_path, index=False)

second_file_path = "/Users/zihaowang/PycharmProjects/Time-Series-Analysis/Takachar-Time-Series-Analysis/Hot_Test_15/Feeding Rate 22 nd June 2023.xlsx"
df2 = pd.read_excel(second_file_path)

# Iterate through the rows and columns of the DataFrame
for index, row in df2.iterrows():
    for col in df2.columns:
        cell_value = row[col]
        if cell_value == "Cumulative kg consumed":
            # Print the row, column, and cell coordinates
            target_row = index + 1
            target_col = int(col[-1])
            break
# Specify the column and the starting row
column_index = target_col
starting_row = target_row

# Get all values from the specified column starting from the specified row
values = df2.iloc[starting_row:, column_index].tolist()

# Print the values
print(values)

def time_difference(time1, time2):
    # Define the two time points
    time1 = datetime.strptime('10:30:00', '%H:%M:%S')
    time2 = datetime.strptime('14:45:30', '%H:%M:%S')

    # Calculate the time difference
    time_diff = time2 - time1

    # Format the time difference in HH:MM:SS format
    time_diff_formatted = str(time_diff)

    # Print the formatted time difference
    return time_diff_formatted



# Running Data
# fan_data(fan_cols)