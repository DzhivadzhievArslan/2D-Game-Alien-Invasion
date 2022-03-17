import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
# Создаем список для хранения данных, которые будут наноситься на график
squares = [1, 4, 9, 16, 25]
plt.style.use('seaborn')
# fig - представляет весь рисунок или набор генерируемых диаграмм
# ax - представляет одну диаграмму на рисунке
# subplots() - функция, позволяющая сгенерировать одну или несколько поддиаграмм на одной диаграмме
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
# Назначение заголовка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Назначение размера шрифта делений на осях.
ax.tick_params(axis='both', labelsize=14)
# plot() - функция, которая пытается построить графическое представление для заданных чисел
ax.plot(input_values, squares)
# show() - открывает окно просмотра Matplotlib и выводит график
plt.show()
# test
print("Everything is okay!")