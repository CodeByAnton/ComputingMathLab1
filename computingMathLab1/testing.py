from gauss import GaussSolver

print("\n----------------------------Тестировнаие-----------------------------------\n")

print("\n----------------------------Тест1-------------------------------------\n")
solver1 = GaussSolver()
solver1.input_from_file("Test1")
solver1.gaussian_elimination()
right_answers = [-3, -1, 2, 7]
flag_test1 = True
for i in range(4):
    if abs(right_answers[i] - solver1.solution[i]) > 0.0000001:
        flag_test1 = False
        break
print("Тест 1 пройден" if flag_test1 else "Тест 1 провален")

print("\n----------------------------Тест2-------------------------------------\n")
solver2 = GaussSolver()
solver2.input_from_file("Test2")
solver2.gaussian_elimination()
print("Тест 2 пройден" if solver2.solution == "Система уравнений не имеет решений." else "Тест 2 провален")

print("\n----------------------------Тест3-------------------------------------\n")
solver3 = GaussSolver()
solver3.input_from_file("Test3")
solver3.gaussian_elimination()
print("Тест 3 пройден" if solver3.solution == "Система уравнений имеет бесконечное количество решений." else "Тест 3 провален")
