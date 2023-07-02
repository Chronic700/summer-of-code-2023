from dt import Node
from dt import DecisionTreeRegressor
from rtd import bootstrapper
import numpy as np
import pandas as pd
import csv
from tqdm import tqdm

#phone_data=pd.read_csv("C:\\Users\\Shikhar Gupta\\Desktop\\Mobile Phone1.csv")
#print(phone_data.head(10))
#test_phone_data=pd.read_csv("C:\\Users\\Shikhar Gupta\\Desktop\\Mobile Phones.csv")

phone_data=[]
with open("Mobile Phone3.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
            phone_data.append(row)
# for e in phone_data[-1]:
#     print(type(e))

for i in range(len(phone_data)):
        phone_data[i][0], phone_data[i][1], phone_data[i][4], phone_data[i][5], phone_data[i][7], phone_data[i][8]= int(phone_data[i][0]), int(phone_data[i][1]), int(phone_data[i][4]), int(phone_data[i][5]), int(phone_data[i][7]), int(phone_data[i][8])
        phone_data[i][2], phone_data[i][3], phone_data[i][6]=float(phone_data[i][2]), float(phone_data[i][3]), float(phone_data[i][6])

class RandomForest(object):
    def __init__(self,dataset,tree_count):
        self.dataset=dataset
        self.tree_count=tree_count
        self.forest=[]
    
    def data_maker(self,dataset):
        num_features,num_samples=np.shape(dataset)
        randomizer=bootstrapper(dataset,num_samples,num_features)
        return randomizer.feature_chooser()
    
    def tree_maker(self):
        dataset=self.data_maker(self.dataset)
        tree=DecisionTreeRegressor(min_samples=3,max_depth=4)
        # X = dataset.iloc[: :-1].values
        # Y = dataset.iloc[: -1].values.reshape(-1,1)
        tree.fit(dataset)
        return tree
    
    def forest_maker(self):
        if hasattr(tqdm,'_instances'): tqdm._instances.clear()
        for i in tqdm(range(self.tree_count)):
            self.forest.append(self.tree_maker())
    
    def make_a_prediction(self,x:list):
        expected_values=[]
        for i in range(self.tree_count):
            tree=self.forest[i]
            expected_values.append(tree.make_prediction(x,tree.root))
        return np.mean(expected_values)
    
    def predict(self,X):
        return [self.make_a_prediction(x) for x in X]


# Our_Forest=RandomForest(phone_data,100)
# Our_Forest.forest_maker()
