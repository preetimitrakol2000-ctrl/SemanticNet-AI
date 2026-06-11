from graph_node import ConceptNode
from inference import SemanticGraph

if __name__ == "__main__":
    print("🧠 Initializing SemanticNet-AI Knowledge Inference Layer...")
    
    net = SemanticGraph()
    
    c1 = ConceptNode("Convolutional_Layer")
    c2 = ConceptNode("Neural_Network")
    c3 = ConceptNode("Artificial_Intelligence")

    # Construct explicit logical dependencies
    net.connect_concepts(c1, c2, "PART_OF")
    net.connect_concepts(c2, c3, "IS_A")

    query_start = "Convolutional_Layer"
    query_end = "Artificial_Intelligence"
    
    is_related = net.trace_relation_path(query_start, query_end)
    
    print(f"📊 Querying Graph: Does [{query_start}] structurally connect to [{query_end}]?")
    print(f"🔮 Inference Result: {'ASSERTION VERIFIED ✅' if is_related else 'NO PATH DETECTED ❌'}")
