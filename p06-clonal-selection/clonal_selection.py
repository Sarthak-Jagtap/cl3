import random

# Fitness function (maximize)
def fitness(x):
    return x ** 2

# Initialize population
def initialize_population(size):
    return [random.uniform(-10, 10) for _ in range(size)]

# Clone best individuals
def clone(population, clone_factor=2):
    clones = []
    for individual in population:
        for _ in range(clone_factor):
            clones.append(individual)
    return clones

# Mutation (small random change)
def mutate(clones, mutation_rate=0.1):
    mutated = []
    for c in clones:
        if random.random() < mutation_rate:
            c += random.uniform(-1, 1)
        mutated.append(c)
    return mutated

# Selection (keep best)
def select(population, size):
    population = sorted(population, key=lambda x: fitness(x), reverse=True)
    return population[:size]


def clonal_selection(pop_size=5, generations=10):

    population = initialize_population(pop_size)

    for gen in range(generations):
        print(f"\nGeneration {gen+1}")

        # Evaluate
        population = select(population, pop_size)

        print("Best solution:", population[0], "Fitness:", fitness(population[0]))

        # Clone
        clones = clone(population)

        # Mutate
        mutated = mutate(clones)

        # Combine
        population = population + mutated

        # Select best again
        population = select(population, pop_size)

    return population[0]


# MAIN
best = clonal_selection()

print("\nFinal Best Solution:", best)
print("Final Fitness:", fitness(best))
