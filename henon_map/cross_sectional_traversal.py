# Initiate Coordinates
x = 0
y = -0.2

a = -1.4

# List of Accumulated Values During Iterations
x_list = [x]
y_list = [y]

def iterateAndAccumulate(x, y):
    iterationsComplete = 0
    while iterationsComplete < 270000:
        
        x_next = 1 + a*(x**2) + y

        y_next = 0.3*x
        
        x_list.append(x_next)
        y_list.append(y_next)
        
        iterationsComplete += 1
        
        # Let's update the values of x and y for the next iteration
        x = x_next
        y = y_next

import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure

# Check if work to be resumed from last time or start afresh
# resume = True if something was written in Resume.txt. Else the computer
# didn't need to save anything in Resume.txt therefore never encountered the error.
with open('Resume.txt', 'r') as file_object:
	content = file_object.read()
	if content == '':
		resume = False
	else:
		# Check why not empty with print('aha'+ content +'aha')
		resume = True


if resume == True:
	# Go fetch data from last time
	with open('Resume.txt', 'r') as file_object:
		lines = file_object.readlines()
		a = float(lines[0]) # Access the first line and store as 'a'
		imageNumber = int(lines[1]) # Access the second line and store as 'imageNumber'
else:
	# 'a' is what varies therefore placed outside the loop so you don't redefine it everytime
	a =  -1.4
	imageNumber = 1

# Loop until all images produced
#while imageNumber < 10:
while a < 0:
    
    # Initiate Coordinates
    x = 0
    y = -0.2

    # List of Accumulated Values During Iterations
    x_list = [x]
    y_list = [y]
    
    # Loop until all values calculated
    iterateAndAccumulate(x, y)
    
    # Set resolution (16x9 inches at 480 dpi gives 7680x4320, 8K)
    figure(figsize=(16, 9), dpi=480)
    
    # Produce the image
    plt.plot(x_list, y_list, '.', markersize=0.3)

    # Adding title, xlabel and ylabel
    plt.title('A Basic Line Plot, a = '+ '{:.3f}'.format(round(a, 3))) # Title of the plot
    plt.xlabel('x-axis') # X-Label
    plt.ylabel('y-axis') # Y-Label
    
    # Prevent automatic setting of axis ranges, which vary imagewise
    plt.xlim([-1.5, 1.5])
    plt.ylim([-0.4, 0.4])
    
    # Save the image
    try:
    	plt.savefig("Henon\Henon"+ str(imageNumber) +".jpg")
    except MemoryError:
    	with open('Resume.txt', 'w') as file_object:
    		file_object.write(str(a) + '\n') # Write value of 'a' on 1st line
    		file_object.write(str(imageNumber) + '\n') # Write value of 'imageNumber' on 2nd line
    	break

    # Clear the canvas else the next iteration will print on the previous [plt.clf()]
    # Close the figure because consumes too much memory it says
    plt.close()
    
    # Confirm and next image
    print('Image no.' + str(imageNumber) + ' OK!')
    imageNumber += 1    
    # Increment 'a'
    a += 0.002