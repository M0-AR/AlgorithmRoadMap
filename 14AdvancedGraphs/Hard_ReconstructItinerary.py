# T: O(v^2) S: O(n)
def find_itinerary(tickets):
    # Map every source node to an empty list
    adj = {src: [] for src, dst in tickets}

    # Sort
    tickets.sort()

    # Build adj list
    for src, dst in tickets:
        adj[src].append(dst)

    # Starting point of list
    res = ["JFK"]

    def dfs(src):
        # When result is equal to tickets + 1 so we reach to the result
        if len(res) == len(tickets) + 1:
            return True
        # The source has not any outgoing source from it
        if src not in adj:
            return False

        temp = list(adj[src])
        # Enumerate let us iterate at the index and value at the same time
        for i, v in enumerate(temp):
            adj[src].pop(i)
            res.append(v)

            # We are looking for just one path so we return true when we find a path
            if dfs(v): return True

            adj[src].insert(i, v)
            res.pop()
            return False

    dfs(res[0])
    return res


print(find_itinerary(
    [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))  # Output: ["JFK","MUC","LHR","SFO","SJC"]

print(find_itinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"],
                      ["ATL", "SFO"]]))  # Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
