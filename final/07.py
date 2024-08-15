import numpy as np
import matplotlib.pyplot as plt

num_rolls = 100000

def simulate_dice_rolls(num_rolls):
    rolls = np.random.randint(1, 7, size=(num_rolls, 2))
    sums = rolls.sum(axis=1)
    return sums

def calculate_probabilities(sums):
    counts = np.bincount(sums - 2)  
    probabilities = counts / len(sums) * 100  
    return probabilities

sums = simulate_dice_rolls(num_rolls)
probabilities = calculate_probabilities(sums)

possible_sums = np.arange(2, 13)
print("Сума | Ймовірність")
print("-------------------")
for i, prob in enumerate(probabilities):
    print(f"{possible_sums[i]:2d}   | {prob:5.2f}%")

plt.figure(figsize=(10, 6))
plt.bar(possible_sums, probabilities, color='skyblue', edgecolor='black')
plt.xlabel('Сума')
plt.ylabel('Ймовірність (%)')
plt.title('Ймовірність кожної суми при киданні двох кубиків')
plt.xticks(possible_sums)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

analytical_probabilities = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]
print("Аналітичні ймовірності")
print("-------------------")
for i, prob in enumerate(analytical_probabilities):
    print(f"{possible_sums[i]:2d}   | {prob:5.2f}%")