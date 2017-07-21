from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq

# data generation
data = vstack((rand(150,2) + array([0.5,0.5]),rand(150,2)))


centroids,_ = kmeans(data,2)

idx,_ = vq(data,centroids)

# now with K = 3 (3 clusters)
centroids,_ = kmeans(data,3)
idx,_ = vq(data,centroids)

plot(data[idx==0,0],data[idx==0,1],'p',
     data[idx==1,0],data[idx==1,1],'s',
     data[idx==2,0],data[idx==2,1],'b') # third cluster points
plot(centroids[:,0],centroids[:,1],'y',markersize=15)
show()