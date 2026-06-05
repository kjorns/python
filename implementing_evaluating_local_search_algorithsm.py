import random
import math

# Define the function to optimize
def objective_function(x):
    return -x**2 + 4*x  # A simple quadratic function

# Part 1: Implementing Hill Climbing
def hill_climbing(start_x, step_size=0.1, max_iterations=1000):
    # Step 1: Generate a random initial solution
    current_x = start_x
    current_value = objective_function(current_x)
    iterations = 0

    for i in range(max_iterations):
        iterations = i + 1
        # Step 2: Apply the hill climbing algorithm to iteratively improve the solution
        new_x = current_x + random.choice([-step_size, step_size])
        new_value = objective_function(new_x)

        # If the new solution is better, accept it
        if new_value > current_value:
            current_x, current_value = new_x, new_value
        else:
            break  # Step 3:Stop when no further improvements can be made

    return current_x, current_value, iterations

# Part 2: Implementing Simulated Annealing
def simulated_annealing(start_x, step_size=0.1, max_iterations=1000, initial_temp=100, cooling_rate=0.99):
    current_x = start_x
    current_value = objective_function(current_x)
    temperature = initial_temp # Introduce a temperature parameter that decreases over time
    iterations = 0

    for i in range(max_iterations):
        iterations = i + 1
        new_x = current_x + random.uniform(-step_size, step_size)
        new_value = objective_function(new_x)

        # Occasionally accept worse solutions to escape local optima
        delta_e = new_value - current_value

        # Accept new solution if it's better or with probability based on temperature
        if new_value > current_value or (temperature > 0 and random.uniform(0, 1) < math.exp(delta_e / temperature)):
            current_x, current_value = new_x, new_value

        # Implement a cooling schedule (exponential decay)
        temperature *= cooling_rate

        if temperature < 1e-8:  # Stop when temperature is very low
            break

    return current_x, current_value, iterations

# Part 3: Comparing Performance
def run_lab_comparison(num_trials=50):
    hc_stats = {'values': [], 'iterations': []}
    sa_stats = {'values': [], 'iterations': []}

    for _ in range(num_trials):
        start_x = random.uniform(0, 4)

        # Run Hill Climbing
        hc_solution, hc_value, hc_iteration = hill_climbing(start_x)
        hc_stats['values'].append(hc_value)
        hc_stats['iterations'].append(hc_iteration)

        # Run Simulated Annealing
        sa_solution, sa_value, sa_iteration = simulated_annealing(start_x)
        sa_stats['values'].append(sa_value)
        sa_stats['iterations'].append(sa_iteration)

    avg_hc_value = sum(hc_stats['values']) / num_trials
    avg_sa_value = sum(sa_stats['values']) / num_trials
    avg_hc_iteration = sum(hc_stats['iterations']) / num_trials
    avg_sa_iteration = sum(sa_stats['iterations']) / num_trials

    hc_success = sum(1 for v in hc_stats['values'] if v > 3.99)
    sa_success = sum(1 for v in sa_stats['values'] if v > 3.99)

    print(f"Solution Quality:")
    print(f"Hill Climbing: {avg_hc_value:.4f}")
    print(f"Simulated Annealing: {avg_sa_value:.4f}")

    print(f"Runtime Efficiency:")
    print(f"Hill Climbing: {avg_hc_iteration:.2f}")
    print(f"Simulated Annealing: {avg_sa_iteration:.2f}")

    print(f"Robustness:")
    print(f"Hill Climbing: {hc_success}/{num_trials}")
    print(f"Simulated Annealing: {sa_success}/{num_trials}")

if __name__ == "__main__":
    run_lab_comparison()