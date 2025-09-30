import random
import math
from collections import defaultdict

class AntColonyMCSP:
    def __init__(self, graph, times, fuels, source, target, fuel_budget,
                 n_ants=20, n_iterations=100, alpha=1.0, beta=2.0,
                 rho=0.5, q=100.0):
        """
        graph: dict {u: [v1,v2,...]} adjacency list
        times[u][v]: cost (time) of edge (u,v)
        fuels[u][v]: fuel consumption of edge (u,v)
        source: start node
        target: end node
        fuel_budget: maximum allowed fuel
        """
        self.graph = graph
        self.times = times
        self.fuels = fuels
        self.source = source
        self.target = target
        self.fuel_budget = fuel_budget
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.q = q

        # initialize pheromone trails
        self.pheromone = defaultdict(lambda: defaultdict(lambda: 1.0))

    def _construct_solution(self):
        path = [self.source]
        fuel_used = 0
        time_used = 0
        visited = set([self.source])

        while path[-1] != self.target:
            u = path[-1]
            neighbors = self.graph[u]
            feasible = []
            probs = []
            for v in neighbors:
                if v in visited:
                    continue
                fuel_needed = self.fuels[u][v]
                if fuel_used + fuel_needed <= self.fuel_budget:
                    tau = self.pheromone[u][v] ** self.alpha
                    eta = (1.0 / (self.times[u][v] + 1e-9)) ** self.beta
                    feasible.append(v)
                    probs.append(tau * eta)

            if not feasible:
                return None, math.inf, math.inf  # infeasible path

            # roulette-wheel selection
            s = sum(probs)
            r = random.random() * s
            cum = 0
            for v, p in zip(feasible, probs):
                cum += p
                if cum >= r:
                    chosen = v
                    break

            path.append(chosen)
            fuel_used += self.fuels[u][chosen]
            time_used += self.times[u][chosen]
            visited.add(chosen)

        return path, time_used, fuel_used

    def _update_pheromones(self, solutions):
        # evaporate
        for u in self.graph:
            for v in self.graph[u]:
                self.pheromone[u][v] *= (1 - self.rho)

        # reinforce
        for path, time_used, fuel_used in solutions:
            if path is None:
                continue
            contribution = self.q / (time_used + 1e-9)
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                self.pheromone[u][v] += contribution

    def run(self):
        best_path, best_time, best_fuel = None, math.inf, math.inf
        for _ in range(self.n_iterations):
            solutions = []
            for _ in range(self.n_ants):
                path, time_used, fuel_used = self._construct_solution()
                if path is not None and time_used < best_time:
                    best_path, best_time, best_fuel = path, time_used, fuel_used
                solutions.append((path, time_used, fuel_used))
            self._update_pheromones(solutions)
        return best_path, best_time, best_fuel
