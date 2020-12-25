#!/usr/bin/env python3
"""
   Name    : decision_tree.py
   Author  : Ian Gomez
   Date    : December 25, 2020
   Description : An implementation of decision tree's (not even close to optimal).
                 This is learned in the same way I was taught in my ML class
                 By splitting data based on features where the best feature has
                 the highest Information Gain
                 (Which equates to lowest Shannon Conditional Entropy)
   Github  : imgomez0127@github
"""
from math import log
from collections import Counter
import numpy as np
import pandas as pd

def accuracy(true, preds):
    return np.sum(true == preds)/len(preds)
def conditional_entropy(data, feature):
    total_samples = data.shape[0]
    entropy = 0
    converted_data = data[[feature]].values.reshape(-1)
    value_amts = Counter(converted_data)
    for value in value_amts.keys():
        converted_data = data[data[feature] == value]['class'].values.reshape(-1)
        value_amt = data[data[feature] == value].shape[0]
        category_counts = Counter(converted_data)
        category_entropy = 0
        for count in category_counts.values():
            category_entropy += count/value_amt * log(count/value_amt)
        entropy += value/total_samples * category_entropy
    return entropy

def get_feature(data, features):
    best_feature = ""
    min_entropy = float('inf')
    for feature in features:
        feature_entropy = conditional_entropy(data, feature)
        if feature_entropy < min_entropy:
            min_entropy = feature_entropy
            best_feature = feature
    return best_feature

def check_inputs(data):
    data = data.values
    for i in range(data.shape[1]):
        if not (data[0, i] == data[:, i]).all():
            return False
    return True

class Node:
    def __init__(self, feature, value, counts, edges):
        self.feature = feature
        self.value = value
        self.edges = edges
        self.decision = max(counts.keys(), key=lambda x: counts[x])

    def __str__(self):
        return f'{self.feature} Node Value: {self.value} Decision: {self.decision}'

class DecisionTree:
    def __init__(self, data):
        decision = Counter(data[['class']].values.reshape(-1))
        self.root = Node("Root", None, decision, [])
        self.features = set(data.columns)
        self.features.remove('class')

    def build_tree_helper(self, root, features, data):
        if not features:
            return
        if not set(data[['class']].values.reshape(-1)):
            return
        if check_inputs(data):
            return
        feature = get_feature(data, features)
        categories = set(data[[feature]].values.reshape(-1))
        for category in categories:
            new_features = features.copy()
            new_features.remove(feature)
            converted_data = data[data[feature] == category]['class'].values.reshape(-1)
            counts = Counter(converted_data)
            cur_node = Node(feature, category, counts, [])
            root.edges.append(cur_node)
            self.build_tree_helper(cur_node, new_features, data[data[feature] == category])

    def build_tree(self, data):
        self.build_tree_helper(self.root, self.features, data)

    def predict_helper(self, root, data):
        if not root.edges:
            return root.decision
        feature = root.edges[0].feature
        feature_val = data[feature]
        for node in root.edges:
            if node.value == feature_val:
                return self.predict_helper(node, data)
        return root.decision

    def predict(self, data):
        return self.predict_helper(self.root, data)

    def build_str(self, root, i):
        S = (2 * i * '-') + str(root) + '\n'
        for node in root.edges:
            S += self.build_str(node, i+1)
        return S

    def __str__(self):
        return self.build_str(self.root, 0)

    def __call__(self, data):
        return self.predict(data)


if __name__ == "__main__":
    # For this example dataset I discritize the values because I am lazy
    # and do not want to deal with having to split real valued numbers into classes
    # Essentially it kinda does that by treating all intermediate float values
    # as just the base integer
    df = pd.read_csv('iris.data')
    class_names = ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica')
    classes = df['class'].values
    for i, class_name in enumerate(class_names):
        classes[classes == class_name] = i
    df['class'] = classes
    df = df.astype('int32')
    tree = DecisionTree(df)
    tree.build_tree(df)
    print(tree)
    print("Test Item:")
    print(df.iloc[0])
    print("Prediction")
    print(tree(df.iloc[0]))
    preds = np.array([tree(df.iloc[i]) for i in range(df.shape[0])])
    print(f'Tree Accuracy on training set: {accuracy(classes, preds)}')
