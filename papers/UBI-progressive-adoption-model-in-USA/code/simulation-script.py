# simulation-script.py
"""
Simulation Script for UBI Progressive Adoption Model in the USA

This script simulates the economic impacts of progressively implementing a Universal Basic Income (UBI) in the United States.

Author: [Your Name]
Date: [Date]
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
t_start = 0
t_end = 30  # Simulation over 30 years
time = np.arange(t_start, t_end + 1)

# Initialize variables
P0 = 330e6  # Initial population
n = 0.005   # Population growth rate
MPC = 0.8   # Marginal propensity to consume
epsilon = 0.1  # Labor supply elasticity
tau_0 = 0.20   # Initial tax rate
A = 1.0        # Total factor productivity
alpha = 0.7    # Output elasticity of labor
delta = 0.05   # Depreciation rate of capital
r = 0.03       # Interest rate on government debt
mu = 0.5       # Inflation sensitivity
UBI_max = 12000  # Maximum UBI amount per person per year
T_adopt = 10     # UBI adoption period in years

# Initialize data storage
results = pd.DataFrame(columns=[
    'Year', 'Population', 'UBI', 'GDP', 'Consumption', 'Investment',
    'Government_Debt', 'Tax_Revenue', 'Labor_Supply', 'Employment',
    'Wage_Rate', 'Inflation', 'Poverty_Rate', 'Gini_Coefficient'
])

# Initial conditions
K_prev = 5e12     # Initial capital stock
D_prev = 20e12    # Initial government debt
pi_prev = 0.02    # Initial inflation rate
Y_potential = 20e12  # Potential GDP
L0 = 160e6        # Initial labor supply
Y_avg = 60000     # Average income per capita
C0 = 1e12         # Autonomous consumption

# Simulation loop
for t in time:
    # Calculate population
    P_t = P0 * np.exp(n * t)

    # Determine UBI amount
    if t <= T_adopt:
        UBI_t = UBI_max * (t / T_adopt)
    else:
        UBI_t = UBI_max

    # Total UBI cost
    UBI_cost = UBI_t * P_t

    # Adjust labor supply
    L_S_t = L0 * (1 - epsilon * (UBI_t / Y_avg))

    # Ensure labor supply is non-negative
    L_S_t = max(L_S_t, 0)

    # Production function
    Y_t = A * (L_S_t ** alpha) * (K_prev ** (1 - alpha))

    # Tax rate adjusts to fund UBI
    tau_UBI = (UBI_cost + r * D_prev) / Y_t
    tau_t = tau_0 + tau_UBI

    # Tax revenue
    T_t = tau_t * Y_t

    # Disposable income
    Y_D_t = Y_t - T_t + UBI_cost

    # Consumption
    C_t = C0 + MPC * Y_D_t

    # Investment
    I_t = Y_t - C_t - UBI_cost  # Assuming G(t) = 0 for simplicity

    # Capital accumulation
    K_t = K_prev + I_t - delta * K_prev

    # Government debt update
    D_t = D_prev + (UBI_cost + r * D_prev) - T_t

    # Inflation
    output_gap = (Y_t - Y_potential) / Y_potential
    pi_t = pi_prev + mu * output_gap

    # Poverty rate reduction (simplified assumption)
    Poverty_Rate_t = max(0, 12 - (UBI_t / UBI_max) * 6)

    # Gini coefficient reduction (simplified assumption)
    Gini_Coefficient_t = max(0.35, 0.41 - (UBI_t / UBI_max) * 0.05)

    # Store results
    results = results.append({
        'Year': t,
        'Population': P_t,
        'UBI': UBI_t,
        'GDP': Y_t,
        'Consumption': C_t,
        'Investment': I_t,
        'Government_Debt': D_t,
        'Tax_Revenue': T_t,
        'Labor_Supply': L_S_t,
        'Employment': L_S_t,  # Assuming full employment
        'Wage_Rate': Y_t / L_S_t if L_S_t != 0 else 0,
        'Inflation': pi_t,
        'Poverty_Rate': Poverty_Rate_t,
        'Gini_Coefficient': Gini_Coefficient_t
    }, ignore_index=True)

    # Update previous period variables
    K_prev = K_t
    D_prev = D_t
    pi_prev = pi_t

# Save results to CSV
results.to_csv('../data/simulation-results.csv', index=False)

print("Simulation completed. Results saved to '../data/simulation-results.csv'.")
