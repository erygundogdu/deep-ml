def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    pass
    r = len(a)
    c = len(a[0])
    col_lst = []
    for i in range(c):
        col = []
        for k in range(r):
            val = a[k][i]
            col.append(val)
        col_lst.append(col)

    return col_lst