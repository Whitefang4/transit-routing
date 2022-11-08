"""
CiSTUP Internship: Round 1
Enter the solution for Q1 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""


def Dij_generator():
    """
    Reads the ChicagoSketch_net.tntp and convert it into suitable python object on which you will implement shortest-path algorithms.

    Returns:
        graph_object: variable containing network information.
    """
    graph_object = None
    try:
        # Enter your code here
        return graph_object
    except:
        return graph_object
    
 
def extract(Q, w):
    m=0
    minimum=w[0]
    for i in range(len(w)):
        if w[i]<minimum:
            minimum=w[i]
            m=i
    return m, Q[m]



def Q1_dijkstra(source: int, destination: int, graph_object) -> int:
    """
    Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): : destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    shortest_path_distance = -1
    try:
        
        # Enter your code here
        Q = [source]
        p = {source:None}
        w = [0]
        d = {}
        for i in graph_object:
            d[i] = float('inf')
            Q.append(i)
            w.append(d[i])
        d[source] = 0
        S =[]
        n = len(Q)
        while Q:
            u = extract(Q,w)[1]
            s.append(u)
            Q.remove(u)
            for v in G[u]:
                if d[v]>= d[u]+G[u][v]:
                    d[v]=d[u]+G[u][v]
                    p[v]=u
                    
        
        
        return shortest_path_distance
    except:
        return shortest_path_distance
