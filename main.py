from algorithms import BacktrackingMCSP, AntColonyMCSP

def ant_colony_worker():
    graph = {
        0: [1, 2],
        1: [2, 3],
        2: [3],
        3: []
    }
    times = {
        0: {1: 2, 2: 5},
        1: {2: 1, 3: 4},
        2: {3: 2},
        3: {}
    }
    fuels = {
        0: {1: 3, 2: 6},
        1: {2: 1, 3: 3},
        2: {3: 2},
        3: {}
    }
    source, target = 0, 3
    fuel_budget = 6

    colony = AntColonyMCSP(graph, times, fuels, source, target, fuel_budget, n_ants=10, n_iterations=50)

    path, time_cost, fuel_cost = colony.run()

    print("Ant Colony best path:", path)
    print("Ant Colony time cost:", time_cost)
    print("Ant Colony fuel used:", fuel_cost)

def backtracking_worker():
  graph = {
      0: [1, 2],
      1: [2, 3],
      2: [3],
      3: []
  }

  times = {
      0: {1: 2, 2: 5},
      1: {2: 1, 3: 4},
      2: {3: 2},
      3: {}
  }

  fuels = {
      0: {1: 3, 2: 6},
      1: {2: 1, 3: 3},
      2: {3: 2},
      3: {}
  }
  source, target = 0, 3
  fuel_budget = 6

  solver = BacktrackingMCSP(graph, times, fuels, source, target, fuel_budget)
  path, time_cost, fuel_cost = solver.run()
  print("Backtracking best path:", path)
  print("Backtracking time cost:", time_cost)
  print("Backtracking fuel used:", fuel_cost)


if __name__ == "__main__":
  print("Running Ant Colony Optimization for MCSP:")
  ant_colony_worker()
  print("\nRunning Backtracking for MCSP:")
  backtracking_worker()
