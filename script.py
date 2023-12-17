import random
from tabulate import tabulate
import math

# Function to calculate Economic Order Quantity (EOQ)
def calculate_eoq(daily_demand_mean, holding_cost_per_unit, ordering_cost):
    eoq = math.sqrt((2 * 365 * daily_demand_mean * ordering_cost) / (365*holding_cost_per_unit))
    return eoq


def simulate_inventory(initial_inventory, demand_mean, demand_stddev, restock_amount, lead_time, simulation_period,
                       holding_cost_per_unit):
    inventory = initial_inventory
    inventory_levels = [inventory]
    days_until_delivery = 0
    stockout_days = 0
    total_cost = 0

    for day in range(1, simulation_period + 1):
        daily_demand = max(0, int(random.gauss(demand_mean, demand_stddev)))

        if inventory >= daily_demand:
            inventory -= daily_demand
        else:
            stockout_days += 1
            inventory = 0

        if days_until_delivery == 0:
            if inventory < restock_amount:
                days_until_delivery = lead_time
                order_cost = (restock_amount - inventory) * holding_cost_per_unit
                total_cost += order_cost

        if days_until_delivery > 0:
            days_until_delivery -= 1
            if days_until_delivery == 0:
                inventory += restock_amount

        inventory_levels.append(inventory)

    return inventory_levels, total_cost, stockout_days


# Set parameters
initial_inventory = 160
demand_mean = 9
demand_stddev = 0.97
lead_time = 14
simulation_period = 365
holding_cost_per_unit = 0.035
ordering_cost = 50  

# Define a range of restock amounts to try
restock_amounts_to_try = [100, 110, 120, 130, 140, 150, 160, 170, 180, 200]

# Collect results in a list of lists for tabulate
results = []

# Run simulation for each restock amount and collect results
for restock_amount in restock_amounts_to_try:
    inventory_levels, total_cost, stockout_days = simulate_inventory(
        initial_inventory, demand_mean, demand_stddev, restock_amount, lead_time, simulation_period,
        holding_cost_per_unit
    )

    # Append results to the list
    results.append([restock_amount, total_cost, stockout_days])

# Display results in a table using tabulate
headers = ["Restock Amount", "Total Inventory Cost", "Stockout Days"]
print(tabulate(results, headers=headers, tablefmt="grid"))

# Calculate EOQ
eoq = calculate_eoq(demand_mean, holding_cost_per_unit, ordering_cost)

# Display EOQ
print(f"Economic Order Quantity (EOQ): {eoq}")
