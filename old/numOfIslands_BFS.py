class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        v = m*n

        graph = [[] for i in range(v)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    graph[self.__getIndex(n,i,j)] += [-1]
                    if i > 0 and grid[i-1][j] == "1":
                        self.__connect(graph,n,i,j,i-1,j)
                    if j > 0 and grid[i][j-1] == "1":
                        self.__connect(graph,n,i,j,i,j-1)
        return self.__bfs(graph)

    def __getIndex(self, n, i, j):
        return n*i + j

    def __connect(self, graph,n , r1, c1, r2, c2):
        graph[self.__getIndex(n,r1,c1)] += [self.__getIndex(n,r2,c2)]
        graph[self.__getIndex(n,r2,c2)] += [self.__getIndex(n,r1,c1)]

    def __bfs(self,graph):
        counter = 0
        for v in graph:
            if len(v) > 0:
                counter += 1
                e = 1
                while True:
                    if e >= len(v):
                        break

                    if v[e] == -1:
                        e += 1
                        continue

                    v += graph[v[e]]
                    graph[v[e]] = []
                    e += 1

        return counter

sol = Solution()
grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
print(sol.numIslands(grid))