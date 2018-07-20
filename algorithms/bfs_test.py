from bfs import get_route as bfs_get_route

# A Node is an str
# An Edge is a tuple(Node, Node)
# A Graph is a list(Edge)

example_graph = [
    ("A", "B"),
    ("A", "E"),
    ("B", "E"),
    ("B", "F"),
    ("C", "D"),
    ("E", "C"),
    ("E", "F"),
    ("F", "G")]

print(bfs_get_route("A", "G", example_graph))