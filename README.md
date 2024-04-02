- # Robustness-of-Graph-Embeddings-for-Community-Detection

## Overview

This GitHub repository contains the code and tools used in the research paper titled `Robustness of graph embedding methods for community detection` (arXiv here: UNDER CONSTRUCTION). The project focuses on evaluating robustness of community detection methods based on graph embeddings. Below is a brief guide to the organization of the repository.

## 0. Package WGE

In the folder `0. Package WGE`, you will find some basic tools and functions we designed to carry out various tasks. They are enclosed as a package `WGE`, which can be installed from the folder.

## 1. Real World Graph Pre-Processing

In the folder `1. Real World Graph Pre-Processing`, you will find two real-world networks stored in `.gml` files. The notebook `GML_2_NetworkX & Test.ipynb` is provided to extract the edge list and community membership of nodes in these real-world networks. Additionally, the notebook tests the distribution of community sizes and degree sequences for both networks.

## 2. Graph Generation and Pre-Processing

Navigate to `2. Graph Generation and Pre-Processing` to find files (`Gene_1k.py`, `Gene_1w.py`, `Gene_1k.ipynb`, `Gene_1w.ipynb`) for generating LFR networks. The betweenness centrality of network nodes are also calculated and output. The notebook `Gene_Btwn_Rank.ipynb` allows obtaining node ranks based on betweenness centrality.

## 3. Edge Removal Process

In the folder `3. Edge Removal Process`, there are two programs: `remove.py` for synthetic LFR graphs and `remove_real.py` for real-world graphs. These programs generate sequences of edges and nodes to be removed. Files with the extension `**.stoch_rmv` contain edge removal based on random node selection, while `**.rank_rmv` files contain edge removal based on targeted node selection considering betweenness centrality rank.

## 4. Main

Navigate to the `4. Main` folder to find programs `Graph_Disturb.py` and `Graph_Disturb_real.py`. These programs are used to calculate ECS similarity scores with more edges removed from graphs.

## Usage

Detailed instructions and examples for running the code are provided in each folder's respective README files.

## Requirements

### Computation Environment

Our computations are performed on the Big Red 200 supercomputer, an HPE Cray EX system designed by Indiana University to support scientific and medical research, as well as advanced research in artificial intelligence, machine learning, and data analytics.

- **Specifications:**
  - 640 compute nodes with 256 GB of memory each
  - Two 64-core, 2.25 GHz, 225-watt AMD EPYC 7742 processors per node
  - 64 GPU-accelerated nodes with 256 GB of memory
  - Single 64-core, 2.0 GHz, 225-watt AMD EPYC 7713 processor per GPU node
  - Four NVIDIA A100 GPUs per GPU node
  - Theoretical peak performance (Rpeak) of nearly 7 petaFLOPS
  - Managed with HPE's Performance Cluster Manager (HPCM)
  - Operating System: SUSE Enterprise Linux Server (SLES) version 15 on compute, GPU, and login nodes

### Modules Used

The following modules are loaded for the project on Big Red 200:

```bash
module load cudatoolkit
module load python/gpu/3.10.5
```

### Python Packages
All the required Python packages for running our experiments are listed in the `requirements.txt` file.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.