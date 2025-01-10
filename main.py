import numpy as np

# Grille depart (7x7)
frame = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
])

def compute_number_neighbors(padded_frame, index_line, index_column):
    """
    Cette fonction prend en entrée la matrice avec bordure et
    renvoie le nombre de cellules voisines vivantes.
    """
    neighbors_count = 0
    
    for i in range(index_line - 1, index_line + 2):
        for j in range(index_column - 1, index_column + 2):
            if i == index_line and j == index_column:
                continue  # pass pour la cellule 
            neighbors_count += padded_frame[i, j]  # 1 = vivant, 0 si mort)
    
    return neighbors_count


print(frame)
