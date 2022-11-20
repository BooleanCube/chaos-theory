import numpy as np
from manim import *


class BifurcationDiagram(Scene):
    def construct(self):
        r = 0.01  # rate of change value (r) will be changing but starts as 0.01
        y_0 = 0.5  # y_initial value doesn't matter for the equilibrium point
        steps = 200  # the number of steps calculated for each rate of change (x-axis range for time)
        iterate = 0.01  # gap between each iteration

        plot_axes = Axes(
            x_range=[0, 4, 0.5],
            y_range=[-0.1, 1.1, 0.1],
            x_length=9,
            y_length=5.5,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
            },
            tips=False,
        )

        y_label = plot_axes.get_y_axis_label("", edge=DOWN, direction=DOWN, buff=0.2)
        x_label = plot_axes.get_x_axis_label("\\text{Equilibrium Point(s) ($y$) vs Rate of Change ($x$)}", edge=DOWN,
                                             direction=DOWN, buff=0.4)
        plot_labels = VGroup(x_label, y_label)

        # x represents rate of change (r)
        # y represents equilibrium point(s) in population percentage
        x = []
        y = []

        while r < 4.0:
            tx = np.zeros(steps+1)
            ty = np.zeros(steps+1)
            tx[0], ty[0] = 0, y_0

            # Draw the equilibrium graph with the time vs population relationship.
            for i in range(steps):
                ty[i+1] = r * ty[i] * (1 - ty[i])
                tx[i+1] = tx[i] + 1

            # Iterate through the graph starting from the end (time = 1000) and add all the population percentages
            # into a set of equilibrium points. Maximum of 50 equilibrium points can be set for each rate of change.
            eqpoints = set()
            for i in range(steps-1, steps-51, -1):
                v = round(ty[i], 3)
                eqpoints.add(v)

            # Adding equilibrium points to the graph
            for i in eqpoints:
                x.append(r)
                y.append(i)

            r += iterate

        plots = VGroup()
        for i in range(len(x)):
            plots += Dot(point=plot_axes.c2p(x[i], y[i], 0), color=BLUE, radius=0.02)
        extras = VGroup()
        extras += plot_axes.get_horizontal_line(plot_axes.c2p(4, 1, 0), color=BLUE)
        extras += plot_axes.get_vertical_line(plot_axes.c2p(4, 1, 0), color=BLUE)
        extras += Dot(point=plot_axes.c2p(4, 1, 0), color=YELLOW)
        title = Title(
            r"Logistic Map of $y_{x+1} = r * (y_x) * (1 - y_x)$",
            include_underline=False,
            font_size=40,
        )

        self.play(Write(title))
        self.play(Create(plot_axes), Create(plot_labels), Create(extras))
        self.play(AnimationGroup(*[Create(plot) for plot in plots], lag_ratio=0.03))
        self.wait(5)
