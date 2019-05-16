import json
import networkx as nx
from networkx.readwrite import json_graph

class DatabaseManager():

    def __init__(self):
        self.graph = None
        self.db = None
        self.db_type = 'json'
        self.file_path = 'db.json'
        self.node_size = 0
        self.edge_size = 0

    def loadDatabase(self):

        with open(self.file_path, 'r') as fp:
            self.db = json.load(fp)
            self.graph = json_graph.node_link_graph(self.db)
        self.node_size = len(self.graph.nodes)
        self.edge_size = len(self.graph.edges)

    def findNode(self, node_options):

        if 'name' in node_options:
            name = node_options['name']
            return self.graph.nodes[name]

    def addNode(self, node_options):

        if 'name' in node_options :
            import pdb; pdb.set_trace()
            self.graph.add_node(node_options['name'], **node_options)
            with open(self.file_path, 'w') as fp:
                json.dump(json_graph.node_link_data(self.graph), fp)
            return self.findNode(node_options)
        else : 
            return False

    def addEdge(self, edge_options):

        if 'uv_nodes' in edge_options and len(edge_options['uv_nodes']) == 2 :
            uv_nodes = edge_options.pop('uv_nodes')
            self.graph.add_edge(*uv_nodes, **edge_options)
            with open(self.file_path, 'w') as fp:
                json.dump(json_graph.node_link_data(self.graph), fp)
            return 'success'

