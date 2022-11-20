import numpy as np
import statistics


def calculate_eqpoint():
    eqpoints = set()
    for j in range(steps - 1, steps - 51, -1):
        v = round(y[j], 3)
        eqpoints.add(v)
    return eqpoints


def calculate_eqpoints(ys):
    ys = ys[-100:-1]
    sy = set(ys)

    freq = {}
    for y in sy:
        freq[y] = ys.count(y)

    mode = statistics.mode(ys)
    modefreq = freq[mode]
    maxdiff = 1

    eqpoints = set()
    for y in sy:
        if freq[y] >= modefreq-maxdiff:
            eqpoints.add(y)

    return eqpoints


r = 2.99999  # rate of change has to be a value in the interval [0, 4] ( I put it at 2.9999 for the sake of runtime )
y_0 = 0.5  # y_initial has to be a value in the interval [0, 1]
steps = 5000  # the number of steps shown (x-axis range for time)
skip = 0.00001

allrates = []
ratecount = {}

while r < 4.0:
    # x represents time (x)
    # y represents population (y_x)
    x = [0]*(steps+1)
    y = [0]*(steps+1)
    x[0], y[0] = 0, y_0

    # Draw the equilibrium graph with the time to population relationship.
    for i in range(steps):
        y[i + 1] = r * y[i] * (1 - y[i])
        x[i + 1] = x[i] + 1

    # Iterate through the graph starting from the end (time = 1000) and add all the population percentages
    # into a set of equilibrium points. Maximum of 50 equilibrium points can be set for each rate of change.
    eqpoints = calculate_eqpoints([round(i, 4) for i in y])

    # Adding equilibrium points counts to the lists
    allrates.append(r)
    ratecount[r] = len(eqpoints)

    r += skip
    r = round(r, 5)

period = 1
n = 1
biparam = [0]  # 0 is a dummy node, it will never be reached
print("n | Period | Bifurcation Parameter | Ratio")
for i in allrates:
    # I had to do this because my calculations are not perfectly precise
    if i < 3:
        continue
    # I had to do this because of precision errors in calculations
    if period == 32:
        break

    if ratecount[i] >= period*2:
        biparam.append(i)
        period *= 2
        if n < 3:
            print(str(n) + " | " + str(period) + " "*(6-len(str(period))) + " | " + str(i))
        else:
            ratio = round((biparam[n-1]-biparam[n-2])/(biparam[n]-biparam[n-1]), 3)
            print(str(n) + " | " + str(period) + " "*(6-len(str(period))) + " | " + str(i) + " "*(21-len(str(i))) +
                  " | " + str(ratio))
        n += 1
