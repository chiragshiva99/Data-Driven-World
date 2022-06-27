graph = {
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["D"],
    "D": ["C"],
    "E": ["F"],
    "F": ["C"]
}


def get_neighbours(graph, vert):
    result = graph.get(vert, None)
    return result


def get_source(graph, vert):
    result = []
    for (k, v) in graph.items():
        if vert in v:
            result.append(k)
    return result


assert get_neighbours(graph, "B") == ["C", "D"]
assert sorted(get_source(graph, "C")) == ["A", "B", "D", "F"]