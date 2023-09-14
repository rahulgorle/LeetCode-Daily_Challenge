class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Construct a graph from tickets
        graph = {}
        for ticket in tickets:
            from_airport, to_airport = ticket
            if from_airport in graph:
                graph[from_airport].append(to_airport)
            else:
                graph[from_airport] = [to_airport]
        
        # Sort the destinations for each airport in lexical order
        for key in graph:
            graph[key].sort()
        
        # Initialize the result itinerary
        itinerary = []
        
        def dfs(node):
            # If the node is in the graph and has destinations
            if node in graph:
                destinations = graph[node]
                while destinations:
                    next_dest = destinations.pop(0)  # Get the smallest lexical destination
                    dfs(next_dest)  # Recursively visit the next destination
            itinerary.append(node)  # Add the node to the itinerary
        
        dfs("JFK")  # Start DFS from JFK
        
        # Reverse the itinerary to get the correct order
        return itinerary[::-1]
