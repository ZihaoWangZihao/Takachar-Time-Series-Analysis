import pandas as pd
import matplotlib.pyplot as plt

file_path = "/Users/zihaowang/PycharmProjects/Time-Series-Analysis/Takachar-Time-Series-Analysis/Day_15_NSTPROR00006-2023-06-22.xlsx"
df = pd.read_excel(file_path)

col_letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
               'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
               'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

fan_cols = ["C", "D", "E", "F", "G", "H"]
temp_cols = ["I", "J", "K", "L", "M",] # What's with column N?

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
                df.iloc[i, col_letters[letter]] = new_value  # Set the value in the current cell
            else:
                new_value = 0
                df.iloc[i, col_letters[letter]] = new_value

    df.to_excel(file_path, index=False)


def plotting_fan(columns):
    """
    :param columns: <list> fan columns that are going to be dependent variable
    :return: single plot of fan speeds with respect to time
    """
    time_col = df.iloc[:, col_letters["B"]]
    plt.figure(figsize=(8, 6))  # new figure with specified size

    for letter in columns:
        y = df.iloc[:, col_letters[letter]]
        plt.plot(time_col, y, label=f'Fan {col_letters[letter]-1}')  # plot each line with a label corresponding to its column letter

    # Set plot title and labels
    plt.title('Fan Speed with respect to Time')
    plt.xlabel('Time')
    plt.ylabel('Fan Speed')

    # Add a legend
    plt.legend()

    plt.show()


def plotting_temp(columns):
    """
    :param columns: <list> fan columns that are going to be dependent variable
    :return: single plot of temperature with respect to time
    """
    time_col = df.iloc[:, col_letters["B"]]
    plt.figure(figsize=(8, 6))  # new figure with specified size

    for letter in columns:
        y = df.iloc[:, col_letters[letter]]
        plt.plot(time_col, y, label=f'Temp {str(col_letters[letter]-7)}')  # plot each line with a label corresponding to its column letter
    # Set plot title and labels
    plt.title('Temperature with respect to Time')
    plt.xlabel('Time')
    plt.ylabel('Temperature')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()


def plotting_weights(input_weight_col, output_weight_col):
    """
    :param input_weight_col: <Excel Column Letter> for Input Weight
    :param output_weight_col: <Excel Column Letter> for Output Weight
    :return: Plot of Weights with respect to Time
    """
    time_col = df.iloc[:, col_letters["B"]]
    plt.figure(figsize=(8, 6))  # new figure with specified size

    y_input = df.iloc[:, col_letters[input_weight_col]]
    y_output = df.iloc[:, col_letters[output_weight_col]]
    plt.plot(time_col, y_input, label=f'Input Weight')  # plot each line with a label corresponding to its column letter
    plt.plot(time_col, y_output, label=f'Output Weight')

    # Set plot title and labels
    plt.title('Input/Output Weight with respect to Time')
    plt.xlabel('Time')
    plt.ylabel('Weight')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()


def plotting_augers(auger_motor, auger_torque, auger_current):
    """
    :param input_weight_col: <Excel Column Letter> for Input Weight
    :param output_weight_col: <Excel Column Letter> for Output Weight
    :return: Plot of Weights with respect to Time
    """
    time_col = df.iloc[:, col_letters["B"]]
    plt.figure(figsize=(8, 6))  # new figure with specified size

    y_motor = df.iloc[:, col_letters[auger_motor]]
    y_torque = df.iloc[:, col_letters[auger_torque]]
    y_current = df.iloc[:, col_letters[auger_current]]
    plt.plot(time_col, y_motor, label=f'Auger Motor')  # plot each line with a label corresponding to its column letter
    plt.plot(time_col, y_torque, label=f'Auger Torque')
    plt.plot(time_col, y_current, label=f'Auger Current')

    # Set plot title and labels
    plt.title('Auger Information with respect to Time')
    plt.xlabel('Time')
    plt.ylabel('Speeds')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()


# fan_data(fan_cols)
plotting_fan(fan_cols)
# plotting_temp(temp_cols)
# plotting_weights("Q", "R")
# plotting_augers("S", "T", "U")

# fig, axs = plt.subplots(2, 2, figsize=(10, 10))  # create a grid of 2 rows and 2 columns
#
# axs[0, 0].add_artist(#Plot)
# axs[0, 1].add_artist(#Plot)
# axs[1, 0].add_artist(#Plot)
# axs[1, 1].add_artist(#Plot)
#
# plt.tight_layout()
# plt.show()



# Pandas Merge with tolerance --> input weight
# Matplotlib inline -->