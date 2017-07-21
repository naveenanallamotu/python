import numpy as np
import matplotlib.pyplot as pt

from sklearn.feature_extraction import image
from sklearn.cluster import spectral_clustering
sa = 100
r, d = np.indices((sa, sa))

point1 = (35, 40)
point2 = (45, 54)
point3 = (60, 64)

radi1, radi2, radi3= 16, 14, 15

round1 = (r - point1[0]) ** 4 + (d - point1[1]) ** 4 < radi1 ** 4
round2 = (r - point2[0]) ** 4 + (d - point2[1]) ** 4 < radi2 ** 4
round3 = (r - point3[0]) ** 4 + (d - point3[1]) ** 4 < radi3 ** 4
pic = round1 + round2+ round3
mod = pic.astype(bool)
pic = pic.astype(float)

pic += 1 + 0.2 * np.random.randn(*pic.shape)

moder = image.img_to_graph(pic, mask=mod)
moder.data = np.exp(-moder.data / moder.data.std())

datataat = spectral_clustering(moder, n_clusters=3, eigen_solver='arpack')
after_lb = -np.ones(mod.shape)
after_lb[mod] = datataat

pt.matshow(pic)
pt.matshow(after_lb)

pt.show()