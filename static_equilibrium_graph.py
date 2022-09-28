from matplotlib import pyplot as plt
import numpy as np

plt.style.use('dark_background')

#     STATIC VARIABLES    ( with the default values, there
#     should be no fluctuation in the logistic map and
#     the equilibrium should be equal to 0.5 )
# ----------------------------------------------------------
r = 2.0  # rate of change has to be a value in the interval [0, 4]
x_0 = 0.5  # x_initial has to be a value in the interval [0, 1]
steps = 300  # the number of steps shown (x-axis range for time)

print("Declare Variables (hit enter for default values):")
inp = input("Rate of Change (default=2.0): ")
if inp != "":
	r = float(inp)
inp = input("X_Initial (default=0.5): ")
if inp != "":
	x_0 = float(inp)
inp = input("Steps (default=30): ")
if inp != "":
	steps = int(inp)

# x represents time (n)
# y represents population (x_n)
x = np.zeros(steps + 1)
y = np.zeros(steps + 1)
x[0], y[0] = 0, x_0

# Draw the equilibrium graph with the time to population relationship.
for i in range(steps):
	y[i+1] = r * y[i] * (1 - y[i])
	x[i+1] = x[i] + 1

fig, ax = plt.subplots()
ax.plot(x, y, alpha=0.5)

# Plot all the points on the grid for all steps
#  Only plot points if the x-axis range is less than or equal to 20
#  for visibility purposes
if steps <= 30:
	for i in range(steps):
		ax.plot(x, y, 'bo')

ax.set(xlabel='Time (years)', ylabel='Population (fraction of max)')
plt.title("Equilibrium Graph\nx_(n+1) = r(x_n)(1-x_n)")
plt.ylim([0, 1])

#  x_(n+1) over x_n graph
m = {}
x2 = np.zeros(steps)
y2 = np.zeros(steps)
for i in range(steps):
	# print(y[i], y[i+1])
	x2[i] = y[i]
	m[x2[i]] = y[i+1]

x2.sort()
idx = 0
for i in x2:
	y2[idx] = m[i]
	idx += 1

fig2, ax2 = plt.subplots()
ax2.plot(x2, y2, alpha=0.5)
ax2.set(xlabel="x_n", ylabel="x_(n+1)")
plt.title("Graph of x_(n+1) vs x_n")
plt.show()
