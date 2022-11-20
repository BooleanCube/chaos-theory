# Time taken 1.53 hours a += 0.1 / 33 images / 132 MB
# Time taken 15.5 hours a += 0.01 / 331 images / 742 MB with 8.58 billion points in total!!

# Each 3D Cube had 5 different parametres we had to vary to achieve good aesthetics
# These parametres have varied from the 3D Hénon to the 4D Hénon
# - Points per Section (6500)
# - Point Alpha (0.24)
# Those 2 above work together; more points per section implies less alpha,
# but abusing the numbers indroduces posterisation
# - Resolution (100, 100)
# - Increment between Sections (0.0005)
# Again those two just above require careful balance; and higher resolutions
# help give more transparency to the points in the images.
# - Point Size (quite differenceless beyond certain smallness) (0.01)

# You are allowed to define a function in Python with the variables not even defined.
# Provided that Python later knows about all the variables in question at the moment of function call.
# This is because Python only compiles not executes the defined function. Unless you call the function.

def iterateAndAccumulate(x, y):
    iterationsComplete = 0
    # In Python all variables defined/changed inside a function are lost/reverted
    # after the function's execution. We say these variables are ‘local’.
    # A variable defined at the beginning of a program outside a function
    # remains valid for the entire program. We call it a ‘global’ variable.
    # You are not allowed to change a global variable from within a function.
    # Except if you define the two following variables' use as global:
    global divergesToInfinity, divergencesToInfinity
    while iterationsComplete < 6500 and divergesToInfinity == False:

        try:    
            x_next = 1 + a*(x**2) + y
            y_next = z*x

            # We just said you can't change a variable that was defined outside function
            # You can't change it from within a function. But it seems ‘.append()’
            # works all fine ¯\_(ツ)_/¯
            x_list.append(x_next)
            y_list.append(y_next)

            iterationsComplete += 1
        
            # Let's update the values of x and y for the next iteration
            x = x_next
            y = y_next

        # If the plot in question diverges to infinity
        except OverflowError:
            divergesToInfinity = True
            divergencesToInfinity += 1
            # print("Diverged at z = " + '{:.2f}'.format(round(z, 2)))
            pass

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import matplotlib.axes

# Measure the time taken for the render
import time
start = time.time()

# 'a' beyond -2.30 and 0.90 all sections diverge to infinity
# If you change these values, change also those down below!
a_startvalue = -2.30
a_endvalue   =  1.00
a_increment  =  0.01

# Check if work to be resumed from last time or start afresh
# resume = True if something was written in Resume.txt. Else the computer
# didn't need to save anything in Resume.txt remains an empty file.
with open('Resume.txt', 'r') as file_object:
    content = file_object.read()
    if content == '':
        #  resume = False
        a = a_startvalue # Default initial start value
    else:
        # Check why not empty with print('aha'+ content +'aha')
        resume = True


imageNumber = 1
while a < 1.00:

    fig = plt.figure()
    fig.set_size_inches(100, 100) # (50, 50) gives 5000x5000px, hence (76.8, 43.2) is 8K
    ax = fig.add_subplot(111, projection='3d')
    plt.xlim([-2.0, 2.0])
    plt.ylim([-1.0, 1.0])
    ax.set_zlim3d(-1.5, 0.5)

    # Enable or Disable markings on your axes
    # Those are a list of numbers, left empty to disable axis markings
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    divergencesToInfinity = 0
    convergences = 0

    # Create a cube on each rundown
    # Start with a low value of z. Keep plotting sections without clearing until z reaches high value
    z = -1.5000
    startCube = time.time()
    while z < 0.5000:

        # Only defining these 5 values here and not inside the function because
        # all non-returned values are lost after a function call.
        # Initial x and y, for each rundown
        x = 0
        y = -0.2

        x_list = [x]
        y_list = [y]
        z_list = []

        # By default, we assume a map does not diverge to infinity
        divergesToInfinity = False

        iterateAndAccumulate(x, y)
        
        if divergesToInfinity == False:
            # print("Converged at z = " + '{:.2f}'.format(round(z, 2)))
            convergences += 1

            while len(z_list) < len(x_list):
                z_list.append(z)

            # Although colour '#146CA8' is the Matplotlib blue
            ax.scatter3D(x_list, y_list, z_list, c='#146cA8', marker='.', s=0.01, alpha=0.24);
            # Now you don't clear (aka. simply say nothing it won't clear)
            # and calculate the next set and plot without clearing previous plots
        
        z += 0.0005

    plt.savefig("Henon\Henon"+ str(imageNumber) +".png")
    stopCube = time.time()

    print("Cube at a = "+ '{:.2f}'.format(round(a, 2)) +" finished in " +\
    str(round(((stopCube-startCube)/60), 2)) + " minutes. Progress: " +\
    str(imageNumber) + "/" + str((a_endvalue - a_startvalue)/a_increment) + ".   ", end='\r')

    with open('Render Log.txt', 'a') as file_object:
        file_object.write("Cube at a = "+ '{:.2f}'.format(round(a, 2)) +" finished in " +\
        str(round(((stopCube-startCube)/60), 2)) + " minutes with " +\
        str(divergencesToInfinity) + " divergences and " + str(convergences) + " convergences.\n")

    # Clear your cube for the next increment of 'a'
    # Normally I'd have here used ‘plt.cla()’—clearing each cube after each save.
    # This would consume less time than closing the Matplotlib, then re-opening it
    # for next cube. But just clearing the cube produces errors, as a vertical line
    # of dots on each frame from the 3rd. So we have no choice.
    plt.close()
    
    a += 0.01
    imageNumber += 1

    with open('Resume.txt', 'a') as file_object:
        file_object.write(value of a)


end = time.time()
print("It took "+ str(round(((end-start)/3600), 2)) +" hours." + ' '*40)
with open('Render Log.txt', 'a') as file_object:
        file_object.write("It took "+ str(round(((end-start)/3600), 2)) +" hours.")