import argparse
from WGE.graph_input import graph_input_simple
import multiprocessing
from WGE.remove_procedure import generate_remove_procedure_realreal

# Create argument parser
parser = argparse.ArgumentParser(description='This program performs graph embedding, clustering. Plot will be made accordingly')

# Add command line arguments
parser.add_argument('-N', '--N_value', type=int, help='Number of Vertices')
parser.add_argument('-d', '--disturb_type', type=int, help='Disturb type?')
parser.add_argument('-m', '--mu_value', type=float, help='mu_value')  
parser.add_argument('-u', '--percent_limit', type=float, help='percent_limit')  

# Parse command line arguments
args = parser.parse_args()

# Read values of command line arguments
N = args.N_value
disturb_type=args.disturb_type
mu = args.mu_value
upperbound = args.percent_limit


graph, membership, between = graph_input_simple(N=N, mu=mu, disturb_type=disturb_type)  

if disturb_type==1:
    between = [0] * graph.number_of_nodes()

print(N, mu)
generate_remove_procedure_realreal(disturb_type=disturb_type, mu=mu, graph=graph,
                                   number_of_nodes=graph.number_of_nodes(), betweenness=between, upperbound=upperbound,
                                   sample_count=50)
