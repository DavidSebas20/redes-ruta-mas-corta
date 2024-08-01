import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ruta Más Corta en un Grafo")
        
        self.graph = nx.Graph()
        
        # GUI Elements
        self.node_label = tk.Label(root, text="Nodo:")
        self.node_label.grid(row=0, column=0)
        self.node_entry = tk.Entry(root)
        self.node_entry.grid(row=0, column=1)
        
        self.connection_label = tk.Label(root, text="Conexión (Nodo1 Nodo2 Distancia):")
        self.connection_label.grid(row=1, column=0)
        self.connection_entry = tk.Entry(root)
        self.connection_entry.grid(row=1, column=1)
        
        self.add_node_button = tk.Button(root, text="Agregar Nodo", command=self.add_node)
        self.add_node_button.grid(row=0, column=2)
        
        self.add_connection_button = tk.Button(root, text="Agregar Conexión", command=self.add_connection)
        self.add_connection_button.grid(row=1, column=2)
        
        self.connections_listbox = tk.Listbox(root, height=10, width=50)
        self.connections_listbox.grid(row=2, column=0, columnspan=3)
        
        self.start_node_label = tk.Label(root, text="Nodo Inicio:")
        self.start_node_label.grid(row=3, column=0)
        self.start_node_entry = tk.Entry(root)
        self.start_node_entry.grid(row=3, column=1)
        
        self.end_node_label = tk.Label(root, text="Nodo Fin:")
        self.end_node_label.grid(row=4, column=0)
        self.end_node_entry = tk.Entry(root)
        self.end_node_entry.grid(row=4, column=1)
        
        self.shortest_path_button = tk.Button(root, text="Mostrar Ruta Más Corta", command=self.show_shortest_path)
        self.shortest_path_button.grid(row=5, column=1)
        
        self.result_text = tk.Text(root, height=5, width=50)
        self.result_text.grid(row=6, column=0, columnspan=3)
    
    def add_node(self):
        node = self.node_entry.get()
        if node:
            self.graph.add_node(node)
            self.node_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Ingrese un nodo válido.")
    
    def add_connection(self):
        connection = self.connection_entry.get()
        try:
            node1, node2, distance = connection.split()
            distance = float(distance)
            self.graph.add_edge(node1, node2, weight=distance)
            self.connection_entry.delete(0, tk.END)
            
            # Update listbox with new connection
            self.connections_listbox.insert(tk.END, f"{node1} - {node2}: {distance}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese una conexión válida en el formato 'Nodo1 Nodo2 Distancia'.")
    
    def show_shortest_path(self):
        start_node = self.start_node_entry.get()
        end_node = self.end_node_entry.get()
        if start_node in self.graph.nodes and end_node in self.graph.nodes:
            try:
                shortest_path = nx.dijkstra_path(self.graph, start_node, end_node)
                path_length = nx.dijkstra_path_length(self.graph, start_node, end_node)
                
                
                # Display shortest path details
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, f"Ruta más corta: {' -> '.join(shortest_path)}\n")
                self.result_text.insert(tk.END, f"Distancia total: {path_length}")

                self.plot_graph(shortest_path)
            except nx.NetworkXNoPath:
                messagebox.showerror("Error", f"No hay camino entre {start_node} y {end_node}.")
        else:
            messagebox.showerror("Error", "Ingrese nodos válidos de inicio y fin.")
    
    def plot_graph(self, shortest_path):
        pos = nx.spring_layout(self.graph)
        plt.figure()
        
        # Draw the graph
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
        
        # Highlight the shortest path
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_nodes(self.graph, pos, nodelist=shortest_path, node_color='orange')
        nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges, edge_color='red', width=2)
        
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
