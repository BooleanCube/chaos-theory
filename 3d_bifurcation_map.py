# Time taken 8.8 minutes

# Only defining x, y, z, x_list, y_list to be able to define function iterateAndAccumulate()
# Not because we want them to be these values
# In this program 'z' acts as 'b' in the iterative equations
x = 0
y = -0.2
z = 0

x_list = [x]
y_list = [y]

def iterateAndAccumulate(x, y):
    iterationsComplete = 0
    # if-logic explained below
    if '{:.4f}'.format(round(z, 4)) == '0.4025':
        iterations = 600000
    else:
        iterations = 20000
    while iterationsComplete < iterations:
        
        # Within this Cube we want to plot 'a' that always stays constant at -1.176
        x_next = 1 + -1.176*(x**2) + y

        y_next = z*x
        
        x_list.append(x_next)
        y_list.append(y_next)
        
        iterationsComplete += 1
        
        # Let's update the values of x and y for the next iteration
        x = x_next
        y = y_next

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import matplotlib.axes

fig = plt.figure()
fig.set_size_inches(70, 70) # (50, 50) gives 5000x5000px, hence (76.8, 43.2) is 8K
ax = plt.axes(projection='3d')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([-1.5, 1.5])

# Measure the time taken for the render
import time
start = time.time()

z = -0.6000
# A rundown until z is updated (a.k.a each z is a section in the cube)
while z < 0.4025:

    # Only defining these 5 values here and not inside the function because
    # all non-returned values are lost after a function call.
    # Initial x and y, for each rundown
    x = 0
    y = -0.2

    x_list = [x]
    y_list = [y]
    z_list = []

    iterateAndAccumulate(x, y)
    
    while len(z_list) < len(x_list):
        z_list.append(z)

    # Plot the topmost section distinctly
    if '{:.4f}'.format(round(z, 4)) == '0.4025':
        print("Match!")
        ax.scatter3D(x_list, y_list, z_list, c='#284b63', marker='.', s=1.1);
    else:
        # Although colour '#146CA8' is the Matplotlib blue
        ax.scatter3D(x_list, y_list, z_list, c='#146cA8', marker='.', s=0.01, alpha=0.24);
    # Now you don't clear (aka. simply say nothing it won't clear)
    # and calculate the next set and plot without clearing previous plots

    print("Cross-section at "+ '{:.4f}'.format(round(z, 4)) +" OK!")
    z += 0.0005

plt.savefig('Henon\Henon.png')
end = time.time()
print("It took "+ str(round(((end-start)/60), 1)) +" minutes.")