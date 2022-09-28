from manim import *


class DynamicEquilibriumGraph(Scene):
    def construct(self):
        r = 0.2  # rate of change has to be a value in the interval [0, 4]
        y_0 = 0.5  # y_initial has to be a value in the interval [0, 1]
        steps = 30  # the number of steps shown (x-axis range for time)
        skip = 0.2  # how much to skip (determines the number of animations) 4/0.5 = 20

        plot_axes = Axes(
            x_range=[0, steps, 2],
            y_range=[0, 1, 0.1],
            x_length=9,
            y_length=5.5,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
            },
            tips=False,
        )

        y_label = plot_axes.get_y_axis_label("0", edge=DOWN, direction=DOWN, buff=0.2)
        x_label = plot_axes.get_x_axis_label("\\text{Population Percentage ($y$) vs Time ($x$)}", edge=DOWN, direction=DOWN, buff=0.4)
        plot_labels = VGroup(x_label, y_label)

        extras = VGroup()
        extras += plot_axes.get_horizontal_line(plot_axes.c2p(steps, 1, 0), color=BLUE)
        extras += plot_axes.get_vertical_line(plot_axes.c2p(steps, 1, 0), color=BLUE)
        extras += Dot(point=plot_axes.c2p(steps, 1, 0), color=YELLOW)
        title = Title(
            r"Equilibrium Graph of $y_{x+1} = " + str(round(r, 2)) + " * (y_x) * (1 - y_x)$ with $y_0 = " + str(round(y_0, 2)) + "$",
            include_underline=False,
            font_size=40,
        )

        self.play(Write(title))
        self.play(Create(plot_axes), Create(plot_labels), Create(extras))

        prev = None
        while r < 4.0:
            # x represents time (x)
            # y represents population (y_x)
            x = np.zeros(steps + 1)
            y = np.zeros(steps + 1)
            x[0], y[0] = 0, y_0

            # Draw the equilibrium graph with the time to population relationship.
            for i in range(steps):
                y[i + 1] = r * y[i] * (1 - y[i])
                x[i + 1] = x[i] + 1

            plots = VGroup()
            plots += plot_axes.plot_line_graph(x_values=x, y_values=y, add_vertex_dots=True)

            if prev is None:
                prev = [Create(plot) for plot in plots]
                self.play(AnimationGroup(*prev))
                prev = [Uncreate(plot) for plot in plots]
            else:
                newtitle = Title(
                    r"Equilibrium Graph of $y_{x+1} = " + str(round(r, 2)) + " * (y_x) * (1 - y_x)$ with $y_0 = " + str(
                        round(y_0, 2)) + "$",
                    include_underline=False,
                    font_size=40,
                )
                self.remove(title)
                self.add(newtitle)
                title = newtitle
                self.play(AnimationGroup(*prev), run_time=0.01)
                new = [Create(plot) for plot in plots]
                self.play(AnimationGroup(*new))
                prev = [Uncreate(plot) for plot in plots]

            r += skip
            skip -= 0.005
            self.wait(0.1)
