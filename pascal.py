def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = []
        print r
        for c in range(0, r+1):
            upleft = rows[r - 1][c - 1] if c > 0 else 0
            print r-1,c
            upright = rows[r - 1][c] if c < r else 0
            print upleft+upright
            row.append(upleft + upright)       
        rows.append(row)
        print rows
    return rows
