# chaos-theory

> Playing around with chaos theory simulations. Creating equilibrium graphs and visualizing the logistic maps.

## Chaos Theory
The Logistic Map is derived from a very simple mathematical recursive function: `x_(n+1) = r * (x_n) * (1-x_n)` <br>
In this case, I would like to take the example of a population percentage over time (years) graph to explain the logistic map.
- x_(n+1) represents population percentage next year (a value in the interval [0,1])
- x_n represents the population percentage this year (a value in the interval [0,1])
- r represents the fertility rate (a value in the interval [0,4])

The very simple equation has extremely complex behaviour that becomes very chaotic (hard to predict) at high rate (r) values. <br>
These types of maps are often used to be able to predict population percentage or visualize repetitive chaos until the repeating window is so large that it is considered to be arbitrary.
When you graph out the logistic map for population percentage over time, we see that for each rate of change value (r) there is a set equilibrium value regardless of initial population percentage (x_0) which is where all randomness and chaos ceases and settles in at a particular point. So, let's explore how the equilibrium point is related to the rate of change (fertility rate) values.<br>

### Relationship between rate of change and equilibrium points
- When the rate of change (fertility rate) is too low, for example less than 1.00, the equilibrium point will be 0.00 which means the species has gone extinct. <br>
![image](https://user-images.githubusercontent.com/47650058/192679432-e0909c11-4296-42e4-adfd-7a4b90e8a778.png)
- When the rate of change (fertility rate) is decently large, for example less than 3.00, the equilibrium point will be at a set value above 0.00 so the population settles in at a percentage, the equilibrium point, without going extinct. This phenomenon is common in nature, as we usually see the populations start to stabilize over time as long as there are no external events causing the population percentage to falter. In this example we can see the equilibrium point to be ~0.65.
![image](https://user-images.githubusercontent.com/47650058/192680494-2e60daf4-823d-489e-990d-7d26d9e77556.png)
- So far, the equilibrium graph seems reasonable and appropriate. However, this is where the chaos begins. When the rate of change (fertility rate) is too high, for example greater than or equal to 3.00, we start to see more than 1 equilibrium point and more arbitrary results. As the fertility rate (rate of change) increases, the chaos (randomness) also grows exponentially and splits into more equilibrium points exponentially. When the equilibrium point splits into multiple points again, we call it a bifurcation. At `r=3.6` we start to see fractal-like behaviour in the logistic map because of the amount of bifurcations. This phenomenon is also fairly common in nature, as some populations could oscillate between different percentage values over a window of time repeatedly. In this example, we can see there are 4 equilbirium points, so there must have been 3 period-doubling bifurcations in the equilibrium graph (First splits into 2, and then the 2 split into 4). <br>
![image](https://user-images.githubusercontent.com/47650058/192681721-14e85352-1874-4778-834d-04eb5a790afb.png)

## Bifurcation Diagram
The Bifurcation Diagram graphically represents the behaviors observed between the rate of change and the equilibrium points as mentioned above in <a href="https://github.com/BooleanCube/chaos-theory#relationship-between-rate-of-change-and-equilibrium-points">"Chaos Theory"</a>
The figure below graphs the detailed complexity of how the rate of change affects equilibrium, in other words, how the rate of change relates to chaos.
We can visually see most of the periodically doubling bifurcation but after `r=3.6` it starts to get really chaotic and the equilibrium points are almost entirely random.

![image](https://user-images.githubusercontent.com/47650058/192730089-e254d51a-8ca9-44e3-a2bc-71987ef1a085.png)

### Feigenbaum Constant
Mitchell J. Feigenbaum observed that there was a common ratio between the widths of the periodically doubling bifurcations. Even though Feigenbaum originally related to the period-doubling bifurcations in the logistic map, it showed universality (observed as a property in large independent systems. Therefore, we can conclude that every chaotic system that fits the requirements will bifurcate at the same constant rate. <br>

The feigenbaum constant is the limit as n approaches infinity of the ratio between each bifurcation interval width to the next between every period-doubling. <br>

![image](https://user-images.githubusercontent.com/47650058/192737008-41bb896e-47b4-4cec-a273-e420bf95fcae.png) <br>
![image](https://user-images.githubusercontent.com/47650058/192737182-f98e5dd0-614a-4d0d-8b9f-fb358c9f3f02.png)

As we can see from our graphed bifurcation diagram figure above, the bifurcation intervals and the interval widths match the description in the table above and so I can conclude with my calculations that the feigenbaum constant is indeed ~4.669.

## Usage

### Static Equilibrium Graphing Simulation
**Note:** Make sure you have installed the `matplotlib` python package before running this python script. <br>
To start the static equilibrium graph simulation, run the following command:
```
$ python3 static_equilibrium_graph.py
```
You will then be greeted with a prompt for input data. The script allows you to configure the variables to your choosing before visualizing the results. The prompt will look something similar to this: <br> <br>
![image](https://user-images.githubusercontent.com/47650058/192431390-c1db4208-50df-43e2-94cd-884e13f16984.png) <br> <br>
After completing the input data prompts, the application will open a graph visualizer with the equilibrium graph (helps visualize the population percentage over time ratio) and a visual comparison between `x_(n+1)` and `x_n` to help explain how the population percentage may jump up and down but settle in at an equilibrium point. <br>

![image](https://user-images.githubusercontent.com/47650058/192678214-ef87e041-6f97-490f-83ad-394849222006.png)

### Dynamic Manim Equilibrium Graph
**Note:** Make sure you have installed all **REQUIRED AND OPTIONAL** dependencies for manim first, and then installed the manim library itself. <br>
To start the dynamic manim equilibrium graph, run the following command:
```
$ manim -p -ql dynamic_equilibrium_graph.py DynamicEquilibriumGraph
```
Similar to the Static Equilibrium Graph, this script also generates all equilibrium graphs by iterating through the interval values for the rate of change variable. *This equilibrium graph script is animated with manim and is not as configurable as the equilibrium graph with the matplotlib package.* <br> <br>
![dynamicequilibriumgraph](https://im5.ezgif.com/tmp/ezgif-5-fda7b8c5f3.gif)

### Bifurcation Diagram
**Note:** Make sure you have installed all **REQUIRED AND OPTIONAL** dependencies for manim first, and then installed the manim library itself. <br>
To start the bifurcation diagram figure animation, run the following command:
```
$ manim -p -ql bifurcation_diagram.py BifurcationDiagram
```
As described in the [Bifurcation Diagram Analysis](https://github.com/BooleanCube/chaos-theory#bifurcation-diagram), this is nothing more than an animation of the Bifurcation Diagram being generated. You can also see the animation without having to run the manim code: <br>

![bifurcationdiagram](https://user-images.githubusercontent.com/47650058/192745066-2413253a-cf56-4e45-9079-1d97b5d27004.gif)

### Feigenbaum Constant Calculator
**Note:** You must have any version of python3 installed on your computer. Preferably one of the more recent versions (Versions 3.7.9+)
To started the feigenbaum calculator, run the following command:
```
$ python3 feigenbaum_calculator.py
```
This runs a simulation of ALL equilibrium graphs with r values that iterates every 0.00001. Such a small iteration amount makes the calculator very slow to make calculations but also makes it more precise. As described in the [Feigenbaum Constant Analysis](https://github.com/BooleanCube/chaos-theory#feigenbaum-constant), the calculator finds the bifurcation parameters where the number of equilibrium points double. The calculations are not entirely precise and accurate because of the rounding of the rate of change values and the bifurcation parameter values. There is no way to really calculate where the period-doubling bifurcations are, so we have to run simulations with perfect precision to observe where they appear. Here are the most precise results I could produce: <br>

![image](https://user-images.githubusercontent.com/47650058/192828501-b883c4b2-8987-4a25-b9f6-91422039aebf.png) <br>
![image](https://user-images.githubusercontent.com/47650058/192737182-f98e5dd0-614a-4d0d-8b9f-fb358c9f3f02.png)

We can see from the calculations, the ratio that is being calculated as n approaches infinity continuously moves towards ~4.669 which is the feigenbaum constant.

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
I recently came across a very intriguing [video about chaos theory](https://youtu.be/ovJcsL7vyrk) that they produced and was inspired to build this myself because I wanted to explore the logistic map and chaos for myself. <br>
**Packages Used:** <br>
IEEE COMPUTER SOC. (2007). Matplotlib: A 2D graphics environment (Version 3.6.0) [Computing in Science \& Engineering]. 10.1109/MCSE.2007.55 <br>
The Manim Community Developers. (2022). Manim – Mathematical Animation Framework (Version v0.16.0) [Computer software]. https://www.manim.community/

----

*Created by BooleanCube :]*
