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

def compute_number_neighbors(paded_frame, index_line, index_column):
    """
    Cette fonction prend en entrée la matrice avec bordure et
    renvoie le nombre de cellules voisines vivantes.
    """
    neighbors_count = 0
    
    for i in range(index_line - 1, index_line + 2):
        for j in range(index_column - 1, index_column + 2):
            if i == index_line and j == index_column:
                continue  # pass pour la cellule 
            neighbors_count += paded_frame[i, j]  # 1 = vivant, 0 si mort)
    
    return neighbors_count

def compute_next_frame(frame):
    """
    Cette fonction prend en entrée une frame et calcule la frame suivante
    à partir des règles du jeu de la vie
    """
    paded_frame = np.pad(frame, 1, mode="constant") # je vous offre le code pour le zéro padding c'est cadeau !
    next_frame = frame.copy()

    # Étape 1 : 2 boucles for imbriquées pour parcourir la matrice avec bordure (zero padding) élément par élément.
    # Faites attention à l'index de début et d'arrêt ! (il s'agit de la matrice avec bordure)
    for row in range(1, paded_frame.shape[0] - 1):
        for col in range(1, paded_frame.shape[1] - 1):
            
            # Étape 2 : Pour chacun des éléments, calculez le nombre de voisins.
            num_neighbors = compute_number_neighbors(paded_frame, row, col)
            
            # Étape 3 : Pour chacun des éléments, faire les tests (état de l'élément et son nombre de voisins)
            # afin de voir s'il y a des modifications à faire.
            # Si c'est le cas, effectuez les modifications directement dans la matrice `next_frame` (Attention à l'indice utilisé !)
            if paded_frame[row, col] == 1:  
                if num_neighbors not in [2, 3]:
                    next_frame[row - 1, col - 1] = 0  # kill
            else:  
                if num_neighbors == 3:
                    next_frame[row - 1, col - 1] = 1  

    return next_frame

while True:
    print(frame)
    frame = compute_next_frame(frame)