import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate
from colorama import init, Fore

init(autoreset=True)

def build_graph():
    G = nx.DiGraph()
    edges = [
        ("Термінал 1", "Склад 1", 25),
        ("Термінал 1", "Склад 2", 20),
        ("Термінал 1", "Склад 3", 15),
        ("Термінал 2", "Склад 3", 15),
        ("Термінал 2", "Склад 4", 30),
        ("Термінал 2", "Склад 2", 10),
        ("Склад 1", "Магазин 1", 15),
        ("Склад 1", "Магазин 2", 10),
        ("Склад 1", "Магазин 3", 20),
        ("Склад 2", "Магазин 4", 15),
        ("Склад 2", "Магазин 5", 10),
        ("Склад 2", "Магазин 6", 25),
        ("Склад 3", "Магазин 7", 20),
        ("Склад 3", "Магазин 8", 15),
        ("Склад 3", "Магазин 9", 10),
        ("Склад 4", "Магазин 10", 20),
        ("Склад 4", "Магазин 11", 10),
        ("Склад 4", "Магазин 12", 15),
        ("Склад 4", "Магазин 13", 5),
        ("Склад 4", "Магазин 14", 10),
    ]
    for u, v, capacity in edges:
        G.add_edge(u, v, capacity=capacity)
    return G

def calculate_max_flow(G, source, sink):
    return nx.maximum_flow(G, source, sink)

def visualize_graph(G):
    pos = nx.spring_layout(G, seed=42)
    labels = nx.get_edge_attributes(G, "capacity")
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", edge_color="gray", font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Граф логістичної мережі")
    plt.show()

def main():
    G = build_graph()
    sources = ["Термінал 1", "Термінал 2"]
    sinks = [f"Магазин {i}" for i in range(1, 15)]
    
    max_flow_value = 0
    final_flow = {}
    
    for source in sources:
        for sink in sinks:
            flow_value, _ = calculate_max_flow(G, source, sink)
            max_flow_value += flow_value
            final_flow[(source, sink)] = flow_value
    
    print(Fore.GREEN + f"\nМаксимальний потік у мережі: {max_flow_value}")
    
    rows = [[src, sink, flow] for (src, sink), flow in final_flow.items() if flow > 0]
    print(Fore.CYAN + "\nТаблиця розподілу потоків:")
    print(tabulate(rows, headers=["Термінал", "Магазин", "Фактичний потік (од.)"], tablefmt="grid"))
    
    visualize_graph(G)

if __name__ == "__main__":
    main()
