class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __lt__(self, other):
        return (self.value / self.weight) > (other.value / other.weight)

def fractional_knapsack(items, capacity):
    items.sort(reverse=True, key=lambda x: x.value / x.weight)
    total_value = 0.0
    for item in items:
        if capacity > 0 and item.weight <= capacity:
            capacity -= item.weight
            total_value += item.value
        else:
            fractional = capacity / item.weight
            total_value += item.value * fractional
            break
    return total_value

items = [
    Item(60, 10),
    Item(100, 10),
    Item(120, 30)
]
capacity = 50
max_value = fractional_knapsack(items, capacity)
print(f"Maximum value in the knapsack: {max_value}")
