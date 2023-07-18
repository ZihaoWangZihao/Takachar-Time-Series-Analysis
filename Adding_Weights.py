import pandas as pd
from datetime import datetime, timedelta

import pandas as pd
from datetime import datetime, timedelta

############################################## Cumulative kg Consumed ################################################

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

# All values under "Cumulative kg consumed" column in a list
kg_values = df2.iloc[starting_row:, column_index].tolist()

#########################################################################################################

###################################################### Return Time Feed ##################################################
# Read the Excel file into a DataFrame
df = pd.read_excel('/Users/zihaowang/PycharmProjects/Time-Series-Analysis/Takachar-Time-Series-Analysis/Hot_Test_15/Feeding Rate 22 nd June 2023.xlsx')

# Find the column index for the "Timestamp" header
for index, row in df.iterrows():
    for col_index, col in enumerate(df.columns):
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
values = df.iloc[starting_row:, column_index].tolist()
time_feed = []

for i in values:
    try:
        formatted_time = i.strftime("%H:%M")
        time_feed.append(formatted_time)
    except:
        continue

#return time_feed
print(time_feed)

# Create a dictionary with time as keys and kg as values
data_dict = dict(zip(time_feed, kg_values))

#############################################################################################################################

################################################ Return Time N #################################################################

import pandas as pd
from datetime import datetime

# Read the Excel file into a DataFrame
df = pd.read_excel('/Users/zihaowang/PycharmProjects/Time-Series-Analysis/Takachar-Time-Series-Analysis/Hot_Test_15/NSTPROR00006-2023-06-22 (1).xlsx')

# Specify the column name containing the timestamp data
timestamp_column = 'Time'

# Extract the timestamp data column
timestamp_data = df[timestamp_column].tolist()

# Print the timestamp data
time_N = []
for timestamp in timestamp_data:
    datetime_obj = datetime.strptime(timestamp, '%I:%M:%S %p')
    time_str = datetime_obj.strftime('%H:%M:%S')
    time_N.append(time_str)

############################################### Time Difference ###############################################################

import pandas as pd
from datetime import datetime

    # Define the two time points
    #time1 = datetime.strptime('10:30:00', '%H:%M:%S')
   # time2 = datetime.strptime('14:45:30', '%H:%M:%S')

df = pd.read_excel('/Users/zihaowang/PycharmProjects/Time-Series-Analysis/Takachar-Time-Series-Analysis/Hot_Test_15/NSTPROR00006-2023-06-22 (1).xlsx')

# Find the time difference for each pair of times
time_feed_new = [datetime.strptime(time, "%H:%M").strftime("%H:%M:%S") for time in time_feed]

time_feed_dt = [datetime.strptime(time, "%H:%M:%S") for time in time_feed_new]
time_N_dt = [datetime.strptime(time, "%H:%M:%S") for time in time_N]

for i, N_time in enumerate(time_N_dt):
    smallest_diff = None
    smallest_diff_index_feed = None

    # Iterate over each time_feed element
    for j, feed_time in enumerate(time_feed_dt):
        # Calculate time difference
        diff = abs(N_time - feed_time)

        # Update smallest difference and index if it is the smallest encountered so far
        if smallest_diff is None or diff < smallest_diff:
            smallest_diff = diff
            smallest_diff_index_feed = j

    # Get the corresponding time_feed and combustion kg based on the smallest time difference
    closest_feed_time = time_feed[smallest_diff_index_feed]
    cumulative_kg = data_dict[closest_feed_time]

    # Update the corresponding row in the DataFrame with the combustion kg value
    df.at[i, 'Cumulative kg'] = cumulative_kg

# Save the updated DataFrame to a new Excel file
df.to_excel('/Users/zihaowang/PycharmProjects/Time-Series-Analysis/Takachar-Time-Series-Analysis/Hot_Test_15/NSTPROR00006-2023-06-22 (1).xlsx', index=False)

###############################################################################################################################





