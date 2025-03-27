import tkinter as tk
from tkinter import messagebox
from queue import PriorityQueue

# Définir la grille
grid = [
    ['S', ' ', ' ', ' '],
    [' ', '😊', ' ', ' '],
    [' ', ' ', '😊', ' '],
    [' ', ' ', ' ', '✅']
]

# Taille de chaque cellule dans la grille
cell_size = 50

# Position initiale de l'agent (Start) et position du trésor (Goal)
start = (0, 0)
goal = (3, 3)

# Fonction pour calculer la distance de Manhattan (heuristique pour A*)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Algorithme A* pour trouver le chemin optimal
def a_star(grid, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        _, current = frontier.get()

        if current == goal:
            break

        for next in get_neighbors(current):
            new_cost = cost_so_far[current] + 1  # Coût de déplacement = 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put((priority, next))
                came_from[next] = current

    # Reconstruire le chemin optimal
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# Fonction pour obtenir les voisins valides d'une cellule
def get_neighbors(cell):
    x, y = cell
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Haut, Bas, Gauche, Droite
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '😊':
            neighbors.append((nx, ny))
    return neighbors

# Fonction pour afficher la grille avec Tkinter
def draw_grid(canvas, grid, path):
    canvas.delete("all")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            x0, y0 = j * cell_size, i * cell_size
            x1, y1 = x0 + cell_size, y0 + cell_size
            canvas.create_rectangle(x0, y0, x1, y1, outline="black")
            if (i, j) == start:
                canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text="S", font=("Arial", 20))
            elif (i, j) == goal:
                canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text="✅", font=("Arial", 20))
            elif grid[i][j] == '😊':
                canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text="😊", font=("Arial", 20))
            elif (i, j) in path:
                canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text="•", font=("Arial", 20))

# Fonction pour lancer la recherche du chemin optimal
def find_optimal_path():
    path = a_star(grid, start, goal)
    if path:
        draw_grid(canvas, grid, path)
        messagebox.showinfo("Chemin optimal", f"Chemin trouvé! Longueur du chemin : {len(path) - 1}")
    else:
        messagebox.showinfo("Chemin optimal", "Aucun chemin trouvé.")

# Initialisation de Tkinter
root = tk.Tk()
root.title("Chemin Optimal avec A*")

canvas = tk.Canvas(root, width=len(grid[0]) * cell_size, height=len(grid) * cell_size)
canvas.pack()

# Bouton pour lancer la recherche du chemin optimal
find_path_button = tk.Button(root, text="Trouver le chemin optimal", command=find_optimal_path)
find_path_button.pack()

# Afficher la grille initiale
draw_grid(canvas, grid, [])

# Lancer l'application
root.mainloop()