A long time ago I heard about 'six degrees of separation', and the topic recently came up in a BCG training lecture. We were shown the ['Oracle of Bacon'](https://oracleofbacon.org/) site which shows actor's relationship to Kevin Bacon. I was curious what was the maximum relationship level, so I got to coding. I found this especially interesting as I have recently completed an algorithms course and this looked like a great use case for testing out a breadth-first-search algorithm. I had recently completed another toy project that needed some graphing algorithms so I saw this as a great chance to practice further.

So, the punchline is that the greatest distance Actor to Kevin Bacon is the infamous [Iraj Safavi](https://www.imdb.com/name/nm0755811/) with 10 links. Personally I thought his best acting work was in the 1989 film [Homework](https://www.imdb.com/title/tt0097843/?ref_=nm_flmg_cin_4) (I'm bullshitting I have no idea who he is). It seems the Iranian film industry is quite isolated from Hollywood (makes sense). Given this linkage is only in terms of co-acting, it makes sense that this number is higher than the 'six degrees' where being an acquaintance is enough.

The following is the code used to obtain the results. Be warned that the BFS takes a very long time. The data for the project can be [found here as JSON](https://oracleofbacon.org/how.php).

And you can enter Iraj Safavi [here](https://oracleofbacon.org/) as an 'actor' link. https://oracleofbacon.org/

The following is the code you can use to replicate. BFS uses a linked list, which is commonly a dictionary of str: list indicating actor and co-stars. This was done as a str:set to speed things up.


    import os
    import json
    from collections import defaultdict
    from tqdm import tnrange
    import itertools
    from tqdm import tqdm
    import pandas as pd


    # Load data (cant quite straight import)
    file = "data.txt"
    data = []
    with open(file, 'r') as f:
        data = f.readlines()
    data = [json.loads(d) for d in data]

    # Get unique list of actors
    all_cast = []

    for movie in data:
        for actor in movie["cast"]:
            all_cast.append(actor)

    all_cast = list(set(all_cast))
    len(all_cast)

    # Get linked list of actor: [worked with, ...]
    # Fast method. Not worried about self-duplication
    cast_associations = defaultdict(set)

    for m in tnrange(len(data)):
        movie = data[m]

        for c1 in movie["cast"]:
            for c2 in movie["cast"]:
                cast_associations[c1].add(c2) # Add both ways
                cast_associations[c2].add(c1)

    # Remove self from cast associations to speed things up
    for cast in cast_associations:
        cast_associations[cast].remove(cast)

    # Check Mr Bacon's associations
    cast_associations["Kevin Bacon"]

    # Grabbed a standard breadth first search off stackoverflow
    # Credit https://stackoverflow.com/questions/46383493/python-implement-breadth-first-search
    # With small modifications

    # visits all the nodes of a graph (connected component) using BFS
    def bfs_connected_component(graph, start):
        # keep track of all visited nodes
        explored = []
        # keep track of nodes to be checked
        queue = [start]

        levels = {}         # this dict keeps track of levels
        levels[start]= 0    # depth of start node is 0

        visited= [start]     # to avoid inserting the same node twice into the queue

        # keep looping until there are nodes still to be checked
        with tqdm(total=len(graph)) as pbar: # Added a timing check
            while queue:
               # pop shallowest node (first node) from queue
                node = queue.pop(0)

                explored.append(node)
                neighbours = graph[node]

                # Consider adding a set->list operation every 10,000 iterations or so to speed up search process


                # add neighbours of node to queue
                for neighbour in neighbours:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        visited.append(neighbour)
                        pbar.update(1)

                        levels[neighbour] = levels[node]+1
                        # print(neighbour, ">>", levels[neighbour])
        return explored, levels

    explored, levels = bfs_connected_component(cast_associations, "Kevin Bacon")

    # Print top 10 results

    results = pd.DataFrame.from_dict(levels, orient='index')[0]
    results.name = "Actor"
    results.tail(10)
    # results.to_csv("bacon_number.csv")
