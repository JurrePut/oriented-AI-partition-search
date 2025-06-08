from sage.graphs.graph_generators import graphs
from itertools import product
from sage.graphs.independent_sets import IndependentSets
import time


def find_cycle(G):
    """
    This function gets the cycle from a graph containing precisely 1 cycle
    """
    while not all((G.degree(v) > 1 for v in G.vertices())):
        degree1vertices = [v for v in G.vertices() if G.degree(v) == 1]
        G.delete_vertices(degree1vertices)
    start = G.vertices()[0]
    cycle = [start]
    for i in range(1,len(G)):
        neighbors = G.neighbors(cycle[i-1])
        if neighbors[0] in cycle:
            next_vertex = neighbors[1]
        else:
            next_vertex = neighbors[0]
        cycle += [next_vertex]
    return cycle + [start]

def is_satisfiable(G,cycles_left):
    """
    This function checks if all the cycles we got from check_partition can all be oriented at the same time
    """
    satgraph = Graph()
    for cycle in cycles_left:
        for c in range(len(cycle)-2):
            satgraph.add_edge(f"{cycle[c]}_{cycle[c+1]}", f"{cycle[c+1]}_{cycle[c+2]}")
            satgraph.add_edge(f"{cycle[c+2]}_{cycle[c+1]}", f"{cycle[c+1]}_{cycle[c]}")
    components = satgraph.connected_components()
    number_of_components = len(components)
    if number_of_components == 1:
        return False
    elif number_of_components == 0:
        return [(),1]
    assignments = [True] + [None]*(number_of_components-1)
    component_map = {}
    for i, component in enumerate(components):
        for node in component:
            component_map[node] = i  # Assign each node an index corresponding to its component
    for v in satgraph.vertices():
        parts = v.split('_')
        opposite_v = f"{parts[1]}_{parts[0]}"
        map_v = component_map.get(v)
        map_oppv = component_map.get(opposite_v)
        if map_v == map_oppv:
            return False
        if assignments[map_v] == True and assignments[map_oppv] == None:
            assignments[map_oppv] = False
        elif assignments[map_v] == None and assignments[map_oppv] == None:
            assignments[map_v] = True
            assignments[map_oppv] = False
    
    edges = []
    for v in satgraph.vertices():
        if assignments[component_map.get(v)] == True:
            parts = v.split('_')
            edges += [(f"{parts[1]}_{parts[0]}",component_map.get(v)//2)]
    return [edges,number_of_components/2]


def check_partition_oriented(G, independent_sets):
    vertices = G.vertices()
    for independent_set in independent_sets:
        tree_set = set(vertices) - set(independent_set)
        tree_subgraph = G.subgraph(tree_set)
        
        # Check if the partition gives us an acyclic graph
        if tree_subgraph.is_directed_acyclic():
            g = tree_subgraph.union(G.subgraph(independent_set))
            return g  # This graph can be partitioned
    return False  # No valid partition found


def check_partition(G):
    vertices = G.vertices()
    onecycles = []
    valid_independent_sets = []
    used_independent_sets = []

    for independent_set in IndependentSets(G):
        tree_set = set(vertices) - set(independent_set)
        tree_subgraph = G.subgraph(tree_set)
        # Check if the partition gives us a graph with 1 or 0 cycles
        if tree_subgraph.is_connected():
            if len(tree_subgraph) == tree_subgraph.size():
                onecycle = find_cycle(tree_subgraph)
                used_independent_sets += [independent_set]
                if onecycle not in onecycles:
                    onecycles += [onecycle]
            elif len(tree_subgraph) == tree_subgraph.size()+1:
                return False   
            else:
                valid_independent_sets += [independent_set] #only connected partitions have to be checked again later
    valid_filtered_independent_sets = [] #subsets of sets that result in one cycle cannot give an AI-partition
    for independent_set in valid_independent_sets:
        if not any(set(independent_set) < set(other) for other in used_independent_sets):
            valid_filtered_independent_sets.append(independent_set)
    return [onecycles,valid_filtered_independent_sets]    

def main(G):
    graph_information = check_partition(G)
    if graph_information is not False:
        satisfy = is_satisfiable(G, graph_information[0])
        if satisfy is not False:
            valid_independent_sets = graph_information[1]
            unassigned = G.size() - len(satisfy[0])
            for c in iter(product([True, False], repeat=satisfy[1]-1)):
                usededges = []
                c = [True] + list(c)
                for maps in satisfy[0]:
                    if c[maps[1]] == True:
                        usededges += [maps[0]]
                    else:
                        parts = maps[0].split('_')
                        usededges +=  [f"{parts[1]}_{parts[0]}"]

                true_edges = [e for e in G.edges() if f"{e[0]}_{e[1]}" in usededges]
                false_edges = [e for e in G.edges() if f"{e[1]}_{e[0]}" in usededges]
                unassigned_edges = [e for e in G.edges() if e not in true_edges and e not in false_edges]
                d0 = [e for e in true_edges] + [(e[1],e[0]) for e in false_edges]

                for a in iter(product([True, False], repeat=unassigned)):
                    u = 0
                    diedges = []
                    for e in unassigned_edges:
                        if a[u]:
                            diedges.append((e[0],e[1]))
                        else:
                            diedges.append((e[1],e[0]))
                        u += 1
                    diedges.extend(d0)
                    d = DiGraph(diedges)
                    if all((0 < d.out_degree(v) and 0 < d.in_degree(v)) for v in d.vertices()) or connectedness <= 1:
                        oplossing = check_partition_oriented(d, valid_independent_sets)
                        if oplossing is False:
                            return d
    return False
                        

minvert = int(input('minimum number of vertices'))
maxvert = int(input('maximum number of vertices'))
mindegree = int(input('minimum degree'))
maxdegree = int(input('maximum degree'))
connectedness = int(input('minimum connectedness'))
planar = bool(input('planar graphs only? (True/False)'))

numberofgraphs = 0
for n in range(minvert,maxvert+1):
    numberofgraphs = 0
    start_time = time.time()
    print('n =',n)
    checked = 0
    for G in iter(graphs.nauty_geng(f' -d{mindegree} -D{maxdegree} -c -b {n}')):  
        '''
        Generate undirected graphs of order n with given parameters, some options are:
        -d{mindegree}: only generate graphs with this as minimum degree
        -D{maxdegree}: only generate graphs with this as maximum degree
        -c: generate connected graphs
        -b: generate bipartite graphs
        -t: generate trianglefree graphs
        '''
        if G.vertex_connectivity() < connectedness:
            continue
        
        if planar:
            if not G.is_planar():
                continue

        oplossing = main(G)
        if oplossing is not False:
            show(oplossing)
            print('has no partition')
            for v in oplossing.vertices():
                print(f"{v}:{oplossing.neighbors_out(v)}", end=", ")
            print("")
            print('number of edges', oplossing.size())
            numberofgraphs += 1
        checked += 1
    end_time = time.time()
    print('graphs checked',checked)
    print('number of graphs found',numberofgraphs)
    print(f"Time taken = {end_time - start_time:.2f} seconds")   
