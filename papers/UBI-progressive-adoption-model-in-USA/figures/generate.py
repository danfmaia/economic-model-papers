# GDP Growth Over Time
import pandas as pd
import matplotlib.pyplot as plt

results = pd.read_csv('../data/simulation-results.csv')

# GDP Growth Over Time
plt.plot(results['Year'], results['GDP'] / 1e12, label='GDP')
plt.title('GDP Growth Over Time')
plt.xlabel('Year')
plt.ylabel('GDP (Trillions of Dollars)')
plt.legend()
plt.grid(True)
plt.savefig('gdp-growth.png')
plt.show()

# Poverty Rate Reduction Over Time
plt.plot(results['Year'], results['Poverty_Rate'], label='Poverty Rate')
plt.title('Poverty Rate Reduction Over Time')
plt.xlabel('Year')
plt.ylabel('Poverty Rate (%)')
plt.legend()
plt.grid(True)
plt.savefig('poverty-reduction.png')
plt.show()
