"""Example usage for Simulated Annealing Combinatorial Optimizer Skill."""
from client import SimulatedAnnealingOptimizer

def main():
    print("Executing Simulated Annealing Combinatorial Optimizer...")
    cities = [(0.0, 0.0), (0.0, 10.0), (10.0, 10.0), (10.0, 0.0)]
    sa = SimulatedAnnealingOptimizer(initial_temp=50.0, cooling_rate=0.99, max_iterations=2000, seed=42)
    res = sa.optimize_tsp(cities)
    print("Result:", res)
    assert abs(res["optimal_cost"] - 40.0) < 1e-3, f"Expected 40.0, got {res['optimal_cost']}"
    print("Simulated Annealing Combinatorial Optimizer verified successfully!")

if __name__ == "__main__":
    main()
