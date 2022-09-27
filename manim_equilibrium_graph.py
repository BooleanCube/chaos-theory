from manim import *
import random


class RandomEquilibriumGraph(Scene):
    def construct(self):
        r = random.random()*4  # rate of change has to be a value in the interval [0, 4]
        x_0 = random.random()  # x_initial has to be a value in the interval [0, 1]
        steps = 30  # the number of steps shown (x-axis range for time)

        plot_axes = Axes(
            x_range=[0, steps, 2],
            y_range=[0, 1, 0.1],
            x_length=9,
            y_length=5.5,
            axis_config={
                "numbers_to_include": np.arange(steps+1),
                "font_size": 20,
            },
            tips=False,
        )

        y_label = plot_axes.get_y_axis_label("0", edge=DOWN, direction=DOWN, buff=0.2)
        x_label = plot_axes.get_x_axis_label("\\text{Population Percentage ($y$) vs Time ($x$)}", edge=DOWN, direction=DOWN, buff=0.4)
        plot_labels = VGroup(x_label, y_label)

        # x represents time (n)
        # y represents population (x_n)
        x = np.zeros(steps + 1)
        y = np.zeros(steps + 1)
        x[0], y[0] = 0, x_0

        # Draw the equilibrium graph with the time to population relationship.
        for i in range(steps):
            y[i + 1] = r * y[i] * (1 - y[i])
            x[i + 1] = x[i] + 1

        plots = VGroup()
        plots += plot_axes.plot_line_graph(x_values=x, y_values=y, add_vertex_dots=True)

        extras = VGroup()
        extras += plot_axes.get_horizontal_line(plot_axes.c2p(steps, 1, 0), color=BLUE)
        extras += plot_axes.get_vertical_line(plot_axes.c2p(steps, 1, 0), color=BLUE)
        extras += Dot(point=plot_axes.c2p(steps, 1, 0), color=YELLOW)
        title = Title(
            r"Equilibrium Graph of $x_{n+1} = " + str(round(r, 2)) + " * (x_n) * (1 - x_n)$ with $x_0 = " + str(round(x_0, 2)) + "$",
            include_underline=False,
            font_size=40,
        )

        self.play(Write(title))
        self.play(Create(plot_axes), Create(plot_labels), Create(extras))
        self.play(AnimationGroup(*[Create(plot) for plot in plots], lag_ratio=0.05))
        self.wait(60)
