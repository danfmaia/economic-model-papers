# sensitivity-analysis.py
"""
Sensitivity Analysis Script for UBI Progressive Adoption Model

This script analyzes how variations in key parameters affect the simulation outcomes.

Author: [Your Name]
Date: [Date]
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters to test
MPC_values = [0.7, 0.8, 0.9]
epsilon_values = [0.05, 0.1, 0.2]

# Function to run simulation with different MPC and epsilon


def run_simulation(MPC, epsilon):
    # (Include the simulation code here, adjusting MPC and epsilon)
    # For brevity, use a simplified version or assume the function returns a DataFrame
    # Replace with actual simulation code
    pass


# Analyze the impact of different MPC values
for MPC in MPC_values:
    # Run simulation
    # results_MPC = run_simulation(MPC=MPC, epsilon=0.1)
    # For illustration, load existing results and adjust
    results_MPC = pd.read_csv('../data/simulation-results.csv')
    # Adjust consumption proportionally
    results_MPC['Consumption'] *= MPC / 0.8

    # Plot GDP
    plt.plot(results_MPC['Year'], results_MPC['GDP'] /
             1e12, label=f'MPC={MPC}')

plt.title('GDP over Time for Different MPC Values')
plt.xlabel('Year')
plt.ylabel('GDP (Trillions of Dollars)')
plt.legend()
plt.grid(True)
plt.savefig('../figures/GDP_vs_MPC.png')
plt.close()

# Analyze the impact of different epsilon values
for epsilon in epsilon_values:
    # Run simulation
    # results_epsilon = run_simulation(MPC=0.8, epsilon=epsilon)
    # For illustration, load existing results and adjust
    results_epsilon = pd.read_csv('../data/simulation-results.csv')
    results_epsilon['Labor_Supply'] *= (1 - epsilon * (
        results_epsilon['UBI'] / Y_avg)) / (1 - 0.1 * (results_epsilon['UBI'] / Y_avg))

    # Plot Labor Supply
    plt.plot(results_epsilon['Year'], results_epsilon['Labor_Supply'] /
             1e6, label=f'Epsilon={epsilon}')

plt.title('Labor Supply over Time for Different Elasticities')
plt.xlabel('Year')
plt.ylabel('Labor Supply (Millions)')
plt.legend()
plt.grid(True)
plt.savefig('../figures/LaborSupply_vs_Epsilon.png')
plt.close()

print("Sensitivity analysis completed. Figures saved in '../figures/'.")
