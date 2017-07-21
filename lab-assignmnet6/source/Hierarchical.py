import numpy as np
from sklearn.cluster import MeanShift  # as ms
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as pt
from mpl_toolkits.mplot3d import Axes3D
#from matplotlib import style

#style.use("ggplot")

ponits = [[3, 3, 3], [9, 9, 9], [2, 9, 9]]

mo, _ = make_blobs(n_samples=1500, centers=ponits, cluster_std=0.5)

shift_calulating = MeanShift()
shift_calulating.fit(mo)
datalabeling = shift_calulating.labels_
centersofpoints = shift_calulating.cluster_centers_

print(centersofpoints)

clustertospot = len(np.unique(datalabeling))

print("esitmated clustering group", clustertospot)

penning = 20 * ['y', 'c', 'm', 'p', 's', 'd', 't']

print(penning)
print(datalabeling)

fig = pt.figure()
axised = fig.add_subplot(111, projection='3d')

for i in range(len(mo)):
    axised.scatter(mo[i][0], mo[i][1], mo[i][2], c=penning[datalabeling[i]], marker='o')

axised.scatter(centersofpoints[:, 0], centersofpoints[:, 1], centersofpoints[:, 2],
           marker="x", color='k', s=150, linewidths=5, zorder=10)

pt.show()
