# chaos-theory

> Playing around with chaos theory simulations. Creating equilibrium graphs and visualizing the logistic maps.

## Chaos Theory
Here, I played around with a simple logistic map equation: `x_(n+1) = r * (x_n) * (1-x_n)` <br>
In this case, I would like to take the example of a population percentage over time (years) graph to explain the logistic map.
- x_(n+1) represents population percentage next year (a value in the interval [0,1])
- x_n represents the population percentage this year (a value in the interval [0,1])
- r represents the fertility rate (a value in the interval [0,4])

The very simple equation has extremely complex behaviour that becomes very chaotic (hard to predict) at high rate (r) values. <br>
These types of logistic maps are often used to be able to predict population percentage or visualize repetitive chaos until the repeating window is so large that it is considered to be arbitrary.
When you graph out the logistic map for population percentage over time, we see that for each rate of change value (r) there is a set equilibrium value regardless of initial population percentage (x_0) which is where all randomness and chaos ceases and settles in at a particular point. So, let's explore how the equilibrium point is related to the rate of change (fertility rate) values.<br>

- When the rate of change (fertility rate) is too low, for example less than 1.00, the equilibrium point will be 0.00 which means the species has gone extinct. <br>
![image](https://user-images.githubusercontent.com/47650058/192679432-e0909c11-4296-42e4-adfd-7a4b90e8a778.png)
- When the rate of change (fertility rate) is decently large, for example less than 3.00, the equilibrium point will be at a set value above 0.00 so the population settles in at a percentage, the equilibrium point, without going extinct. This phenomenon is common in nature, as we usually see the populations start to stabilize over time as long as there are no external events causing the population percentage to falter. In this example we can see the equilibrium point to be ~0.65.
![image](https://user-images.githubusercontent.com/47650058/192680494-2e60daf4-823d-489e-990d-7d26d9e77556.png)
- So far, the logistic map seems reasonable and appropriate. However, this is where the chaos begins. When the rate of change (fertility rate) is too high, for example greater than or equal to 3.00, we start to see more than 1 equilibrium point and more arbitrary results. As the fertility rate (rate of change) increases, the chaos (randomness) also grows exponentially and splits into more equilibrium points exponentially. When the equilibrium point splits into multiple points again, we call it a bifercation. At `r=3.6` we start to see fractal-like behaviour in the logistic map because of the amount of bifercations. This phenomenon is also fairly common in nature, as some populations could oscillate between different percentage values over a window of time repeatedly. In this example, we can see there are 4 equilbirium points, so there must have been 3 periodically doubling bifercations in the logistic map (First splits into 2, and then the 2 split into 4). <br>
![image](https://user-images.githubusercontent.com/47650058/192681721-14e85352-1874-4778-834d-04eb5a790afb.png)



## Usage

### Dynamic Equilibrium Graphing Simulation
**Note:** Make sure you have installed the `matplotlib` python package before running this python script. <br>
To start the dynamic equilibrium graph simulation, run the following command:
```
$ python3 dynamic_equilibrium_graph.py
```
You will then be greeted with a prompt for input data. The script allows you to configure the variables to your choosing before visualizing the results. The prompt will look something similar to this: <br> <br>
![image](https://user-images.githubusercontent.com/47650058/192431390-c1db4208-50df-43e2-94cd-884e13f16984.png) <br> <br>
After completing the input data prompts, the application will open a graph visualizer with the equilibrium graph (helps visualize the population percentage over time ratio) and a visual comparison between `x_(n+1)` and `x_n` to help explain how the population percentage may jump up and down but settle in at an equilibrium point. <br>
![image](https://user-images.githubusercontent.com/47650058/192678214-ef87e041-6f97-490f-83ad-394849222006.png)

### Random Manim Equilibrium Graph
**Note:** Make sure you have installed all **REQUIRED AND OPTIONAL** dependencies for manim first, and then installed the manim library itself.
To start the random manim equilibrium graph, run the following command:
```
$ manim -p -ql manim_equilibrium_graph.py RandomEquilibriumGraph
```
Similar to the Dynamic Equilibrium Graph, this script also generates a random equilibrium graph by randomly selecting variable values in the appropriate interval. This equilibrium graph script is animated with manim and is not as configurable as the equilibrium graph with the matplotlib package. <br> <br>
![chaossimulation](https://user-images.githubusercontent.com/47650058/192432660-b22f5a68-7b56-4c38-92c2-7fc2237a48fb.gif)

## Installation
**REQUIREMENT:** Must install [Python 3.7+](https://www.python.org/downloads/release/python-379/) (Versions of Python under 3.7 will not work for manim) <br> <br>
Before we download the chaos-theory project and run it, we need to install manim, a mathematics animation tool, and a bunch of other python packages that were used for the project.
**Note:** Please download all the **REQUIRED AND OPTIONAL** dependencies before moving on to installing manim.

### Linux
Follow the installation instructions on the [manim installation documentation page](https://docs.manim.community/en/stable/installation/linux.html) to completely install manim.
To finally install manim after installing the dependencies and rebooting your system, run the following command in a terminal:
```
$ pip3 install manim
```

### Windows
Follow the installation instructions using a package manager or installer of your choice from the [manim installation documentation page](https://docs.manim.community/en/stable/installation/windows.html).
To finally install manim after installing the dependencies, run the following command in your command prompt:
```
$ python -m pip install manim
```

### MacOS
Follow the installation instructions using a package manager or installer of your choice form the [manim installation documentation page](https://docs.manim.community/en/stable/installation/macos.html).
To finally install manim after downloading the dependencies, run the following command in your terminal:
```
$ pip3 install manim
```

### Python Packages
After installing manim successfully, we have to install some other python packages for GUI. <br>
Matplotlib, a graphing math utility for python, can be installed through pip just like manim and is necessary to run some parts of this application.
```
$ pip3 install matplotlib
```
or
```
$ python3 -m pip install matplotlib
```

## Credits
[Veritasium](https://www.youtube.com/c/veritasium) is a channel of science and engineering videos featuring experiments, expert interviews, cool demos, and discussions with the public about everything science. <br>
I recently came across a very intriguing [video about chaos theory](https://youtu.be/ovJcsL7vyrk) that they produced and was inspired to build this myself because I wanted to explore the logistic map and chaos for myself.
I used the [matplotlib](https://matplotlib.org/) python package and a [community managed version of manim](https://github.com/ManimCommunity/manim)

----

*Created by BooleanCube :]*
