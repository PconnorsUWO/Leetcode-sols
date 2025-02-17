def maxWeight(pizzas):
    pizzas.sort()
    n, days = len(pizzas), len(pizzas) // 4
    total_weight, index = 0, n - 1

    # Pick heaviest pizza on odd days
    for day in range(1, days + 1, 2):
        total_weight += pizzas[index]
        index -= 1

    # Pick second heaviest pizza on even days
    index -= 1
    for day in range(2, days + 1, 2):
        total_weight += pizzas[index]
        index -= 2

    return total_weight