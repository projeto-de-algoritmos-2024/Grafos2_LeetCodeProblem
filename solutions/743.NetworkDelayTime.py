from typing import List
import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Construir o grafo como um dicionário de adjacência
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Inicializa a min-heap
        djk_HEAP = [(0, k)]  # (custo, nó atual)
        djk_SET = {}
        
        # Enquanto a fila não estiver vazia
        while djk_HEAP:
            custo, no_atual = heapq.heappop(djk_HEAP)
            
            # Se o nó já está na mancha continua
            if no_atual in djk_SET:
                continue
            
            # Registra a distância de menor custo para o nó
            djk_SET[no_atual] = custo
            
            # Insere arestas vizinhas na HEAP
            for neighbor, weight in graph[no_atual]:
                if neighbor not in djk_SET:
                    heapq.heappush(djk_HEAP, (custo + weight, neighbor))
        
        # Se todos os nós foram alcançados, retorna o custo
        if len(djk_SET) == n:
            return max(djk_SET.values())
        return -1