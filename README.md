# Network-Robustness

## Overview

This GitHub repository contains the code and tools used in the research paper titled `Robustness of graph embedding methods for community detection`. The project focuses on evaluating robustness of community detection methods based on graph embedding. Below is a brief guide to the organization of the repository.

## 0. Package WGE

In the folder `0. Package WGE`, you will find the tools and functions we designed to carry out various tasks.

## 1. Real World Graph Pre-Processing

In the folder `1. Real World Graph Pre-Processing`, you will find two real-world networks stored in `.gml` files. The notebook `GML_2_NetworkX & Test.ipynb` is provided to extract the edge list and community membership of nodes in these networks. Additionally, the notebook tests the distribution of community sizes and degree sequences for both networks.

## 2. Graph Generation and Pre-Processing

Navigate to `2. Graph Generation and Pre-Processing` to find files (`Gene_1k.py`, `Gene_1w.py`, `Gene_1k.ipynb`, `Gene_1w.ipynb`) for generating LFR networks. The generated networks are used to output the betweenness centrality of network nodes. The notebook `Gene_Btwn_Rank.ipynb` allows obtaining node ranks based on betweenness centrality.

## 3. Edge Removal Process

In the folder `3. Edge Removal Process`, there are two programs: `remove.py` for synthetic LFR graphs and `remove_real.py` for real-world graphs. These programs generate sequences of edges and nodes to be removed. Files with the extension `**.stoch_rmv` contain edge removal based on random node selection, while `**.rank_rmv` files contain edge removal based on targeted node selection considering betweenness centrality rank.

## 4. Main

Navigate to the `4. Main` folder to find scripts `Graph_Disturb.py` and `Graph_Disturb_real.py`. These programs are used to calculate ECS similarity scores with more edges removed from graphs.

## Usage

Detailed instructions and examples for running the code are provided in each folder's respective README files.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.