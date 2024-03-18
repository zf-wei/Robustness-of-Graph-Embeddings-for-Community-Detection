# Main - Graph Disturbance Programs

This folder contains programs to evaluate robustness of network community detection under graph disturbance on synthetic graphs using "Graph_Disturb.py" and on real-world graphs using "Graph_Disturb_real.py."

## Graph Disturbance for Synthetic Graphs - `Graph_Disturb.py`
This program is designed to evaluate robustness of community structure for LFR synthetic networks.

### Input Files

- `graph_1000_0.01.between`: File storing the betweenness centrality of nodes.

- `graph_1000_0.01.edgelist`: File storing the edgelist of the LFR graph.

- `graph_1000_0.01.membership`: File storing the community membership of nodes.

- `graph_1000_0.01.rank`: File storing the betweenness centrality rank of nodes.

- `graph_1000_0.01.stoch_rmv`: File containing edge/node removal sequences for random node selection.

- `graph_1000_0.01.rank_rmv`: File containing edge/node removal sequences for targeted node selection based on betweenness centrality rank.

  *Note: The numbers in the file names (e.g., 1000 and 0.01) are examples representing the number of nodes and mixing parameters.*

### Parameters

- `-N` or `--N_value`: Number of nodes.
- `-D` or `--D_value`: Embedding Dimension.
- `-M` or `--M_value`: Embedding Method ID (1: HOPE, 2: Laplacian Eigenmap, 3: LLE, 4: DeepWalk, 5: M-NMF, 6: LINE, 7: node2vec).
- `-d` or `--disturb_type`: Disturbance Type (1: Random node selection, 5: Targeted node selection).
- `-m` or `--mu_value`: Mixing parameter. (e.g., 0.01)

### Output Files

The output files are mean value and standard deviation of ECS similarity scores:

- For Random Node Selection: mean value of ECS is stored in `Stoch_{Number of nodes}_{mixing parameter}_{embedding dimension}dim_{method id}_MEAN.csv`; standard deviation of ECS is stored in `Stoch_{Number of nodes}_{mixing parameter}_{embedding dimension}dim_{method id}_STD.csv`.
- For Targeted Node Selection: mean value of ECS is stored in `Rank_{Number of nodes}_{mixing parameter}_{embedding dimension}dim_{method id}_MEAN.csv`; standard deviation of ECS is stored in `Rank_{Number of nodes}_{mixing parameter}_{embedding dimension}dim_{method id}_STD.csv`.

## Graph Disturbance for Real-World Graphs - `Graph_Disturb_real.py`
This program is designed to evaluate robustness of community structure for real world networks. Everything is similar with that in `Graph_Disturb.py`.
## Note

- The usage of LINE and LLE depends on the availability of a GPU.

Feel free to explore and utilize the output files for further analysis. For any questions or issues, please refer to the documentation or contact [zfwei11@gmail.com](zfwei11@gmail.com).