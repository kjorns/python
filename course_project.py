import nltk
import re
from nltk.tokenize import word_tokenize

# SOURCE ASSIGNMENT: SEARCH ALGORITHM IMPLEMENTATION
def binary_search(numbers, target):
    low, high = 0, len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = numbers[mid]

        if mid_element == target:
            return mid
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# SOURCE ASSIGNMENT: IMPLEMENTING A SEMANTIC NETWORK IN PYTHON
class SemanticNetwork:

    def __init__(self):
        self.network = {}
        self._initialize_knowledge_base()

    def add_node(self, node):
        if node not in self.network:
            self.network[node] = {}

    def add_relation(self, subject, relation, obj):
        if subject not in self.network:
            self.add_node(subject)
        if obj not in self.network:
            self.add_node(obj)

        if relation not in self.network[subject]:
            self.network[subject][relation] = []
        
        if obj not in self.network[subject][relation]:
            self.network[subject][relation].append(obj)

    def get_related(self, node, relation):
        return self.network.get(node, {}).get(relation, [])
    
    def display_network(self):
        print(f"{'Subject':<15} | {'Relation':<12} | {'Object'}")
        print("-" * 45)
        for subject, relations in self.network.items():
            for relation, objects in relations.items():
                for obj in objects:
                    print(f"{subject:<15} --[{relation:<10}]--> {obj}")

    def _initialize_knowledge_base(self):
        # TYPES
        self.add_relation("Bulbasaur", "is-a", "Grass-Type")
        self.add_relation("Bulbasaur", "is-a", "Poison-Type")
        self.add_relation("Ivysaur", "is-a", "Grass-Type")
        self.add_relation("Ivysaur", "is-a", "Poison-Type")
        self.add_relation("Venusaur", "is-a", "Grass-Type")
        self.add_relation("Venusaur", "is-a", "Poison-Type")
        self.add_relation("Charmander", "is-a", "Fire-Type")
        self.add_relation("Charmeleon", "is-a", "Fire-Type")
        self.add_relation("Charizard", "is-a", "Fire-Type")
        self.add_relation("Charizard", "is-a", "Flying-Type")
        self.add_relation("Squirtle", "is-a", "Water-Type")
        self.add_relation("Wartortle", "is-a", "Water-Type")
        self.add_relation("Blastoise", "is-a", "Water-Type")
        self.add_relation("Pikachu", "is-a", "Electric-Type")
        self.add_relation("Raichu", "is-a", "Electric-Type")
        self.add_relation("Eevee", "is-a", "Normal-Type")
        self.add_relation("Vaporeon", "is-a", "Water-Type")
        self.add_relation("Jolteon", "is-a", "Electric-Type")
        self.add_relation("Flareon", "is-a", "Fire-Type")

        # EVOLUTIONS
        self.add_relation("Bulbasaur", "evolves-to", "Ivysaur")
        self.add_relation("Ivysaur", "evolves-to", "Venusaur")
        self.add_relation("Charmander", "evolves-to", "Charmeleon")
        self.add_relation("Charmeleon", "evolves-to", "Charizard")
        self.add_relation("Squirtle", "evolves-to", "Wartortle")
        self.add_relation("Wartortle", "evolves-to", "Blastoise")
        self.add_relation("Pikachu", "evolves-to", "Raichu")
        self.add_relation("Eevee", "evolves-to", "Vaporeon")
        self.add_relation("Eevee", "evolves-to", "Jolteon")
        self.add_relation("Eevee", "evolves-to", "Flareon")

        # ABILITIES & WEAKNESSES ATTRIBUTES
        self.add_relation("Bulbasaur", "has-ability", "Overgrow")
        self.add_relation("Charmander", "has-ability", "Blaze")
        self.add_relation("Squirtle", "has-ability", "Torrent")
        self.add_relation("Pikachu", "has-ability", "Static")
        self.add_relation("Eevee", "has-ability", "Run Away")
        self.add_relation("Eevee", "has-ability", "Adaptability")
        self.add_relation("Grass-Type", "weak-to", "Fire-Type")
        self.add_relation("Fire-Type", "weak-to", "Water-Type")
        self.add_relation("Water-Type", "weak-to", "Grass-Type")
        self.add_relation("Water-Type", "weak-to", "Electric-Type")

    def find_matching_concept(self, query):
        from nltk.tokenize import word_tokenize
        tokens = word_tokenize(query.lower())

        # Sorted List
        concepts = sorted(list(self.network.keys()))

        for token in tokens:
            # Call Binary Search Function
            idx = binary_search(concepts, token.capitalize())
            if idx != -1:
                return concepts[idx]
        return None

# SOURCE ASSIGNENT: CHATBOT PROGRAM
class Chatbot:
    def __init__(self):
        self.semantic_network = SemanticNetwork()
        # Persona Responses
        self.persona_responses = {
            r'.*who made you.*': 'I was created by Kaitlyn Jorns for her AI class.',
            r'.*favorite color.*': 'Pink.',
            r'.*marvel.*': 'My favorite Marvel character is Wanda Maximoff, the Scarlet Witch.',
            r'.*star wars.*': 'My favorite Star Wars character is Anakin Skywalker.',
            r'.*hello|hi|hey.*': 'Hello! How can I help you today?'
        }
    
    def respond(self, query):
        # Check Persona Layer
        for pattern, response in self.persona_responses.items():
            if re.match(pattern, query, re.IGNORECASE):
                return response
            
        # Check Knowledge Layer
        concept = self.semantic_network.find_matching_concept(query)
        if concept:
            types = self.semantic_network.get_related(concept, "is-a")
            evolves = self.semantic_network.get_related(concept, "evolves-to")

            reply = f"I found {concept} in my database! "
            if types: reply += f"It is a {', '.join(types)} type. "
            if evolves: reply += f"It evolves into {', '.join(evolves)}."
            return reply
        
        return "Sorry, I didn't understand your query."

def main():
    nltk.download('punkt')  # Download necessary NLTK data
    nltk.download('punkt_tab') # I was getting an error, added this to fix it
    chatbot = Chatbot()

    chatbot.semantic_network.display_network()
    
    # Start conversation
    print("Chatbot: Hello! How can I assist you today? (Type 'quit' to stop)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()