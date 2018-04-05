import numpy as np
import pandas as pd
import sklearn.neighbors.kd_tree as kdtree
import time

train_vecs = pd.read_pickle('train_vecs.pkl')
test_vecs = pd.read_pickle('test_vecs.pkl')

X = list(train_vecs[train_vecs.label!='new_whale'].vec)
Xlabel = list(train_vecs[train_vecs.label!='new_whale'].label)
Y = list(test_vecs.vec)

tree = kdtree.KDTree(X, leaf_size=10) 
dist, ind = tree.query(Y, k=5) 
threshold = dist.mean()/2
print('Setting threshold to:', threshold)

prediction = []
for k in range(len(Y)):
    
    labels = [Xlabel[i] for i in ind[k]]
    labels.insert(np.searchsorted(dist[k], threshold,side='left'), 'new_whale')
    
    prediction.append(' '.join(labels[:5]))

df = pd.DataFrame({'Image': list(test_vecs.name),'Id': prediction})
df = df[['Image','Id']]

df.to_csv("sub_test02.csv", index=False)