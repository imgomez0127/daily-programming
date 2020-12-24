from math import log
from collections import Counter

def conditional_entropy(data, feature):
    total_samples = data.shape[0]
    entropy = 0
    converted_data = data[[feature]].values.reshape(-1)
    value_amts = Counter(converted_data)
    for value in value_amts.keys():
        converted_data = data[data[feature] == value]['class'].values.reshape(-1)
        value_amt = data[data['class'] == value].shape[0]
        category_counts = Counter(converted_data)
        category_entropy = 0
        for count in category_counts.values():
            category_entropy += count/value_amt * log(count/value_amt)
        entropy += value_amts/total_samples * category_entropy
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

class Node:
    def __init__(self, value, counts, edges=[]):
        self.value = value
        self.edges = edges
        self.decision = max(counts.keys(), key=lambda x: counts[x])

class DecisionTree:
    def __init__(self, data):
        decision = Counter(data[['class']])
        self.root = Node(None, decision)
        self.features = set(data.columns)
        self.features.remove('class')

    def build_tree_helper(self, root, features, data):
        if len(features) == 0:
            return
        if len(set(data[['class']].values.reshape(-1))) == 0:
            return
        feature = get_feature(data, features)
        categories = set(data[[feature]])
        features.remove(feature)
        for category in categories:
            converted_data = data[data[feature] == category]['class'].values.reshape(-1)
            counts = Counter(converted_data)
            cur_node = Node(category, counts)
            root.edges.append(cur_node)
            self.build_tree_helper(cur_node, features, data[data[feature] == category])

    def build_tree(self, data):
        self.build_tree_helper(self.root, self.features, data)
