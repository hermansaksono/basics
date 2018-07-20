def get_route(source, dest, graph):
    # type: (str, str, list[str]) -> list[str]
    if source == dest:
        return [dest]
    else:
        neighbors = get_neighbors(source, graph)
        candidate = get_sub_route(neighbors, dest, graph)
        if not candidate:
            return False
        else:
            return [source] + candidate


def get_sub_route(list_of_sources, dest, graph):
    # type: (list[str], str, list[str]) -> list[str]
    if len(list_of_sources) == 0:
        return False
    else:
        candidate = get_route(list_of_sources[0], dest, graph)
        if candidate is not False:
            return candidate
        else:
            return get_sub_route(list_of_sources[1:], dest, graph)


def get_neighbors(node, graph):
    # type: (str, list[str]) -> list[str]
    neighbors = []
    for edge in graph:
        if edge[0] == node:
            neighbors.append(edge[1])
    return neighbors
