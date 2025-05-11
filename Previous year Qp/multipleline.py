from matplotlib import pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Plotting the lines
plt.plot(x, y1, label='Line 1', color='blue', linestyle='--')
plt.plot(x, y2, label='Line 2', color='green', linestyle='-.')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple Lines on One Plot')

# Adding legend
plt.legend(loc='upper left')

# Show the plot
plt.show()
