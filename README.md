# Graph Shortest Path Optimization

A Python implementation of two algorithms for solving the **Multi-Constraint Shortest Path (MCSP)** problem, where you need to find the shortest path between two nodes while respecting fuel consumption constraints.

## Problem Description

The Multi-Constraint Shortest Path problem involves finding the optimal path in a graph with multiple constraints:
- **Objective**: Minimize travel time between source and target nodes
- **Constraint**: Stay within a given fuel budget
- Each edge has both a time cost and a fuel consumption cost

## Algorithms Implemented

### 1. Backtracking Algorithm (`BacktrackingMCSP`)
- **Approach**: Exhaustive search using depth-first traversal
- **Pruning**: 
  - Fuel budget constraints
  - Current best time bounds
- **Guarantees**: Finds the optimal solution
- **Time Complexity**: Exponential in worst case
- **Best for**: Small graphs where optimality is required

### 2. Ant Colony Optimization (`AntColonyMCSP`)
- **Approach**: Metaheuristic inspired by ant foraging behavior
- **Features**:
  - Pheromone trail management
  - Probabilistic path construction
  - Configurable parameters (α, β, ρ, Q)
- **Guarantees**: Finds good approximate solutions
- **Time Complexity**: Polynomial
- **Best for**: Larger graphs where good solutions are acceptable

## Project Structure

```
graph-shortest-path-optimization/
├── algorithms/
│   ├── __init__.py              # Package initialization with exports
│   ├── AntColonyMCSP.py         # Ant Colony Optimization implementation
│   └── BacktrackingMCSP.py     # Backtracking algorithm implementation
├── main.py                      # Main execution script with example
└── README.md                    # This file
```

## Installation & Requirements

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only standard library)

### Setup
```bash
git clone <repository-url>
cd graph-shortest-path-optimization
```

## Usage

### Running the Demo
```bash
python3 main.py
```

This will run both algorithms on a sample graph and display the results.

### Using in Your Code

```python
from algorithms import BacktrackingMCSP, AntColonyMCSP

# Define your graph
graph = {
    0: [1, 2],
    1: [2, 3],
    2: [3],
    3: []
}

# Define time costs for each edge
times = {
    0: {1: 2, 2: 5},
    1: {2: 1, 3: 4},
    2: {3: 2},
    3: {}
}

# Define fuel costs for each edge
fuels = {
    0: {1: 3, 2: 6},
    1: {2: 1, 3: 3},
    2: {3: 2},
    3: {}
}

source, target = 0, 3
fuel_budget = 6

# Using Backtracking (exact solution)
solver = BacktrackingMCSP(graph, times, fuels, source, target, fuel_budget)
path, time_cost = solver.run()

# Using Ant Colony Optimization (approximate solution)
colony = AntColonyMCSP(graph, times, fuels, source, target, fuel_budget, 
                       n_ants=10, n_iterations=50)
path, time_cost, fuel_cost = colony.run()
```

## Algorithm Parameters

### BacktrackingMCSP
- `graph`: Adjacency list representation `{node: [neighbors...]}`
- `times`: Time costs `{u: {v: time_cost}}`
- `fuels`: Fuel costs `{u: {v: fuel_cost}}`
- `source`: Starting node
- `target`: Destination node
- `fuel_budget`: Maximum allowed fuel consumption

### AntColonyMCSP
All BacktrackingMCSP parameters plus:
- `n_ants`: Number of ants per iteration (default: 20)
- `n_iterations`: Number of iterations (default: 100)
- `alpha`: Pheromone importance (default: 1.0)
- `beta`: Heuristic importance (default: 2.0)
- `rho`: Evaporation rate (default: 0.5)
- `q`: Pheromone deposit factor (default: 100.0)

## Example Output

```
Running Ant Colony Optimization for MCSP:
Ant Colony best path: [0, 1, 2, 3]
Ant Colony time cost: 7
Ant Colony fuel used: 6

Running Backtracking for MCSP:
Backtracking best path: [0, 1, 2, 3]
Backtracking time cost: 7
```

## Performance Comparison

| Algorithm | Time Complexity | Space Complexity | Solution Quality | Use Case |
|-----------|----------------|------------------|------------------|----------|
| Backtracking | O(b^d) | O(d) | Optimal | Small graphs |
| Ant Colony | O(m × n × k) | O(V²) | Near-optimal | Large graphs |

Where:
- b = branching factor, d = depth
- m = iterations, n = ants, k = average path length
- V = number of vertices

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is part of an academic exercise for the IMT course on Graph Algorithms and Optimization.

## Authors

- Course: IMT 2A - Graphes
- Project: Graph Shortest Path Optimization