## **Appendix A: Theoretical Framework and Mathematical Model**

In this appendix, we present the theoretical foundations and mathematical formulations of our model for the progressive adoption of Universal Basic Income (UBI) in the United States. While the model's structure is fully developed, we acknowledge that the actual numerical calculations and simulations have not been conducted at this time. This work is intentionally left open for contributions from researchers and practitioners who wish to explore the model further.

### **A1. Mathematical Formulation**

The model integrates key economic components to simulate the impact of UBI implementation over time. The core equations are as follows:

#### **1. Population Dynamics**

The total population \( P(t) \) at time \( t \) is modeled using an exponential growth function:

\[
P(t) = P_0 \times e^{n(t - t_0)}
\]

- \( P_0 \): Initial population at base year \( t_0 \).
- \( n \): Annual population growth rate.

#### **2. UBI Implementation Schedule**

The UBI amount per person \( UBI(t) \) increases linearly over the adoption period \( T\_{\text{adopt}} \):

\[
UBI(t) =
\begin{cases}
0, & \text{if } t < t*0 \\
UBI*{\text{max}} \times \dfrac{t - t*0}{T*{\text{adopt}}}, & \text{if } t*0 \leq t \leq t_0 + T*{\text{adopt}} \\
UBI*{\text{max}}, & \text{if } t > t_0 + T*{\text{adopt}}
\end{cases}
\]

- \( UBI\_{\text{max}} \): Maximum UBI amount per person.
- \( T\_{\text{adopt}} \): Total time period for full UBI implementation.

#### **3. Government Budget Constraint**

The government's budget constraint incorporates UBI costs:

\[
G(t) + UBI(t) \times P(t) + r \times D(t - 1) = T(t) + D(t) - D(t - 1)
\]

- \( G(t) \): Government spending excluding UBI.
- \( r \): Interest rate on government debt.
- \( D(t) \): Government debt at time \( t \).
- \( T(t) \): Total tax revenue.

#### **4. Taxation Mechanism**

Total tax revenue \( T(t) \) is given by:

\[
T(t) = \tau(t) \times Y(t)
\]

- \( \tau(t) \): Average effective tax rate at time \( t \).
- \( Y(t) \): Gross Domestic Product (GDP) at time \( t \).

The average effective tax rate adjusts to fund UBI:

\[
\tau(t) = \tau*0 + \tau*{\text{UBI}}(t)
\]

- \( \tau_0 \): Initial average tax rate.
- \( \tau\_{\text{UBI}}(t) \): Additional tax rate required to fund UBI.

#### **5. Consumption Function**

Household consumption \( C(t) \) is modeled as:

\[
C(t) = C_0 + MPC \times \left( Y_D(t) \right)
\]

- \( C_0 \): Autonomous consumption.
- \( MPC \): Marginal propensity to consume.
- \( Y_D(t) \): Disposable income at time \( t \):

\[
Y_D(t) = Y(t) - T(t) + UBI(t) \times P(t)
\]

#### **6. Labor Supply and Employment**

**Labor Supply \( L_S(t) \):**

\[
L*S(t) = L_0 \times \left( 1 - \epsilon \times \dfrac{UBI(t)}{Y*{\text{avg}}} \right)
\]

- \( L_0 \): Initial labor supply.
- \( \epsilon \): Labor supply elasticity with respect to income.
- \( Y\_{\text{avg}} \): Average income per capita.

**Labor Demand \( L_D(t) \):**

\[
L_D(t) = \phi \times \dfrac{Y(t)}{w(t)}
\]

- \( \phi \): Productivity parameter.
- \( w(t) \): Real wage rate.

**Labor Market Equilibrium:**

\[
L_S(t) = L_D(t)
\]

From this equilibrium condition, we can solve for the wage rate \( w(t) \).

#### **7. Production Function and GDP**

The model uses a Cobb-Douglas production function:

\[
Y(t) = A \times [L(t)]^\alpha \times [K(t)]^{1 - \alpha}
\]

- \( A \): Total factor productivity.
- \( L(t) \): Labor input at time \( t \).
- \( K(t) \): Capital stock at time \( t \).
- \( \alpha \): Output elasticity of labor.

**Capital Accumulation:**

\[
K(t) = K(t - 1) + I(t) - \delta \times K(t - 1)
\]

- \( I(t) \): Investment at time \( t \).
- \( \delta \): Depreciation rate of capital.

**Investment Equals Savings:**

\[
I(t) = Y(t) - C(t) - G(t)
\]

#### **8. Inflation Dynamics**

Inflation \( \pi(t) \) is modeled using an expectations-augmented Phillips Curve:

\[
\pi(t) = \pi(t - 1) + \mu \times \left( \dfrac{Y(t) - Y^_(t)}{Y^_(t)} \right)
\]

- \( \pi(t) \): Inflation rate at time \( t \).
- \( \mu \): Sensitivity of inflation to the output gap.
- \( Y^\*(t) \): Potential GDP at time \( t \).

#### **9. Welfare and Inequality Measures**

- **Gini Coefficient \( Gini(t) \):**

  Measures income inequality on a scale from 0 (perfect equality) to 1 (perfect inequality).

- **Poverty Rate \( PR(t) \):**

  Represents the percentage of the population with income below the poverty threshold.

### **A2. Model Assumptions**

The model is based on several key assumptions:

1. **Closed Economy:**

   - No international trade or capital flows are considered.
   - All goods and services are produced and consumed domestically.

2. **Rational Agents:**

   - Individuals and firms make decisions to maximize utility and profits, respectively.
   - Expectations are formed rationally based on available information.

3. **Perfect Competition:**

   - Markets are perfectly competitive.
   - Prices and wages adjust to equilibrate supply and demand.

4. **Constant Parameters:**

   - Parameters such as \( A \), \( \alpha \), \( \delta \), and \( \phi \) remain constant over time.
   - Behavioral parameters like \( MPC \) and \( \epsilon \) are assumed to be stable.

5. **Labor Supply Response:**

   - Labor supply decreases as non-labor income from UBI increases, reflecting the income effect.
   - The substitution effect is minimal or offset by other factors.

6. **No Technological Change:**

   - Total factor productivity \( A \) remains constant; technological progress is not explicitly modeled.

7. **Fixed Government Spending (Excluding UBI):**

   - Government spending \( G(t) \) excluding UBI is constant or grows at a predetermined rate, independent of UBI implementation.

8. **Adaptive Inflation Expectations:**

   - Inflation expectations are based on past inflation rates rather than forward-looking rational expectations.

9. **Uniform Distribution of UBI:**

   - UBI is distributed equally to all individuals regardless of income level or employment status.

10. **No Credit Constraints:**

    - Households and firms have unrestricted access to credit markets; borrowing and lending occur freely at prevailing interest rates.

11. **Static Population Structure:**

    - Age distribution and labor force participation rates are constant, aside from changes due to UBI's impact on labor supply.

12. **Simplified Fiscal Policy:**

    - Tax policies adjust only through the average effective tax rate \( \tau(t) \) to fund UBI; other tax structures remain unchanged.

13. **Instantaneous Market Clearing:**

    - Markets clear instantly without delays or frictions; there are no inventory accumulations or shortages.

14. **Homogeneous Agents:**

    - All individuals have similar preferences and respond uniformly to economic variables, simplifying the analysis of aggregate behavior.

---

**Note to Readers:**

We hope that by opening this work for collaboration, we can collectively advance the understanding of Universal Basic Income and its potential impacts on society. Whether you are an academic researcher, a policymaker, or someone with a keen interest in economic modeling, your contributions are valuable and welcomed.
