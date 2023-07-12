import pandas as pd
from datetime import datetime, timedelta


second_file_path = ""
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

# All values under "Cumulative kg consumed" column in a list
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