def draw_xyz(N):
    pattern = ""
    for i in range(N):
        row = []
        for j in range(N):
            # Hitung urutan dari 1 hingga N*N
            num = i * N + j + 1

            if num % 3 == 0:
                row.append("X")
            elif num % 2 == 0:
                row.append("Z")
            else:
                row.append("Y")
        
        pattern += " ".join(row) + " \n"
    
    return pattern

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """