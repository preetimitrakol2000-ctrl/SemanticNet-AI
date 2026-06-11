class ConceptNode:
    def __init__(self, name):
        self.name = name

class RelationshipEdge:
    def __init__(self, target_node, predicate):
        self.target = target_node
        self.predicate = predicate  # e.g., "IS_A", "PART_OF"
