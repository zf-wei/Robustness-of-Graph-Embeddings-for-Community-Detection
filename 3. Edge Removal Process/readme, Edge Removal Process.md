# Edge Removal Process

This folder contains programs for generating edge and node removal sequences for both synthetic LFR graphs (`remove.py`) and real-world graphs (`remove_real.py`).

## Synthetic LFR Graphs - `remove.py`

The program `remove.py` generates edge and node removal sequences for synthetic LFR graphs. The following parameters can be specified:

- `-N` or `--N_value`: Number of Vertices.
- `-d` or `--disturb_type`: Disturbance type. Use 1 for random node selection and 5 for targeted node selection.
- `-m` or `--mu_value`: Mixing parameter.
- `-u` or `--percent_limit`: The upper bound for the proportion of selected nodes.

### Input Files

- `graph_1000_0.01.between`: File storing the betweenness centrality of nodes.
- `graph_1000_0.01.edgelist`: File storing the edgelist of the generated graph.
- `graph_1000_0.01.membership`: File storing the community membership of nodes.
- `graph_1000_0.01.rank`: File generated by `Gene_Btwn_Rank.ipynb` to store betweenness centrality rank information.

### Output Files

- `graph_1000_0.01.stoch_rmv`: File containing edge/node removal sequences for random node selection.
- `graph_1000_0.01.rank_rmv`: File containing edge/node removal sequences for targeted node selection based on betweenness centrality rank.

## Real World Graphs - `remove_real.py`

The program `remove_real.py` generates edge and node removal sequences for real-world graphs. The structure is similar with that of `remove.py`.

## Notes

- The naming convention for output files includes information about the graph size, mixing parameter and network disturbance type.
- The output files provide sequences for both random and targeted node selection.

Feel free to explore and utilize the generated edge and node removal sequences for your research.

For any questions or issues, please refer to the documentation or contact [zfwei11@gmail.com](mailto:zfwei11@gmail.com).