import pandas as pd
from datetime import datetime, timedelta


second_file_path = "/Users/zihaowang/PycharmProjects/Time-Series-Analysis/Takachar-Time-Series-Analysis/Hot_Test_15/Feeding Rate 22 nd June 2023.xlsx"
df2 = pd.read_excel(second_file_path)

# Iterate through the rows and columns of the DataFrame
# for index, row in df2.iterrows():
#     for col in df2.columns:
#         print(col)
#         cell_value = row[col]
#         if cell_value == "Timestamp (hh:mm format)":
#             # Print the row, column, and cell coordinates
#             target_row = index + 1
#             target_col = int(col[-1])
#             break


########################################################################################################################
# Iterate through the rows and column indices of the DataFrame
for index, row in df2.iterrows():
    for col_index, col in enumerate(df2.columns):
        cell_value = row[col_index]
        if cell_value == "Timestamp (hh:mm format)":
            # Print the row, column, and cell coordinates
            target_row = index + 1
            target_col = col_index
            break

# Specify the column and the starting row
column_index = target_col
starting_row = target_row

# All values under "Cumulative kg consumed" column in a list
values = df2.iloc[starting_row:, column_index].tolist()
new_times = []

for i in values:
    try:
        formatted_time = i.strftime("%H:%M")
        new_times.append(formatted_time)
    except:
        continue

print(new_times)

###############################################################################################################################


#
# def time_difference(time1, time2):
#     # Define the two time points
#     time1 = datetime.strptime('10:30:00', '%H:%M:%S')
#     time2 = datetime.strptime('14:45:30', '%H:%M:%S')
#
#     # Calculate the time difference
#     time_diff = time2 - time1
#
#     # Format the time difference in HH:MM:SS format
#     time_diff_formatted = str(time_diff)
#
#     # Print the formatted time difference
#     return time_diff_formatted