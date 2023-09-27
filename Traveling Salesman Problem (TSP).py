import itertools

def calculate_total_distance(path, graph):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    return total_distance

def solve_tsp(graph):
    num_nodes = len(graph)
    if num_nodes < 2:
        return [0]

    # Inisialisasi node awal
    start_node = 0
    remaining_nodes = [i for i in range(num_nodes) if i != start_node]

    # Inisialisasi variabel untuk menyimpan solusi terbaik
    best_path = [start_node]
    best_distance = float('inf')

    # Gunakan itertools untuk menghasilkan semua kemungkinan permutasi node
    for perm in itertools.permutations(remaining_nodes):
        current_path = [start_node] + list(perm)
        current_distance = calculate_total_distance(current_path, graph)

        if current_distance < best_distance:
            best_path = current_path
            best_distance = current_distance

    return best_path, best_distance

# Contoh grafik untuk TSP
graph = [
    [0, 29, 20, 21],
    [29, 0, 15, 18],
    [20, 15, 0, 16],
    [21, 18, 16, 0]
]

best_path, best_distance = solve_tsp(graph)
print("Solusi TSP:")
print("Rute Terbaik:", best_path)
print("Jarak Terpendek:", best_distance)
