import random
import numpy as np

class bootstrapper(object):
    def __init__(self,X,num_samples,num_features):
        self.X=X
        self.num_samples=num_samples
        self.num_features=num_features

    def sample_chooser(self):
        X=self.X
        n=len(X)-1
        #list=[row for row in X]
        #print(list)
        m=int(2*n/3)
        indices=[random.randint(0,n-1) for _ in range(m)]
        dataset=[]
        for i in range(m):
            dataset.append(X[indices[i]])
        return np.array(dataset)
    
    def feature_chooser(self):
        X=self.X
        num_features, num_samples=np.shape(X)
        m=num_samples-1
        n=int(m**0.5)
        #print(m,n,num_samples)
        feature_indices=random.sample(range(m),n)
        #print(feature_indices)
        dataset=self.sample_chooser()
        small_data=[[] for _ in range(len(dataset))]
        for i in range(len(dataset)):
            for j in feature_indices:
                small_data[i].append(X[i][j])
            small_data[i].append(X[i][-1])
        #print(len(small_data),len(small_data[0]))
        return (small_data)        