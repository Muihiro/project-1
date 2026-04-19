def copy_matrix(matrix):
    return [row[:] for row in matrix]

def get_determinant(matrix):
    n = len(matrix)
    mat = copy_matrix(matrix)
    det = 1.0
    for i in range(n):
        pivot_row = max(range(i, n), key=lambda r: abs(mat[r][i]))
        if pivot_row != i:
            mat[i], mat[pivot_row] = mat[pivot_row], mat[i]
            det *= -1
        if abs(mat[i][i]) < 1e-9:
            return 0.0
        det *= mat[i][i]
        for j in range(i + 1, n):
            factor = mat[j][i] / mat[i][i]
            for k in range(i, n):
                mat[j][k] -= factor * mat[i][k]
    return det


def replace_column(matrix, col_idx, new_col):
    return [row[:col_idx] + [new_col[i]] + row[col_idx + 1:] for i, row in enumerate(matrix)]

def solve_cramer(A, b):
    det_A = get_determinant(A)
    if abs(det_A) < 1e-9:
        return False, None
    return True, [get_determinant(replace_column(A, i, b)) / det_A for i in range(len(A))]

def solve_gauss(A, b):
    n = len(A)
    aug = [A[i] + [b[i]] for i in range(n)]

    for i in range(n):
        pivot_row = max(range(i, n), key=lambda r: abs(aug[r][i]))
        aug[i], aug[pivot_row] = aug[pivot_row], aug[i]
        if abs(aug[i][i]) < 1e-9:
            continue
        pivot = aug[i][i]
        for j in range(i + 1, n):
            factor = aug[j][i] / pivot
            for k in range(i, n + 1):
                aug[j][k] -= factor * aug[i][k]

    solution = [0.0] * n
    has_free = False
    for i in range(n - 1, -1, -1):
        if all(abs(aug[i][j]) < 1e-9 for j in range(n)):
            if abs(aug[i][n]) > 1e-9:
                return 'нет решений', None
            has_free = True
            continue

        val = aug[i][n]
        for j in range(i + 1, n):
            val -= aug[i][j] * solution[j]
        solution[i] = val / aug[i][i] if abs(aug[i][i]) > 1e-9 else 0.0

    return ('infinite' if has_free else 'unique'), solution


def solve_slae_smart(A, b):
    n = len(A)

    success, sol = solve_cramer(A, b)
    if success:
        return "единственное решение (крамер)", sol

    status, sol = solve_gauss(A, b)
    if status == 'нет решений':
        return "нет решений (система несовместна)", None
    elif status == 'infinite':
        return "бесконечно много решений", sol
    return "единственное решение (гаусс)", sol


def print_solution(status, solution):
    print(f"\nстатус: {status}")
    if solution is not None:
        print("решение:")
        for i, val in enumerate(solution):
            print(f"  x[{i}] = {val:.6f}")
    else:
        print("решение: отсутствует")


if __name__ == "__main__":
    A1 = [[2, -3, -1],
          [4, -6, 2],
          [1, 9, 4]]

    b1 = [2, 4, 1]
    print_solution(*solve_slae_smart(A1, b1))