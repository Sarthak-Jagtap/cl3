import numpy as np
import random
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# ---------------------------------------------------
# DUMMY DATASET
# Spray drying parameters of coconut milk
# Inputs:
# [Temperature, Feed Flow Rate]
#
# Output:
# Moisture Content
# ---------------------------------------------------

X = np.array([
    [150, 20],
    [160, 22],
    [170, 25],
    [180, 28],
    [190, 30],
    [200, 35],
    [210, 40],
    [220, 42]
])

Y = np.array([5.2, 4.8, 4.1, 3.7, 3.2, 2.9, 2.5, 2.1])

# Split dataset
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# ---------------------------------------------------
# GENETIC ALGORITHM PARAMETERS
# ---------------------------------------------------

POPULATION_SIZE = 6
GENERATIONS = 10
MUTATION_RATE = 0.2

# ---------------------------------------------------
# CHROMOSOME:
# [hidden_neurons, learning_rate]
# ---------------------------------------------------

def create_chromosome():
    hidden_neurons = random.randint(2, 20)
    learning_rate = random.uniform(0.001, 0.1)

    return [hidden_neurons, learning_rate]

# ---------------------------------------------------
# FITNESS FUNCTION
# Lower MSE = Better Fitness
# ---------------------------------------------------

def fitness(chromosome):

    hidden_neurons = chromosome[0]
    learning_rate = chromosome[1]

    # Neural Network Model
    model = MLPRegressor(
        hidden_layer_sizes=(hidden_neurons,),
        learning_rate_init=learning_rate,
        max_iter=2000,
        random_state=42
    )

    # Train Model
    model.fit(X_train, Y_train)

    # Predictions
    predictions = model.predict(X_test)

    # Mean Squared Error
    mse = mean_squared_error(Y_test, predictions)

    return mse

# ---------------------------------------------------
# SELECTION
# Select top 2 best chromosomes
# ---------------------------------------------------

def selection(population):

    population = sorted(population, key=lambda x: fitness(x))

    return population[:2]

# ---------------------------------------------------
# CROSSOVER
# ---------------------------------------------------

def crossover(parent1, parent2):

    child_hidden = random.choice([parent1[0], parent2[0]])

    child_lr = (parent1[1] + parent2[1]) / 2

    return [child_hidden, child_lr]

# ---------------------------------------------------
# MUTATION
# ---------------------------------------------------

def mutation(chromosome):

    if random.random() < MUTATION_RATE:

        chromosome[0] += random.randint(-2, 2)

        chromosome[0] = max(2, chromosome[0])

        chromosome[1] += random.uniform(-0.01, 0.01)

        chromosome[1] = max(0.001, chromosome[1])

    return chromosome

# ---------------------------------------------------
# GENETIC ALGORITHM
# ---------------------------------------------------

def genetic_algorithm():

    # Initial Population
    population = [
        create_chromosome()
        for _ in range(POPULATION_SIZE)
    ]

    best_solution = None
    best_fitness = float('inf')

    for generation in range(GENERATIONS):

        # Evaluate Population
        population = sorted(
            population,
            key=lambda x: fitness(x)
        )

        current_best = population[0]
        current_fitness = fitness(current_best)

        print(f"\nGeneration {generation+1}")

        print("Best Chromosome:", current_best)

        print("MSE:", current_fitness)

        # Update global best
        if current_fitness < best_fitness:

            best_fitness = current_fitness
            best_solution = current_best

        # Selection
        parents = selection(population)

        # Create New Population
        new_population = parents.copy()

        while len(new_population) < POPULATION_SIZE:

            parent1 = random.choice(parents)
            parent2 = random.choice(parents)

            # Crossover
            child = crossover(parent1, parent2)

            # Mutation
            child = mutation(child)

            new_population.append(child)

        population = new_population

    return best_solution, best_fitness

# ---------------------------------------------------
# MAIN
# ---------------------------------------------------

best_solution, best_error = genetic_algorithm()

print("\n--------------------------------")
print("OPTIMIZED NEURAL NETWORK")
print("--------------------------------")

print("Best Hidden Neurons:", best_solution[0])

print("Best Learning Rate:", best_solution[1])

print("Minimum MSE:", best_error)
