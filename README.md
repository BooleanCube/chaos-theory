# chaos-theory

> Playing around with chaos theory simulations. Creating equilibrium graphs and visualizing the logistic maps.

## Usage

### Dynamic Equilibrium Graphing Simulation
**Note:** Make sure you have installed the `matplotlib` python package before running this python script. <br>
To start the dynamic equilibrium graph simulation, run the following command:
```
$ python3 dynamic_equilibrium_graph.py
```
You will then be greeted with a prompt for input data. The script allows you to configure the variables to your choosing before visualizing the results. The prompt will look something similar to this: <br> <br>
![image](https://user-images.githubusercontent.com/47650058/192431390-c1db4208-50df-43e2-94cd-884e13f16984.png) <br> <br>
After completing the input data prompts, the application will open a graph visualizer with the equilibrium graph. <br>
![image](https://user-images.githubusercontent.com/47650058/192431576-483fb014-d3f1-44a8-8086-22ecd7618c80.png)

### Random Manim Equilibrium Graph
**Note:** Make sure you have installed all **REQUIRED AND OPTIONAL** dependencies for manim first, and then installed the manim library itself.
To start the random manim equilibrium graph, run the following command:
```
$ manim -p -ql manim_equilibrium_graph.py RandomEquilibriumGraph
```
Similar to the Dynamic Equilibrium Graph, this script also generates a random equilibrium graph by randomly selecting variable values in the appropriate interval. This equilibrium graph script is animated with manim and is not as configurable as the equilibrium graph with the matplotlib package. <br> <br>
![chaossimulation](https://user-images.githubusercontent.com/47650058/192432660-b22f5a68-7b56-4c38-92c2-7fc2237a48fb.gif)

## Installation
**REQUIREMENT:** Must install [Python 3.7+](https://www.python.org/downloads/release/python-379/) (Versions of Python under 3.7 will not work for manim) <br>
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

----

*Created by BooleanCube :]*
