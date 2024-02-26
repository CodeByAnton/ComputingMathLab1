from gauss import GaussSolver

solver = GaussSolver()

solver.input_matrix()

solver.gaussian_elimination()

solver.print_triangular_matrix()

solver.print_solution()

solver.print_residuals()

solver.print_determinant()


# Использовнаие библиотек
print("\n-------------------------Результаты вычислени, полученные при помощи библиотеки numpy--------------\n")
solver.gaussian_elimination_by_lib()
flag_diff = True
if isinstance(solver.solution, float):
    for i in range(solver.n):
        if abs(solver.solution[i] - solver.lib_solution[i]) > 0.0000001:
            flag_diff = False

print("\nОтветы, полученные обоими методы идентичны" if flag_diff else "Ответы различны")
