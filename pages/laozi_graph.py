# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 20:06:41 2023

@author: jpwu
"""

import rdflib
from rdflib import Graph
from streamlit_agraph import agraph, Node, Edge, Config

graph = Graph()
graph.parse(r"C:\老子研究\知识图谱\laozi.rdf")
nodes=[]
edges=[]
ids = []
for subj, pred, obj in graph:
    subj = rdflib.namespace.split_uri(subj)[-1]
    if subj not in ids:
        source_node = Node(id=subj, label=subj)
        nodes.append(source_node)
        ids.append(subj)
    obj = rdflib.namespace.split_uri(obj)[-1]
    if obj not in ids:
        target_node = Node(id=obj, label=obj)
        nodes.append(target_node)
        ids.append(obj)

    pred = rdflib.namespace.split_uri(pred)[-1]
    edges.append(Edge(source=subj, 
                          label=pred, 
                          target=obj)) 
    
config = Config(width=750,
                height=950,
                directed=True, 
                physics=True, 
                hierarchical=True,
                )
    
agraph(nodes,edges,config)