"""
Enter the solution for Q3 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""


def number_of_routes(source_stopid: str, destination_stopid: str) -> int:
    """
    Find the number of routes going from source stop id to destination stop id.

    Args:
        source_stopid (str): Source Stop Id
        destination_stopid (str): Destination Stop Id

    Returns:
        final_count (int): Number of routes going from source to destination.
    """
    final_count = -1
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
        final_count = 0
        while Q:
            u = extract(Q,w)[1]
            s.append(u)
            Q.remove(u)
            for v in G[u]:
                if d[v]>= d[u]+G[u][v]:
                    d[v]=d[u]+G[u][v]
                    p[v]=u
            final_count = final_count +1
        
        
        return final_count
    except:
        return final_count
