# Inventory Optimization with Python

This Python script focuses on optimizing inventory management using the Economic Order Quantity (EOQ) model and simulations. It helps businesses determine optimal restocking quantities to minimize costs while meeting demand requirements.


## Code Explanation

### Function: calculate_eoq()

This function calculates the Economic Order Quantity (EOQ) using the EOQ formula:

```python
def calculate_eoq(daily_demand_mean, holding_cost_per_unit, ordering_cost):
    eoq = math.sqrt((2 * 365 * daily_demand_mean * ordering_cost) / (365 * holding_cost_per_unit))
    return eoq
```

It takes parameters for daily demand mean, holding cost per unit, and ordering cost to calculate the EOQ. This quantity represents the ideal order size that minimizes total inventory costs.

### Function: simulate_inventory()

This function simulates inventory management over a specified period, considering various parameters such as initial inventory, demand statistics, restocking amount, lead time, and holding costs.

```python
def simulate_inventory(initial_inventory, demand_mean, demand_stddev, restock_amount, lead_time, simulation_period,
                       holding_cost_per_unit):
    # ... (code explained below)
    return inventory_levels, total_cost, stockout_days
```
It initializes inventory and iterates over each day in the simulation period, tracking daily demand and inventory levels. If inventory falls below the demand, it records stockout days and orders a restock based on lead time and restock amount. The function returns lists of inventory levels, total cost, and stockout days for analysis.

### Simulation and Results Collection

The script runs simulations for various restocking amounts defined in restock_amounts_to_try and collects data on total inventory costs and stockout days for each restocking amount.

```python
# Run simulation for each restock amount and collect results
for restock_amount in restock_amounts_to_try:
    # ... (simulation code)
    results.append([restock_amount, total_cost, stockout_days])
```

It uses the simulate_inventory() function to simulate inventory management for each restocking amount, collecting the results in a list for analysis.

### Displaying Results

Results are displayed in a table format using the tabulate library, showcasing restock amounts, total inventory costs, and stockout days.

```python
# Display results in a table using tabulate
headers = ["Restock Amount", "Total Inventory Cost", "Stockout Days"]
print(tabulate(results, headers=headers, tablefmt="grid"))
```

### Economic Order Quantity (EOQ) Calculation

Lastly, the script calculates the EOQ using the calculate_eoq() function and displays the computed EOQ value.

```python
# Calculate EOQ
eoq = calculate_eoq(demand_mean, holding_cost_per_unit, ordering_cost)

# Display EOQ
print(f"Economic Order Quantity (EOQ): {eoq}")
```

It computes the EOQ based on defined parameters and showcases the resulting value, indicating the optimal restocking quantity for minimizing inventory costs.

## Strategies & Insights

### Proposed Strategies

The script provides insights into inventory optimization strategies:

📍 EOQ Analysis: Utilize the EOQ calculation to determine the optimal restocking quantity.

📍 Cost-Benefit Analysis: Compare total inventory costs for different restocking amounts to identify cost-effective strategies.

📍 Dynamic Restocking: Consider adjusting restock amounts based on changing demand patterns to minimize stockouts and holding costs.

## Running the model & Interpeting the Results

We set the following parameters to test the model found in Operations Management Book Inventory Problems :

| Parameter              | Value        |
|------------------------|--------------|
| initial_inventory      | 160          |
| demand_mean            | 9            |
| demand_stddev          | 0.97         |
| lead_time              | 14           |
| simulation_period      | 365          |
| holding_cost_per_unit  | 0.035        |
| ordering_cost          | 50           |
| restock_amounts_to_try | [100, 110, 120, 130, 140, 150, 160, 170, 180, 200] |


![Results](/eoq_results.png)

**📍 Total Inventory Cost Fluctuations:** As the restock amount increases from 100 to 160, there's a significant drop in the total inventory cost, indicating an optimization point. However, beyond 160, the costs begin to rise again.

**📍 Impact on Stockout Days:** As the restock amount increases, stockout days decrease. Higher restock amounts generally lead to fewer instances of running out of stock (stockouts), which can impact sales or operations negatively.

**📍 Optimal Restock Quantity (EOQ):** The Economic Order Quantity (EOQ) is calculated to be approximately 160.36 units. This represents the optimal order quantity that minimizes total inventory costs, considering both ordering and holding costs.

**📍Cost-Efficiency Insights:** Restock amounts around 160 seem to be cost-efficient, resulting in lower total inventory costs and no stockout days. This aligns with the EOQ calculation and indicates a balance between ordering and holding costs.

**📍 Fluctuation Beyond the EOQ:** Beyond the EOQ, there's an observable increase in total inventory costs. This might indicate inefficiency in managing inventory, leading to increased costs or excess inventory.

***The EOQ formula assumes constant and known demand, constant unit costs, and no constraints on order quantity. **Real-world situations** often have **fluctuations in demand**, varying costs (such as volume discounts), or limitations on order quantities due to storage capacity or supplier constraints.

## References

- *[Wikipedia - Economic Order Quantity](https://en.wikipedia.org/wiki/Economic_order_quantity)*
  
- *[Investopedia - Economic Order Quantity (EOQ)](https://www.investopedia.com/terms/e/economicorderquantity.asp)*
  
- *[GitHub Repository - EOQ Calculator](https://github.com/exampleuser/eoq-calculator)*

- Operations Management: Strategy and Analysis" by Lee J. Krajewski, Larry Ritzman, and Julia Berrisford


