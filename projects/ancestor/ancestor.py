class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_child(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_children(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def earliest(starting_node)
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
        while q.size() > 0:
            path = q.dequeue()
            current_node = path[-1]
            if current_node == destination_vertex:
                return path
            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.get_children(current_node)
                for neighbor in neighbors:
                    next_path = path + [neighbor]
                    q.enqueue(next_path)
                    
def earliest_ancestor(ancestors, starting_node):
    g = Graph
    for ancestor in ancestors:
        g.add_vertex(ancestor[0])
        g.add_child(ancestor[0], ancestor[1])