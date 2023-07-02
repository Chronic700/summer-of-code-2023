import numpy as np
import pandas as pd
class Node(object):
    def __init__(self,type=None,feature_ind=None,threshold=None,left=None,right=None,var_red=None,value=None):
        self.type=type
        #if decision node
        self.value=value

        #if path node
        self.feature_ind=feature_ind
        self.threshold=threshold
        self.left=left
        self.right=right
        self.var_red=var_red


class DecisionTreeRegressor(object):
    def __init__(self,min_samples=2,max_depth=2):
        self.root=None
        self.min_samples=min_samples
        self.max_depth=max_depth

    def build_tree(self,dataset,curr_depth):
        X,Y=dataset[:,:-1],dataset[:,-1]
        num_features,num_samples=np.shape(X)

        if curr_depth<=self.max_depth and num_samples>=self.min_samples:
            best_split=self.get_best_split(dataset, num_features, num_samples)

            if best_split['var_red']>0:
                left_subtree=self.build_tree(best_split['left_data'],curr_depth+1)
                right_subtree=self.build_tree(best_split['right_data'], curr_depth+1)

                return Node(type='path',feature_ind=best_split['feature_ind'],threshold=best_split['threshold'],
                            left=left_subtree,right=right_subtree,var_red=best_split['var_red'])
        
        decision_node_value=self.calculate_decision_node_value(Y)
        return Node(type='decision',value=decision_node_value)
    

    def get_best_split(self,dataset,num_features,num_samples):
        best_split={}
        max_var_red=-float('inf')

        for feature_ind in range(num_features):
            feature_values=dataset[:,feature_ind]
            possible_threshold=np.unique(feature_values)
            
            for threshold in possible_threshold:
                dataset_left=np.array([row for row in dataset if row[feature_ind]<=threshold])
                dataset_right=np.array([row for row in dataset if row[feature_ind]>threshold])

                var_red=self.calculate_var_red(dataset,dataset_left,dataset_right)

                if var_red>max_var_red:
                    best_split['feature_ind']=feature_ind
                    best_split['var_red']=var_red
                    best_split['threshold']=threshold
                    best_split['left_data']=dataset_left
                    best_split['right_data']=dataset_right
                    max_var_red=var_red

        return best_split
    
    def calculate_var_red(self,dataset,dataset_left,dataset_right):
        weight_l=len(dataset_left)/len(dataset)
        weight_r=len(dataset_right)/len(dataset_right)
        return np.var(dataset)-(weight_l*np.var(dataset_left)+weight_r*np.var(dataset_right))
    
    def calculate_decision_node(self,dataset_values):
        return np.mean(dataset_values)
    
    def fit(self,X,Y):
        dataset=np.concatenate((X,Y), axis=1)
        self.root=self.build_tree(dataset)
    
    def make_prediction(self,x,tree:Node):
        if tree.value!=None: return tree.value
        if x[tree.feature_ind]<=tree.threshold:
            return self.make_prediction(x,tree.left)
        else:
            return self.make_prediction(x,tree.right)
    
    def predictions(self,X):
        return [self.make_prediction(x,self.root) for x in X]
    