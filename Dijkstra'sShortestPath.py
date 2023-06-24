import math

def dijkstra(graph, start):
    tentative = {}
    confirmed = {}
    confirmed[start] = 0

    for node, distance in graph[start].items():
        tentative[node] = distance
        next = start
    
    while tentative:
        shortest_distance = math.inf
        for node, distance in tentative.items():
            if distance < shortest_distance:
                shortest_distance = distance
            next = node

    confirmed[next] = shortest_distance
    tentative.pop(next)

    for node, distance in graph[start].items():
        cost = confirmed[next] + distance

        if node in confirmed:
            continue
        elif (node in tentative) and (cost < tentative[node]):
            tentative[node] = cost
        elif node not in tentative:
            tentative[node] = cost

    return confirmed



def main():
    
    graph = {
        'A': {'B': 5, 'C' : 10},
        'B': {'A': 5, 'C': 3, 'D': 11},
        'C': {'A' : 10, 'B': 3, 'D': 2},
        'D': {'B': 11, 'C': 2}
    }
    start = 'D'

    distances = dijkstra(graph, start)

    for node, distance in distances.items():
        print (f"{node} -> {distance}")
    

main()