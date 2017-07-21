import numpy as np
import matplotlib.pyplot as pt
from sklearn import linear_model, datasets
load_dataset = datasets.load_iris()
col1 = load_dataset.data[:, :2]
col3 = load_dataset.target
h = .02
logistic_regression = linear_model.LogisticRegression(C=1e5)


logistic_regression.fit(col1, col3)
mini, maxi = col1[:, 0].min() - .7, col1[:, 0].max() + .7
miny, maxy = col1[:, 1].min() - .7, col1[:, 1].max() + .7
mm, zz = np.meshgrid(np.arange(mini, maxi, h), np.arange(miny, maxy, h))
Zu = logistic_regression.predict(np.c_[mm.ravel(), zz.ravel()])

Zu = Zu.reshape(mm.shape)
pt.figure(1, figsize=(7,9 ))
pt.pcolormesh(mm, zz, Zu, cmap=pt.cm.Paired)

pt.scatter(col1[:, 0], col1[:, 1], c=col3, edgecolors='y', cmap=pt.cm.Paired)
pt.xlim(mm.min(), mm.max())
pt.ylim(zz.min(), zz.max())
pt.xticks(())
pt.yticks(())

pt.show()