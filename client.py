"""
Autonomous Agent Simulated Annealing Combinatorial Optimizer Skill
Pure Python Standard Library implementation.
"""
import math
import random
from typing import List, Dict, Any, Tuple

class SimulatedAnnealingOptimizer:
    """
    Simulated Annealing metaheuristic optimizer for combinatorial problems (e.g. TSP).
    """
    def __init__(self, initial_temp: float = 100.0, cooling_rate: float = 0.995, 
                 min_temp: float = 1e-4, max_iterations: int = 5000, seed: int = 42):
        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate
        self.min_temp = min_temp
        self.max_iterations = max_iterations
        self.random = random.Random(seed)

    def optimize_tsp(self, coordinates: List[Tuple[float, float]]) -> Dict[str, Any]:
        num_cities = len(coordinates)
        if num_cities <= 1:
            return {"optimal_route": list(range(num_cities)), "optimal_cost": 0.0, "convergence_history": []}

        dist_mat = [[0.0] * num_cities for _ in range(num_cities)]
        for i in range(num_cities):
            for j in range(num_cities):
                dx = coordinates[i][0] - coordinates[j][0]
                dy = coordinates[i][1] - coordinates[j][1]
                dist_mat[i][j] = math.hypot(dx, dy)

        def tour_cost(tour: List[int]) -> float:
            c = 0.0
            for k in range(len(tour)):
                c += dist_mat[tour[k]][tour[(k + 1) % len(tour)]]
            return c

        current_tour = list(range(num_cities))
        self.random.shuffle(current_tour)
        current_cost = tour_cost(current_tour)

        best_tour = list(current_tour)
        best_cost = current_cost

        temp = self.initial_temp
        history = []
        accepted_transitions = 0

        for it in range(self.max_iterations):
            if temp < self.min_temp:
                break

            i, j = sorted(self.random.sample(range(num_cities), 2))
            candidate_tour = current_tour[:i] + current_tour[i:j+1][::-1] + current_tour[j+1:]
            candidate_cost = tour_cost(candidate_tour)

            delta = candidate_cost - current_cost

            if delta < 0 or self.random.random() < math.exp(-delta / temp):
                current_tour = candidate_tour
                current_cost = candidate_cost
                accepted_transitions += 1

                if current_cost < best_cost:
                    best_cost = current_cost
                    best_tour = list(current_tour)

            if it % 500 == 0:
                history.append({"iteration": it, "temperature": round(temp, 4), "cost": round(best_cost, 4)})

            temp *= self.cooling_rate

        history.append({"iteration": self.max_iterations, "temperature": round(temp, 4), "cost": round(best_cost, 4)})

        return {
            "optimal_route": best_tour,
            "optimal_cost": round(best_cost, 4),
            "iterations_performed": self.max_iterations,
            "accepted_transitions": accepted_transitions,
            "convergence_history": history
        }
