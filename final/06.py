def greedy_algorithm(items, budget):
    # Розраховуємо співвідношення калорій до вартості для кожної страви
    items_with_ratio = [(name, item['calories'] / item['cost']) for name, item in items.items()]
    
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    items_with_ratio.sort(key=lambda x: x[1], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for name, ratio in items_with_ratio:
        cost = items[name]['cost']
        calories = items[name]['calories']
        
        if total_cost + cost <= budget:
            selected_items.append(name)
            total_cost += cost
            total_calories += calories
    
    return selected_items, total_calories

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
print(greedy_algorithm(items, budget))

def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    item_choice = [[] for _ in range(budget + 1)]

    for name, item in items.items():
        cost = item['cost']
        calories = item['calories']
        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories
                item_choice[current_budget] = item_choice[current_budget - cost] + [name]

    return item_choice[budget], dp[budget]

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
print(dynamic_programming(items, budget))
