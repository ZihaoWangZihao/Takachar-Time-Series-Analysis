import matplotlib.pyplot as plt
import pandas as pd


file_path = "/Users/zihaowang/PycharmProjects/Time-Series-Analysis/Takachar-Time-Series-Analysis/Hot_Test_15/NSTPROR00006-2023-06-22 (1).xlsx"
df = pd.read_excel(file_path)

col_letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
               'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
               'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

# Columns in Excel
fan_cols = ["C", "D", "E", "F", "G", "H"]
temp_cols = ["I", "J", "K", "L", "M",]
output_weight_col = "R"
input_weight_col = "V"
auger_motor = "S"
auger_torque = "T"
auger_current = "U"
auger_power = "P"


# Data
x = df.iloc[:, col_letters["B"]]  # Time
y_motor = df.iloc[:, col_letters[auger_motor]]
y_torque = df.iloc[:, col_letters[auger_torque]]
y_current = df.iloc[:, col_letters[auger_current]]
y_power = df.iloc[:, col_letters[auger_power]]
y_input = df.iloc[:, col_letters[input_weight_col]]
y_output = df.iloc[:, col_letters[output_weight_col]]
fan_data = []
temp_data = []
for col in fan_cols:
    fan_data.append(df.iloc[:, col_letters[col]])

for col in temp_cols:
    temp_data.append(df.iloc[:, col_letters[col]])

#####################################################################

fig = plt.figure(figsize=(10, 8))

# Plotting Fans
ax1 = fig.add_subplot(2, 2, 1)
for i in range(len(fan_data)):
    ax1.plot(x, fan_data[i], label=f'Fan {i+1}')
ax1.set_title('Fan Plots')
ax1.set_xlabel('Time')
ax1.set_ylabel('Fan Speed')
ax1.legend()

# Plotting Temperature
ax2 = fig.add_subplot(2, 2, 2)
for i in range(len(temp_data)):
    ax2.plot(x, temp_data[i], label=f'Temperature {i+1}')
ax2.set_title('Temperature Plots')
ax2.set_xlabel('Time')
ax2.set_ylabel('Temperature')
ax2.legend()

# # Plotting Auger
ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(x, y_motor, label="Auger Motor", color='tab:blue')
ax3.plot(x, y_power, label="Auger Power", color='tab:orange')
ax3.set_xlabel('Time')
ax3.set_ylabel('Label 1')
ax3.tick_params(axis='y')

ax4 = ax3.twinx() # Create a twin axis sharing the x-axis

ax4.plot(x, y_current, label="Auger Current", color='tab:red')
ax4.plot(x, y_torque, label="Auger Torque", color='tab:green')
ax4.set_ylabel('Label 2')
ax4.tick_params(axis='y')

lines1, labels1 = ax3.get_legend_handles_labels()
lines2, labels2 = ax4.get_legend_handles_labels()
lines = lines1 + lines2
labels = labels1 + labels2
ax3.legend(lines, labels)

# Plotting Weights
ax5 = fig.add_subplot(2, 2, 4)
ax5.plot(x, y_output, label="Output Weight", color='tab:green')
ax5.plot(x, y_input, label="Input Current", color='tab:red')
ax5.set_title('Output/Input Weight Plots')
ax5.set_xlabel('Time')
ax5.set_ylabel('Weight')
ax5.legend()

# Adjust the spacing between subplots
fig.tight_layout()

# Display the figure
plt.show()

