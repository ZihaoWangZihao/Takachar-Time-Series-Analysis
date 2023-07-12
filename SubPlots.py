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

# Data
x = df.iloc[:, col_letters["B"]] # Time
auger_motor = "S"
auger_torque = "T"
auger_current = "U"
auger_power = "P"
y_motor = df.iloc[:, col_letters[auger_motor]]
y_torque = df.iloc[:, col_letters[auger_torque]]
y_current = df.iloc[:, col_letters[auger_current]]
y_power = df.iloc[:, col_letters[auger_power]]
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
# ax3.plot(x, y_motor, label=f"Auger Motor")
# ax3.plot(x, y_power, label=f"Auger Power")
# ax3.plot(x, y_current, label=f"Auger Current")
# ax3.plot(x, y_torque, label=f"Auger Torque")
# ax3.set_title('Auger Plots')
# ax3.set_xlabel('Time')
# ax3.set_ylabel('Temperature')
# ax3.legend()

# Plot the first dataset on the primary y-axis
ax3.plot(x, y_motor, label="Auger Motor", color='tab:blue')
ax3.plot(x, y_power, label="Auger Power", color='tab:orange')
ax3.set_xlabel('Time')
ax3.set_ylabel('Label 1')
ax3.tick_params(axis='y')

# Create a twin axis sharing the x-axis
ax4 = ax3.twinx()

# Plot the second dataset on the secondary y-axis
ax4.plot(x, y_current, label="Auger Current", color='tab:red')
ax4.plot(x, y_torque, label="Auger Torque", color='tab:green')
ax4.set_ylabel('Label 2')
ax4.tick_params(axis='y')

# Combine the legends of both axes
lines1, labels1 = ax3.get_legend_handles_labels()
lines2, labels2 = ax4.get_legend_handles_labels()
lines = lines1 + lines2
labels = labels1 + labels2
ax3.legend(lines, labels)


# Adjust the spacing between subplots
fig.tight_layout()

# Display the figure
plt.show()


# # Add the fourth subplot
# ax4 = fig.add_subplot(2, 2, 4)
# ax4.plot(x, y2, label='Cos(x)')
# ax4.plot(x, y4, label='Sqrt(x)')
# ax4.set_title('Plot 4')
# ax4.legend()

