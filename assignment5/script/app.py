from bokeh.plotting import figure

from bokeh.io import curdoc

T= range(0,100)
S1 = [t for t in T]
S2 = [-t for t in T]

p = figure(x_range=(min(T), max(T)), y_range=(min(S2), max(S1)), title = "Simple Trend" )

curdoc().add_root()
