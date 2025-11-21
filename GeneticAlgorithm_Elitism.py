import random

class Chromosome:
    """
    Represents a chromosome (solution) for the genetic algorithm applied to the knapsack problem.
    Each gene in the chromosome is a binary string representing whether an item is included (1) or not (0).
    """
    
    def __init__(self, genes, knapsack):
        """
        Initializes a chromosome with genes and computes its fitness and weight.
        :param genes: List of binary values (as strings) indicating inclusion of items.
        :param knapsack: Dictionary of items with value and weight.
        """
        self.genes = genes
        self.fitness = self.calculate_fitness(knapsack)
        self.weight = self.total_weight(knapsack)

    def calculate_fitness(self, knapsack):
        """
        Calculates the total worth of the items included in the chromosome.
        :param knapsack: Dictionary of items with value and weight.
        :return: Total value of selected items.
        """
        fitness = 0
        # Sum values of selected items
        for i in range(len(self.genes)):
            if self.genes[i] == '1': # If gene is 1 it means this item is selected from knapsack so add its worth to fitness
                fitness += knapsack[i][0]
        return fitness

    def total_weight(self, knapsack):
        """
        Calculates the total weight of the items included in the chromosome.
        :param knapsack: Dictionary of items with value and weight.
        :return: Total weight of selected items.
        """
        weight = 0
        for i in range(len(self.genes)):
            if self.genes[i] == '1': # If gene is 1 it means this item is selected from knapsack so add its weight to weight variable
                weight += knapsack[i][1]
        return weight

    def __str__(self):
        """
        Creates a human-readable string representation of the chromosome.
        :return: A string showing items included in the knapsack.
        """
        output = ''
        for i in range(len(self.genes)):
            if self.genes[i] == '1':
                output += f'Item worth {knapsack[i][0]} and weight {knapsack[i][1]} \n'
        return output


class GeneticAlgorithm:
    """
    Represents the genetic algorithm for solving the 0/1 knapsack problem.
    Includes population generation, selection, crossover, mutation, and evolution logic.
    """

    def __init__(self, weight_limit, knapsack, population_size, mutation_rate):
        """
        Initializes the genetic algorithm parameters.
        :param weight_limit: Maximum allowed weight of the knapsack.
        :param knapsack: Dictionary of items with value and weight.
        :param population_size: Number of individuals in the population.
        :param mutation_rate: Probability of gene mutation (between 0 and 1).
        """
        self.weight_limit = weight_limit
        self.knapsack = knapsack
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = self.initialize_population()

    def initialize_population(self):
        """
        Creates an initial population of valid chromosomes.
        :return: List of Chromosome objects within weight limit.
        """
        population = []
        while len(population) < self.population_size:
            member = [random.choice(['0', '1']) for _ in range(10)]
            member = Chromosome(member, self.knapsack)
            if member.weight <= self.weight_limit:
                population.append(member)
        return population

    def selection(self):
        """
        Selects two fittest chromosomes from the population using elitism.
        :return: List of two selected Chromosome objects.
        """
        selected = []
        one = max(self.population, key=lambda c: c.fitness)
        self.population.remove(one)
        two = max(self.population, key=lambda c: c.fitness)
        self.population.remove(two)
        selected.extend([one, two])
        return selected

    def crossover(self, parent1, parent2):
        """
        Performs single-point crossover between two parent chromosomes.
        Ensures offspring are valid (i.e., within weight limit).
        :param parent1: First parent Chromosome.
        :param parent2: Second parent Chromosome.
        :return: Two child Chromosomes after crossover.
        """
        array1 = parent1.genes[0:5] + parent2.genes[5:]
        array2 = parent2.genes[0:5] + parent1.genes[5:]

        child1 = Chromosome(array1, self.knapsack)
        child2 = Chromosome(array2, self.knapsack)

        # Replace children with parents if they exceed weight limit
        if child1.weight > self.weight_limit:
            child1 = parent1
        if child2.weight > self.weight_limit:
            child2 = parent2
        
        return child1, child2

    def mutation(self, chromosome):
        """
        Mutates a chromosome's genes based on mutation rate while respecting weight constraints.
        :param chromosome: Chromosome to mutate.
        :return: Mutated Chromosome object.
        """
        number = int(self.mutation_rate * len(chromosome.genes)) # For calculating how many genes to mutate
        numbers = random.sample(range(len(chromosome.genes)), number) # Random selecting genes number out of total genes

        for i in numbers:
            original_gene = chromosome.genes[i]
            # Flip the bit
            chromosome.genes[i] = '0' if original_gene == '1' else '1'

            # Recalculate fitness and weight
            chromosome.weight = chromosome.total_weight(self.knapsack)
            chromosome.fitness = chromosome.calculate_fitness(self.knapsack)

            # Revert if weight limit is exceeded
            if chromosome.weight > self.weight_limit:
                chromosome.genes[i] = original_gene
                chromosome.weight = chromosome.total_weight(self.knapsack) # Recalculate weight
                chromosome.fitness = chromosome.calculate_fitness(self.knapsack) # Recalculate fitness

        return chromosome

    def evolve(self):
        """
        Evolves the population using selection, crossover, and mutation.
        Replaces the old population with a new one.
        """
        new_population = []
        for _ in range(self.population_size // 2):
            p1, p2 = self.selection()
            c1, c2 = self.crossover(p1, p2)
            c1 = self.mutation(c1)
            c2 = self.mutation(c2)
            new_population.extend([c1, c2])
        self.population = new_population

    def get_solution(self):
        """
        Returns the best chromosome from the population based on fitness.
        :return: Chromosome with highest fitness.
        """
        return max(self.population, key=lambda c: c.fitness)


def build_knapsack(file):
    """
    Reads item data from a file and constructs the knapsack dictionary.
    :param file: File path containing item values and weights.
    :return: Tuple containing weight limit and knapsack dictionary.
    """
    w = None 
    knapsack = {}

    with open(file, 'r') as file:
        line = file.readline()
        count, w = list(int(i) for i in line.split())
        for i in range(count):
            line = file.readline()
            worth, weight = list(int(i) for i in line.split())
            knapsack[i] = (worth, weight)
    
    return w, knapsack


if __name__ == "__main__":
    # Load knapsack data from file
    w, knapsack = build_knapsack('test case for 0-1 knapsack problem.txt')

    # Initialize Genetic Algorithm
    ga = GeneticAlgorithm(w, knapsack, population_size=10, mutation_rate=0.2)
    
    # Evolve the population over 50 generations
    for _ in range(50):
        ga.evolve()

    # Display all chromosome fitness and weights
    for i in ga.population:
        print(i.fitness, i.total_weight(knapsack), sep=' ')
    
    print()

    # Display best solution
    best_solution = ga.get_solution()
    print("Best solution found:", best_solution, sep='\n')
    print("Fitness of best solution:", best_solution.fitness)
    print("Weight of best solution:", best_solution.weight)
