# Using Djikstra's algorithm, the code below is used to find the shortest route amongst cities. 

from collections import deque

class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Initialize the adjacency list graph with default roads (linear path)
        graph = {i: [i + 1] for i in range(n - 1)}  # Each city i has a road to i+1
        graph[n - 1] = []  # Last city has no outgoing roads

        result = []  # Store shortest path results after each query

        def bfs():
            """ Performs BFS to find the shortest path from city 0 to city (n-1). """
            queue = deque([(0, 0)])  # (current_city, current_distance)
            visited = set()

            while queue:
                city, distance = queue.popleft()
                if city == n - 1:
                    return distance  # Found the shortest path
                if city in visited:
                    continue
                visited.add(city)

                for neighbor in graph[city]:
                    if neighbor not in visited:
                        queue.append((neighbor, distance + 1))
            return float('inf')  # If no path found (shouldn't happen)

        # Step 2: Process each query and compute the shortest path after adding the road
        for u, v in queries:
            graph[u].append(v)  # Add new unidirectional road from u to v
            result.append(bfs())  # Compute the shortest path after adding the road

        return result

# Example test cases
solution = Solution()
print(solution.shortestDistanceAfterQueries(5, [[2,4],[0,2],[0,4]]))  # Output: [3,2,1]
print(solution.shortestDistanceAfterQueries(4, [[0,3],[0,2]]))  # Output: [1,1]
