# Cobb-Douglas Production Function
# This script calculates output based on the Cobb-Douglas production function.

def cobb_douglas(K, L, A=1, alpha=0.3):
    """
    Calculate output using the Cobb-Douglas production function.

    Parameters:
    - K: Capital input
    - L: Labor input
    - A: Total factor productivity (default=1)
    - alpha: Output elasticity of capital (default=0.3)

    Returns:
    - Y: Output
    """
    Y = A * (K ** alpha) * (L ** (1 - alpha))
    return Y


# Example usage
capital = 100
labor = 200
output = cobb_douglas(capital, labor)
print(f'Output: {output}')
