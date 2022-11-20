# Initiate Coordinates
x = 0
y = -0.2

# Initial Values
a = -1.4
b = 0.3

# List of Accumulated Values During Iterations
x_list = [x]
y_list = [y]

imageNumber = 1

def iterateAndAccumulate(x, y):
    iterationsToComplete = imageNumber - 1
    iterationsCompleted = 0
    while iterationsCompleted < iterationsToComplete:
        
        x_next = 1 + a*(x**2) + y

        y_next = b*x 
        
        x_list.append(x_next)
        y_list.append(y_next)
        
        iterationsCompleted += 1
        
        # Let's update the values of x and y for the next iteration
        x = x_next
        y = y_next

import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure

# Set resolution (16x9 inches at 480 dpi gives 7680x4320, 8K. 120 dpi for 1080p)
figure(figsize=(16, 9), dpi=120)
plt.xlabel('x-axis') # X-Label
plt.ylabel('y-axis') # Y-Label
# Prevent automatic setting of axis ranges, which vary imagewise
plt.xlim([-1.5, 1.5])
plt.ylim([-0.42, 0.42])

imageNumber = 1

# Loop until all images produced
while imageNumber < 10000:
    
    # Initiate Coordinates
    x = 0
    y = -0.2

    # List of Accumulated Values During Iterations
    x_list = [x]
    y_list = [y]
    
    # Loop until all values calculated
    iterateAndAccumulate(x, y)
    
    # Produce the image
    plt.plot(x_list, y_list, '.', markersize=2, color='#146cA8')

    # Adding title, xlabel and ylabel
    plt.title('Number of Points Plotted = '+ str(imageNumber)) # Title of the plot
    
    # Prevent automatic setting of axis ranges, which vary imagewise
    plt.xlim([-1.5, 1.5])
    plt.ylim([-0.42, 0.42])
    
    # Save the image
    plt.savefig("Henon\Henon"+ str(imageNumber) +".png")
    
    # Confirm and next image
    print('Image no.' + str(imageNumber) + ' OK!')
    imageNumber += 1