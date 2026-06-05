class SemanticNetwork:

    def __init__(self):
        self.network = {}  # Dictionary to store nodes and relationships

    def add_node(self, node):
        """Add a node (concept/entity) to the network."""
        if node not in self.network:
            self.network[node] = {}

    def add_relation(self, subject, relation, obj):
        """Add a relationship between two nodes."""
        if subject not in self.network:
            self.add_node(subject)
        if obj not in self.network:
            self.add_node(obj)

        if relation not in self.network[subject]:
            self.network[subject][relation] = []
        
        # Ensure the relationship is unique to avoid redundant data
        if obj not in self.network[subject][relation]:
            self.network[subject][relation].append(obj)

    def get_related(self, node, relation):
        """Retrieve related nodes based on a given relation."""
        return self.network.get(node, {}).get(relation, [])

    def display_network(self):
        """Print out the semantic network for visualization."""
        print(f"{'Subject':<15} | {'Relation':<12} | {'Object'}")
        print("-" * 45)
        for subject, relations in self.network.items():
            for relation, objects in relations.items():
                for obj in objects:
                    print(f"{subject:<15} --[{relation:<10}]--> {obj}")

# Example Usage - Pokemon
if __name__ == "__main__":
    sn = SemanticNetwork()
    
    # Adding nodes and relationships

    # Define Type Hierarchy (is-a)
    sn.add_relation("Bulbasaur", "is-a", "Grass-Type")
    sn.add_relation("Bulbasaur", "is-a", "Poison-Type")
    sn.add_relation("Ivysaur", "is-a", "Grass-Type")
    sn.add_relation("Ivysaur", "is-a", "Poison-Type")
    sn.add_relation("Venusaur", "is-a", "Grass-Type")
    sn.add_relation("Venusaur", "is-a", "Poison-Type")
    sn.add_relation("Charmander", "is-a", "Fire-Type")
    sn.add_relation("Charmeleon", "is-a", "Fire-Type")
    sn.add_relation("Charizard", "is-a", "Fire-Type")
    sn.add_relation("Charizard", "is-a", "Flying-Type")
    sn.add_relation("Squirtle", "is-a", "Water-Type")
    sn.add_relation("Wartortle", "is-a", "Water-Type")
    sn.add_relation("Blastoise", "is-a", "Water-Type")
    sn.add_relation("Pikachu", "is-a", "Electric-Type")
    sn.add_relation("Raichu", "is-a", "Electric-Type")
    sn.add_relation("Eevee", "is-a", "Normal-Type")
    sn.add_relation("Vaporeon", "is-a", "Water-Type")
    sn.add_relation("Jolteon", "is-a", "Electric-Type")
    sn.add_relation("Flareon", "is-a", "Fire-Type")

    # Define Evolution (evolves-to)
    sn.add_relation("Bulbasaur", "evolves-to", "Ivysaur")
    sn.add_relation("Ivysaur", "evolves-to", "Venusaur")
    sn.add_relation("Charmander", "evolves-to", "Charmeleon")
    sn.add_relation("Charmeleon", "evolves-to", "Charizard")
    sn.add_relation("Squirtle", "evolves-to", "Wartortle")
    sn.add_relation("Wartortle", "evolves-to", "Blastoise")
    sn.add_relation("Pikachu", "evolves-to", "Raichu")
    sn.add_relation("Eevee", "evolves-to", "Vaporeon")
    sn.add_relation("Eevee", "evolves-to", "Jolteon")
    sn.add_relation("Eevee", "evolves-to", "Flareon")

    # Define Ownership/Abilities (has-ability)
    sn.add_relation("Bulbasaur", "has-ability", "Overgrow")
    sn.add_relation("Charmander", "has-ability", "Blaze")
    sn.add_relation("Squirtle", "has-ability", "Torrent")
    sn.add_relation("Pikachu", "has-ability", "Static")
    sn.add_relation("Eevee", "has-ability", "Run Away")
    sn.add_relation("Eevee", "has-ability", "Adaptability")

    # Define Type Effectiveness (weak-to)
    sn.add_relation("Grass-Type", "weak-to", "Fire-Type")
    sn.add_relation("Fire-Type", "weak-to", "Water-Type")
    sn.add_relation("Water-Type", "weak-to", "Grass-Type")
    sn.add_relation("Water-Type", "weak-to", "Electric-Type")

    # Display the semantic network
    sn.display_network()

    # Query relationships

    # Query: What is Bulbasaur?
    types = sn.get_related("Bulbasaur", "is-a")
    print(f"Bulbasaur Type(s): {', '.join(types)}")

    # Query: What are Eevee's evolutions?
    eeveelutions = sn.get_related("Eevee", "evolves-to")
    print(f"Eevee Evolution: {', '.join(eeveelutions)}")

    # Query: Strategic Weaknesses
    weaknesses = sn.get_related("Water-Type", "weak-to")
    print(f"Water-Type Weaknesses: {', '.join(weaknesses)}")