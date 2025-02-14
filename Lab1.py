from queue import Queue, LifoQueue, PriorityQueue

class Nodo:
    def __init__(self, valor, costo=0):
        self.valor = valor
        self.costo = costo
        self.siguiente = None  

class ColaFIFO:
    def __init__(self):
        self.queue = []

    def empty(self):
        return len(self.queue) == 0

    def top(self):
        return self.queue[0] if not self.empty() else None

    def pop(self):
        return self.queue.pop(0) if not self.empty() else None

    def add(self, item):
        self.queue.append(item)

class PilaLIFO:
    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def top(self):
        return self.stack[-1] if not self.empty() else None

    def pop(self):
        return self.stack.pop() if not self.empty() else None

    def add(self, item):
        self.stack.append(item)

class ColaPrioridad:
    def __init__(self):
        self.pq = PriorityQueue()

    def empty(self):
        return self.pq.empty()

    def top(self):
        return self.pq.queue[0] if not self.empty() else None

    def pop(self):
        return self.pq.get() if not self.empty() else None

    def add(self, priority, item):
        self.pq.put((priority, item))

graph = {
    "Warm-up activities": [("Skipping Rope", 10), ("Exercise bike", 10), ("Tread Mill", 10), ("Step Mill", 10)],
    "Skipping Rope": [("Dumbbell", 15), ("Barbell", 15)],
    "Exercise bike": [("Cable-Crossover", 25)],
    "Tread Mill": [("Pulling Bars", 20), ("Incline Bench", 20)],
    "Step Mill": [("Incline Bench", 16)],
    "Dumbbell": [("Leg Press Machine", 12)],
    "Barbell": [("Leg Press Machine", 10)],
    "Cable-Crossover": [("Climbing Rope", 10)],
    "Pulling Bars": [("Climbing Rope", 6)],
    "Incline Bench": [("Hammer Strength", 20)],
    "Leg Press Machine": [("Stretching", 11)],
    "Climbing Rope": [("Stretching", 10)],
    "Hammer Strength": [("Stretching", 8)]
}

heuristic = {
    "Warm-up activities": 5,
    "Skipping Rope": 16,
    "Exercise bike": 10,
    "Tread Mill": 12,
    "Step Mill": 14,
    "Dumbbell": 9,
    "Barbell": 10,
    "Cable-Crossover": 8,
    "Pulling Bars": 10,
    "Incline Bench": 8,
    "Leg Press Machine": 8,
    "Climbing Rope": 5,
    "Hammer Strength": 4,
    "Stretching": 0
}

def breadth_first_search(start, goal, graph):
    stack = LifoQueue()
    stack.put((start, [start], 0))
    visited = set()

    while not stack.empty():
        node, path, cost = stack.get()
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph.get(node, []):
                stack.put((neighbor, path + [neighbor], cost + edge_cost))
    return None, float('inf')

def depth_first_search(start, goal, graph):
    queue = Queue()
    queue.put((start, [start], 0))  
    visited = set()

    while not queue.empty():
        node, path, cost = queue.get()
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph.get(node, []):
                queue.put((neighbor, path + [neighbor], cost + edge_cost)) 
    return None, float('inf')

def uniform_cost_search(start, goal, graph):
    pq = PriorityQueue()
    pq.put((0, start, [start]))
    visited = {}

    while not pq.empty():
        cost, node, path = pq.get()
        if node == goal:
            return path, cost
        if node not in visited or cost < visited[node]:
            visited[node] = cost
            for neighbor, edge_cost in graph.get(node, []):
                pq.put((cost + edge_cost, neighbor, path + [neighbor]))
    return None, float('inf')

def greedy_best_first_search(start, goal, graph, heuristic):
    pq = PriorityQueue()
    pq.put((heuristic.get(start, float('inf')), start, [start], 0)) 
    visited = set()

    while not pq.empty():
        _, node, path, cost = pq.get()
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph.get(node, []):
                pq.put((heuristic.get(neighbor, float('inf')), neighbor, path + [neighbor], cost + edge_cost)) 
    return None, float('inf')

def a_star_search(start, goal, graph, heuristic):
    pq = PriorityQueue()
    pq.put((heuristic.get(start, float('inf')), 0, start, [start]))
    visited = {}

    while not pq.empty():
        _, cost, node, path = pq.get()
        if node == goal:
            return path, cost
        if node not in visited or cost < visited[node]:
            visited[node] = cost
            for neighbor, edge_cost in graph.get(node, []):
                new_cost = cost + edge_cost
                pq.put((new_cost + heuristic.get(neighbor, float('inf')), new_cost, neighbor, path + [neighbor]))
    return None, float('inf')

start_node = "Warm-up activities"
goal_node = "Stretching"

bfs_path, bfs_cost = breadth_first_search(start_node, goal_node, graph)
dfs_path, dfs_cost = depth_first_search(start_node, goal_node, graph)
ucs_path, ucs_cost = uniform_cost_search(start_node, goal_node, graph)
gbfs_path, gbfs_cost = greedy_best_first_search(start_node, goal_node, graph, heuristic)
a_path, astar_cost = a_star_search(start_node, goal_node, graph, heuristic)

print("Para Breadth-first search:", bfs_path, "Costo:", bfs_cost)
print("Para Depth-first search:", dfs_path, "Costo:", dfs_cost)
print("Para Uniform-cost search:", ucs_path, "Costo:", ucs_cost)
print("Para Greedy Best-first search:", gbfs_path, "Costo:", gbfs_cost)
print("Para A*:", a_path, "Costo:", astar_cost)
