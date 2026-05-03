from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # DFS with Recursion
        # if source == destination:
        #     return True
        
        # graph = defaultdict(list)
        # for u,v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)
        
        # seen = set()
        # seen.add(source)

        # def dfs(i):
        #     if i == destination:
        #         return True
            
        #     for nei_node in graph[i]:
        #         if nei_node not in seen:
        #             seen.add(nei_node)
        #             if dfs(nei_node):
        #                 return True
        #     return False
        
        # return dfs(source)


        # DFS with Stack

        # if source == destination:
        #     return True
        
        # graph = defaultdict(list)
        # for u,v in edges:
        #     graph[v].append(u)
        #     graph[u].append(v)
        
        # seen = set()
        # seen.add(source)
        # stack = [source]

        # while stack:
        #     node = stack.pop()
        #     if node == destination:
        #         return True
        #     for nei_node in graph[node]:
        #         if nei_node not in seen:
        #             seen.add(nei_node)
        #             stack.append(nei_node)
        # return False


        # BFS with deque

        if source == destination:
            return True
        
        graph = defaultdict(list)
        for u,v in edges:
            graph[v].append(u)
            graph[u].append(v)
        
        seen = set()
        seen.add(source)
        q = deque()
        q.append(source)

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for nei_node in graph[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    q.append(nei_node)
        
        return False