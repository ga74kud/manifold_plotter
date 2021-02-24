import manifold_plotter_pkg as mp
import md_pro as md
import matplotlib.pyplot as plt


mygrid = {"x_grid": 5, "y_grid": 4, "x_min": -10, "x_max": 10, "y_min": -7.5, "y_max": 7.5}

# points
P=md.get_meshgrid_points(**mygrid)
# plot the nodes
mp.plot_patches(P)
plt.show()