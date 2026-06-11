class SemanticGraph:
    def __init__(self):
        self.adjacency_list = {}

    def insert_concept(self, concept):
        if concept.name not in self.adjacency_list:
            self.adjacency_list[concept.name] = []

    def connect_concepts(self, source, target, predicate):
        self.insert_concept(source)
        self.insert_concept(target)
        self.adjacency_list[source.name].append((target, predicate))

    def trace_relation_path(self, start_name, target_name, visited=None):
        """Depth-First Search mapping logic to isolate deductive inferences."""
        if visited is None:
            visited = set()
        if start_name == target_name:
            return True

        visited.add(start_name)
        for neighbor_node, predicate in self.adjacency_list.get(start_name, []):
            if neighbor_node.name not in visited:
                if self.trace_relation_path(neighbor_node.name, target_name, visited):
                    return True
        return False
