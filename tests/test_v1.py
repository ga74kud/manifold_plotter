import manifold_plotter as mp
import md_pro as md
import numpy as np
import matplotlib.pyplot as plt



mygrid = {"x_grid": 5, "y_grid": 4, "x_min": -10, "x_max": 10, "y_min": -7.5, "y_max": 7.5}

amount_nodes=np.int(mygrid["x_grid"]*mygrid["y_grid"])

#start point
strt_pnt='0'
# points
P=md.get_meshgrid_points(**mygrid)
# Topology
T, S = md.get_simple_topology_for_regular_grid(P, **mygrid)
# rewards
R = {'16': 100}
mdp_challenge = {'S': S, 'R': R, 'T': T, 'P': P, 'gamma': .9}
# start Markov Decision Process
dict_mdp=md.start_mdp(mdp_challenge)
# plot the nodes
mp.plot_nodes(P, **{'U': dict_mdp['U']})
plt.show()