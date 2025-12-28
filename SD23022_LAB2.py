import random
import streamlit as st

POPULATION_SIZE = 300
CHROMOSOME_LENGTH = 80
TARGET_ONES = 50
GENERATIONS = 50
MUTATION_RATE = 0.01

def generate_individual():
    return [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]

def fitness(individual):
    ones_count = sum(individual)
    return 80 - abs(TARGET_ONES - ones_count)

def selection(population):
    population.sort(key=lambda x: fitness(x), reverse=True)
    return population[:POPULATION_SIZE // 2]

def crossover(parent1, parent2):
    point = random.randint(1, CHROMOSOME_LENGTH - 1)
    return parent1[:point] + parent2[point:]

def mutation(individual):
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]
    return individual

population = [generate_individual() for _ in range(POPULATION_SIZE)]

for generation in range(GENERATIONS):
    selected = selection(population)
    next_generation = []

    while len(next_generation) < POPULATION_SIZE:
        parent1 = random.choice(selected)
        parent2 = random.choice(selected)
        child = crossover(parent1, parent2)
        child = mutation(child)
        next_generation.append(child)

    population = next_generation

best_individual = max(population, key=lambda x: fitness(x))

print("Best Individual:", best_individual)
print("Number of Ones:", sum(best_individual))
print("Fitness Value:", fitness(best_individual))
