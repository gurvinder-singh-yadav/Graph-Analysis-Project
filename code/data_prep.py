import networkx as nx
import os
import pandas as pd
import json

class GraphModel:
    def __init__(self, root=".") -> None:
        self.root = root
        self.node_features()
        self.gen()
        self.node_labels()
        self.add_edges()
    def raw_files(self):
        dic = {"edges_list":"musae_git_edges.csv",
                "nodes_label":"musae_git_target.csv",
                "node_features":"musae_git_features.json"}
        return dic
    def node_labels(self):
        df = pd.read_csv("data/musae_git_target.csv")
        label_matrix = df[["id", "ml_target"]].values
        for key, label in label_matrix:
            self.features[str(key)]["label"] = label
    def add_edges(self):
        path = self.root + "/" + self.raw_files()["edges_list"]
        edge_list = tuple(pd.read_csv(path).values)
        self.Graph.add_edges_from(edge_list)
    def node_features(self):
        js = self.raw_files()["node_features"]
        jsObject = open(self.root + "/" + js)
        js_data = json.load(jsObject)
        node_features = {}
        nodes = []
        for key, value in js_data.items():
            features = {}
            nodes.append(key)
            features["feat"] = value
            # for index, feature in enumerate(value):
            #     features[str(index)] = feature
            node_features[str(key)] = features
        self.features = node_features
        self.nodes = nodes
        self.node_labels()
    def gen(self):
        self.Graph = nx.Graph()
        self.Graph.add_nodes_from(self.nodes)
        nx.set_node_attributes(self.Graph, self.features)
    def finalGraphModel(self):
        return self.Graph
