import heapq

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Número de pontos
        n = len(points)
        
        # Função para calcular a distância de Manhattan entre dois pontos
        def distancia_manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        # Fila de prioridade para gerenciar arestas
        min_heap = []
        
        # Nós já incluídos na MST
        MST = [False] * n
        
        # Começamos com o nó 0
        min_heap.append((0, 0))
        
        custo_total = 0
        arestas_usadas = 0
        
        while arestas_usadas < n:
            # Pegar a aresta de menor custo
            custo, curr = heapq.heappop(min_heap)
            
            # Se o nó já está na MST, ignorar
            if MST[curr]:
                continue
            
            # Adiciona o nó à MST
            MST[curr] = True
            custo_total += custo
            arestas_usadas += 1
            
            # Explorar os vizinhos do nó atual
            for prox_no in range(n):
                if not MST[prox_no]:
                    prox_custo = distancia_manhattan(points[curr], points[prox_no])
                    heapq.heappush(min_heap, (prox_custo, prox_no))
        
        return custo_total

# Testes locais
if __name__ == "__main__":
    solution = Solution()
    
    # Exemplo 1
    pontos1 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print("Exemplo 1:", solution.minCostConnectPoints(pontos1))

    # Exemplo 2
    pontos2 = [[3, 12], [-2, 5], [-4, 1]]
    print("Exemplo 2:", solution.minCostConnectPoints(pontos2))

