import matplotlib.pyplot as plt

input_values = [i for i in range(5000)]
output_values = [i**2 for i in range(5000)]

plt.scatter(input_values, output_values, cmap=plt.cm.Blues)
plt.title('Cube')
plt.xlabel('Value')
plt.ylabel('Cube of the Value')
plt.show()