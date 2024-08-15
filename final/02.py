import matplotlib.pyplot as plt
import numpy as np

def draw_pythagoras_tree(ax, x, y, angle, depth, max_depth, length):
    if depth == max_depth:
        return

    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)
    
    ax.plot([x, x_end], [y, y_end], color='green', lw=2)

    new_length = length * np.sqrt(0.5)
    draw_pythagoras_tree(ax, x_end, y_end, angle + np.pi / 4, depth + 1, max_depth, new_length)
    draw_pythagoras_tree(ax, x_end, y_end, angle - np.pi / 4, depth + 1, max_depth, new_length)

def pythagoras_tree(max_depth):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    x_start, y_start = 0, 0
    initial_length = 10
    initial_angle = np.pi / 2

    draw_pythagoras_tree(ax, x_start, y_start, initial_angle, 0, max_depth, initial_length)

    plt.show()

if __name__ == "__main__":
    try:
        max_depth = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
        pythagoras_tree(max_depth)
    except ValueError:
        print("Будь ласка, введіть ціле число.")

