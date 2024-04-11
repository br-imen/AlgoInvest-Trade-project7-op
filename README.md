# Investment Data Comparison

## Description
This project aims to compare two algorithms for selecting the best combination of investments, ensuring that the total cost does not exceed a specified budget. The project includes two algorithms: a brute-force algorithm and an optimized algorithm.

## Algorithms
### Brute-force Algorithm
The brute-force algorithm iterates through all possible combinations of investments and calculates the total profit for each combination. It then selects the combination with the maximum profit that does not exceed the budget.

### Optimized Algorithm
The optimized algorithm utilizes a dynamic programming approach known as the knapsack algorithm. It efficiently calculates the maximum profit that can be achieved within the budget by considering the value-to-cost ratio of each investment.

## Data
- The investment data is stored in a CSV file, containing information such as investment names, prices, and profits.
- The data is loaded into memory using the pandas library for processing.

## Features
- **Input Data:** Read investment data from a CSV file.
- **Brute-force Algorithm:** Iterate through all combinations to find the best solution.
- **Optimized Algorithm:** Use dynamic programming to efficiently solve the problem.
- **Output:** Display the total price, total value, and selected investments for each algorithm.
- **Performance Comparison:** Measure the execution time of each algorithm.

## Tech Stack
- **Python:** Programming language used for algorithm implementation.
- **pandas:** Library for data manipulation and analysis.
- **time:** Module for measuring execution time.

## Project Structure
- `data/`: Directory containing CSV files with investment data.
- `bruteforce.py`: Python script implementing the brute-force algorithm.
- `optimized.py`: Python script implementing the optimized algorithm.
- `README.md`: Documentation explaining the project, algorithms, and usage instructions.

## Usage
1. Ensure you have Python installed on your system.
2. Install the required dependencies using pip:
   ```bash
   pip install pandas
   ```
3. Run the brute-force algorithm:
   ```bash
   python3 bruteforce.py
   ```
4. Run the optimized algorithm:
   ```bash
   python3 optimized.py
   ```

## Conclusion
The project provides two alternative approaches for selecting the best combination of investments within a budget. While the brute-force algorithm explores all possible combinations, the optimized algorithm offers a more efficient solution using dynamic programming. The choice of algorithm depends on factors such as the size of the dataset and the available computational resources.