import heapq

class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        # Fila de prioridade (min-heap)
        # Elemento da fila: (distância, x, y, obstáculos eliminados)
        heap = [(0, 0, 0, 0)]  # Começamos com a posição (0, 0), 0 passos, 0 obstáculos eliminados
        # Visitação: uma matriz para guardar o menor número de obstáculos eliminados para um par (x, y)
        visitado = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(m)]
        visitado[0][0][0] = 0
        
        # Direções de movimento: Cima, Baixo, Esquerda, Direita
        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while heap:
            passos, x, y, obstaculos = heapq.heappop(heap)
            
            # Se chegamos no final, retornamos a distância
            if x == m - 1 and y == n - 1:
                return passos
            
            # Verificar as 4 direções
            for dx, dy in direcoes:
                nx, ny = x + dx, y + dy
                
                # Verifica se a nova posição está dentro dos limites da matriz
                if 0 <= nx < m and 0 <= ny < n:
                    novos_obstaculos = obstaculos + grid[nx][ny]
                    
                    # Se não houver mais obstáculos ou se podemos eliminar um obstáculo
                    if novos_obstaculos <= k and visitado[nx][ny][novos_obstaculos] > passos + 1:
                        visitado[nx][ny][novos_obstaculos] = passos + 1
                        heapq.heappush(heap, (passos + 1, nx, ny, novos_obstaculos))
        
        # Se não foi possível alcançar o destino
        return -1

if __name__ == "__main__":
    solution = Solution()
    
    # Exemplo 1
    grid1 = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
    k1 = 1
    print("Exemplo 1:", solution.shortestPath(grid1, k1))

    # Exemplo 2
    grid2 = [[0,1,1],[1,1,1],[1,0,0]]
    k2 = 1
    print("Exemplo 2:", solution.shortestPath(grid2, k2))
