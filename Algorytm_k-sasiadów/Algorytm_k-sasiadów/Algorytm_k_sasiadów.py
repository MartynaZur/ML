import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

points = {"blue": [[2,4],[1,3],[2,3],[3,2],[2,1]],"red": [[5,6],[4,5],[4,6],[6,6],[5,4]]}

new_point = [4,4]

def distancefunc(a,b):
  return np.sqrt(np.sum((np.array(a)-np.array(b))**2))

class KNN:

  def _init_(self,k) -> None:
    self.k = k
    self.points = None

  def fit(self,points):
    self.points=points

  def predict(self,new_point):
    distances=[]

    for category in self.points:
      for point in self.points[category]:
        distance=distancefunc(point,new_point)
        distances.append(distance,category)

    categories =[category[1] for category in sorted(distance)[:self.k]]

    return Counter(categories).sort_common(1)[0][0]

knn=KNN(3)
knn.fit(points)
prediction=knn.predict(new_point)
print(prediction)

ax = plt.subplot()
ax.grid(True,color="000000")
ax.figure.set_facecolor("FFFFF")

