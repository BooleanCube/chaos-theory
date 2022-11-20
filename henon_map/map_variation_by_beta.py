# Time taken 31.30 minutes

# Initiate Coordinates
x = 0
y = -0.2

# Original Values
# a = -1.4
# b = 0.3
# Custom Values
a = -1.176
b = 0.3

# List of Accumulated Values During Iterations
x_list = [x]
y_list = [y]

def iterateAndAccumulate(x, y):
    iterationsComplete = 0
    while iterationsComplete < 150000:
        
        x_next = 1 + a*(x**2) + y

        y_next = b*x 
        
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
	b =  -0.8
	imageNumber = 1

# Measure the time taken for the render
import time
start = time.time()
# Loop until all images produced
#while imageNumber < 10:
while b < 0.441:
    
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
    plt.title('A Basic Line Plot, b = '+ '{:.3f}'.format(round(b, 3))) # Title of the plot
    plt.xlabel('x-axis') # X-Label
    plt.ylabel('y-axis') # Y-Label
    
    # Prevent automatic setting of axis ranges, which vary imagewise
    plt.xlim([-3.0, 3.0])
    plt.ylim([-0.7, 0.7])
    
    # Save the image
    try:
    	plt.savefig("Henon\Henon"+ str(imageNumber) +".jpg")
    except MemoryError:
    	with open('Resume.txt', 'w') as file_object:
    		file_object.write(str(b) + '\n') # Write value of 'a' on 1st line
    		file_object.write(str(imageNumber) + '\n') # Write value of 'imageNumber' on 2nd line
    	break

    # Clear the canvas else the next iteration will print on the previous [plt.clf()]
    # Close the figure because consumes too much memory it says
    plt.close()
    
    # Confirm and next image
    print('Image no.' + str(imageNumber) + ' OK!')
    imageNumber += 1    
    # Increment 'a'
    b += 0.001 # 0.002

end = time.time()

print("It took "+ str(round((end-start), 2)/60) +" minutes.")