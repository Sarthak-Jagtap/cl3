import random
from deap import base, creator, tools

# Define fitness (maximize)
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# Attribute: random number
toolbox.register("attr_float", random.uniform, -10, 10)

# Structure: individual & population
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, 1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Fitness function
def eval_func(individual):
    x = individual[0]
    return (x**2,)

toolbox.register("evaluate", eval_func)

# Operators
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    population = toolbox.population(n=10)

    generations = 10

    for gen in range(generations):
        print(f"\nGeneration {gen+1}")

        # Evaluate fitness
        for ind in population:
            ind.fitness.values = toolbox.evaluate(ind)

        # Select
        offspring = toolbox.select(population, len(population))
        offspring = list(map(toolbox.clone, offspring))

        # Crossover
        for i in range(0, len(offspring), 2):
            if i+1 < len(offspring):
                toolbox.mate(offspring[i], offspring[i+1])
                del offspring[i].fitness.values
                del offspring[i+1].fitness.values

        # Mutation
        for ind in offspring:
            if random.random() < 0.2:
                toolbox.mutate(ind)
                del ind.fitness.values

        # Re-evaluate
        for ind in offspring:
            if not ind.fitness.valid:
                ind.fitness.values = toolbox.evaluate(ind)

        population[:] = offspring

        best = max(population, key=lambda ind: ind.fitness.values[0])
        print("Best:", best[0], "Fitness:", best.fitness.values[0])

    return best

# MAIN
best = main()

print("\nFinal Best Solution:", best[0])
print("Final Fitness:", best.fitness.values[0])
