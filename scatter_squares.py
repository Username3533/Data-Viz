import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_valyes = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_valyes, s=10, c=y_valyes, cmap=plt.cm.Blues)

#set chart title and labels
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.ticklabel_format(style='plain')
ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 1100, 0, 1100000])


plt.show()