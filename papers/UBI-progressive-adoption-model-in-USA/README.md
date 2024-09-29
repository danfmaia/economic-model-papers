# A Mathematical Model for Progressive Adoption of Universal Basic Income in the United States of America - README

This directory contains the model-centric paper **"A Mathematical Model for Progressive Adoption of Universal Basic Income in the United States of America"**, along with the associated code, data, and figures.

## **Overview**

The study develops a theoretical model to simulate the economic and social impacts of progressively implementing a Universal Basic Income (UBI) in the USA. It examines various scenarios and analyzes key indicators such as GDP growth, government debt, poverty rates, and income inequality.

## **Contents**

- **paper/**: Contains the main paper and appendices.
  - [**Main Paper**](./paper/main-paper.md)
  - [**Appendices**](./paper/appendices.md)
- **code/**: Python scripts for running simulations and performing sensitivity analyses.
- **data/**: Calibration data and simulation results.
- **figures/**: Generated figures illustrating the simulation outcomes.

## **Instructions**

### **Running the Simulation**

1. **Setup Environment**

   - Install the required Python packages:
     ```bash
     pip install numpy pandas matplotlib
     ```

2. **Run the Simulation Script**

   - Navigate to the `code/` directory:
     ```bash
     cd code/
     ```
   - Execute the simulation script:
     ```bash
     python simulation-script.py
     ```
   - The simulation results will be saved to `../data/simulation-results.csv`.

3. **Generate Figures**

   - Use the code snippets provided to generate figures from the simulation results.
   - Figures will be saved in the `figures/` directory.

### **Performing Sensitivity Analysis**

- Run the sensitivity analysis script:
  ```bash
  python sensitivity-analysis.py
  ```
- This will generate additional figures saved in the `figures/` directory.

## **Data**

- **Calibration Data**: Located in `data/calibration-data.csv`, containing the parameters used in the simulation.
- **Simulation Results**: Generated after running the simulation script, saved in `data/simulation-results.csv`.

## **Contributing**

- Contributions are welcome! Please refer to the main [CONTRIBUTING.md](../../CONTRIBUTING.md) file for guidelines.
- For this paper, you can contribute by:
  - Improving the model or simulation scripts.
  - Adding new scenarios or conducting additional analyses.
  - Enhancing documentation and visualizations.

## **License**

This project is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for details.

## **Contact**

For questions or discussions related to this paper, please open an issue or contact the maintainers.

---

**Note:** This paper is part of the **Economic Model Papers** repository, which aims to promote collaboration on model-centric economic research.
