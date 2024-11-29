import heapq
from typing import List

class Graph:

    def __init__(self, n: int, edges: List[List[int]]) -> None:
        self.n = n
        self.graph = [[] for _ in range(n)]  # Lista de adjacência
        
        for from_node, to_node, cost in edges:
            self.graph[from_node].append((to_node, cost))
    
    def addEdge(self, edge: List[int]) -> None:
        from_node, to_node, cost = edge
        self.graph[from_node].append((to_node, cost))
    
    def shortestPath(self, no_inicio: int, no_dest: int) -> int: 
        
        # Inicializa a min-heap
        djk_HEAP = [(0, no_inicio)] 
        djk_SET = [float('inf')] * self.n 
        djk_SET[no_inicio] = 0 
        
        # Enquanto a fila não estiver vazia
        while djk_HEAP:
            custo_no_atual, no_atual = heapq.heappop(djk_HEAP)
            
            if no_atual == no_dest:
                return custo_no_atual
            
            if custo_no_atual > djk_SET[no_atual]: # Existe opção melhor
                continue  
            
            # Insere arestas vizinhas na HEAP
            for neighbor, cost in self.graph[no_atual]:
                new_dist = custo_no_atual + cost
                if new_dist < djk_SET[neighbor]:
                    djk_SET[neighbor] = new_dist
                    heapq.heappush(djk_HEAP, (new_dist, neighbor))
        
        return -1 