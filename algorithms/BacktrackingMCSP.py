import math

class BacktrackingMCSP:
    def __init__(self, graph, times, fuels, source, target, fuel_budget):
        """
        graph: dict {u: [v1, v2, ...]} adjacency list
        times[u][v]: traversal time of edge (u,v)
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
        self.best_path = None
        self.best_time = math.inf
        self.best_fuel = math.inf

    def _dfs(self, u, path, time_used, fuel_used, visited):
        # prune by fuel budget
        if fuel_used > self.fuel_budget:
            return
        # prune by current best time
        if time_used >= self.best_time:
            return
        # reached target
        if u == self.target:
            self.best_path = path[:]
            self.best_time = time_used
            self.best_fuel = fuel_used
            return
        # explore neighbors
        for v in self.graph[u]:
            if v in visited:
                continue
            self._dfs(
                v,
                path + [v],
                time_used + self.times[u][v],
                fuel_used + self.fuels[u][v],
                visited | {v}
            )

    def run(self):
        self.best_path, self.best_time, self.best_fuel = None, math.inf, math.inf
        self._dfs(self.source, [self.source], 0, 0, {self.source})
        return self.best_path, self.best_time, self.best_fuel
