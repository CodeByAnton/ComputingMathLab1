import numpy as np


class GaussSolver:
    def __init__(self):
        self.n = None
        self.matrix = []
        self.vector = []
        self.solution = []
        self.residuals = []
        self.det = None
        self.lib_solution = []
        self.lib_residuals = []
        self.lib_det = None

    def input_from_console(self):
        try:
            self.n = int(input("Введите размерность матрицы:\n "))
            print("Введите элементы матрицы построчно:")
            for _ in range(self.n):
                row = list(map(float, input().split()))
                self.matrix.append(row)
            print("Введите элементы вектора правых частей:")
            self.vector = list(map(float, input().split()))
        except ValueError:
            print("Входные данные должны быть только числами")

    def input_matrix(self):
        input_stream = input("Укажите источник данных (file(f) или console(c)):\n ").strip()
        if input_stream == "console" or input_stream == "c":
            self.input_from_console()
        elif input_stream == "file" or input_stream == "f":
            file_name = input("Введите имя файла:\n ")
            self.input_from_file(file_name)
        else:
            print("Некорректный ввод источника данных.")

    def input_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                self.n = int(lines[0])  # Считываем размерность матрицы из первой строки файла
                for line in lines[1:]:  # Начинаем считывать саму матрицу со второй строки
                    row = list(map(float, line.split()))
                    self.matrix.append(row[:-1])
                    self.vector.append(row[-1])
                # Проверяем, что количество строк матрицы соответствует указанной размерности
                if len(self.matrix) != self.n:
                    print("Неверное количество строк в матрице.")
                    return
        except FileNotFoundError:
            print("Файл не найден.")

    def gaussian_elimination(self):
        n = len(self.matrix)
        # Прямой ход
        for i in range(n):
            max_row = i
            for j in range(i + 1, n):
                if abs(self.matrix[j][i]) > abs(self.matrix[max_row][i]):
                    max_row = j
            if max_row != i:
                self.matrix[i], self.matrix[max_row] = self.matrix[max_row], self.matrix[i]
                self.vector[i], self.vector[max_row] = self.vector[max_row], self.vector[i]

            if abs(self.matrix[i][i]) < 1e-10:  # Проверка на нулевой коэффициент
                break

            for j in range(i + 1, n):
                factor = self.matrix[j][i] / self.matrix[i][i]
                for k in range(i, n):
                    self.matrix[j][k] -= factor * self.matrix[i][k]
                self.vector[j] -= factor * self.vector[i]

        if abs(self.matrix[n - 1][n - 1]) < 1e-10:  # Проверка на нулевой последний элемент в диагонали

            if abs(self.vector[n - 1]) < 1e-10:  # Проверка на нулевой правый член
                self.solution = "Система уравнений имеет бесконечное количество решений."

            else:
                self.solution = "Система уравнений не имеет решений."
            return

        self.det = 1
        for i in range(n):
            self.det *= self.matrix[i][i]

        # Обратный ход
        self.solution = [0] * n
        for i in range(n - 1, -1, -1):
            self.solution[i] = self.vector[i]
            for j in range(i + 1, n):
                self.solution[i] -= self.matrix[i][j] * self.solution[j]
            self.solution[i] /= self.matrix[i][i]

        # Вектор невязок
        self.residuals = [0] * n
        for i in range(n):
            self.residuals[i] = sum(self.matrix[i][j] * self.solution[j] for j in range(n)) - self.vector[i]

    def gaussian_elimination_by_lib(self):
        augmented_matrix = np.column_stack((self.matrix, self.vector))
        try:
            self.lib_solution = np.linalg.solve(self.matrix, self.vector)
            self.lib_det = np.linalg.det(self.matrix)
            print("\nРешение системы:")
            print(' '.join(f"{i:7.7f}" for i in self.lib_solution))
            print("\nОпределитель матрицы:")
            print(f"{self.lib_det:7.7f}")


        except np.linalg.LinAlgError as e:
            if 'Singular matrix' in str(e):
                if np.linalg.matrix_rank(self.matrix) < np.linalg.matrix_rank(augmented_matrix):
                    print("Система уравнений не имеет решений.")

                else:
                    print("Система уравнений имеет бесконечное количество решений.")

            else:
                print("Возникла ошибка при решении системы:", e)

    def print_triangular_matrix(self):
        print("\nТреугольная матрица:")
        for i in range(len(self.matrix)):
            print(' '.join(f"{i:7.7f}" for i in self.matrix[i]), end=' ')
            print(f"{self.vector[i]:7.7f}")

    def print_solution(self):
        if isinstance(self.solution[0], float):
            print("\nВектор неизвестных:")
            print(' '.join(f"{i:7.7f}" for i in self.solution))
        else:
            print()
            print(self.solution)

    def print_residuals(self):
        if isinstance(self.residuals, float):
            print("\nВектор невязок:")
            print(' '.join(f"{i:7.7f}" for i in self.residuals))

    def print_determinant(self):
        print("\nОпределитель:")
        if isinstance(self.det, float):
            print(f"{self.det:7.7f}")
        else:
            print(self.det)
