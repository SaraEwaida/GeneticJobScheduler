import random
import logging
from models import Job
from calculateMakespan import calculateMakespan

# Setup a custom logger
logger = logging.getLogger('GeneticAlgorithm')
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class Individual:
    def __init__(self, genes):
        self.genes = genes[:]  # Make a copy of the genes list to avoid unintended mutations
        self.fitness = None

    def calculate_fitness(self):
        times = [job.get_operation_times() for job in self.genes]
        machines = [job.get_operation_machines() for job in self.genes]
        config = list(range(len(self.genes)))
        self.fitness, _ = calculateMakespan(times, machines, config, len(self.genes))
        logger.info("Calculating fitness")
        return self.fitness

    def __repr__(self):
        return f'{{{" ".join([f"J{job.job_id}: {[(m, t) for m, t in zip(job.get_operation_machines(), job.get_operation_times())]}" for job in self.genes])}}}'

class Population:
    def __init__(self, jobs, size):
        self.individuals = [Individual(random.sample(jobs, len(jobs))) for _ in range(size)]

    def evolve(self, mutation_rate):
        new_population = []
        while len(new_population) < len(self.individuals):
            parent1, parent2 = random.sample(self.individuals, 2)
            child1_genes, child2_genes = self.crossover(parent1.genes, parent2.genes)
            child1 = Individual(child1_genes)
            child2 = Individual(child2_genes)
            self.mutate(child1, mutation_rate)
            self.mutate(child2, mutation_rate)
            new_population.append(child1)
            new_population.append(child2)
        self.individuals = new_population

    def crossover(self, genes1, genes2):
        point = random.randint(1, len(genes1) - 1)
        return genes1[:point] + genes2[point:], genes2[:point] + genes1[point:]

    def mutate(self, individual, mutation_rate):
        gene_length = len(individual.genes)
        for i in range(gene_length):
            if random.random() < mutation_rate:
                swap_idx = random.randint(0, gene_length - 1)
                individual.genes[i], individual.genes[swap_idx] = individual.genes[swap_idx], individual.genes[i]
                logger.info("Mutation occurred at index %d", i)

class GeneticAlgorithm:
    def __init__(self, jobs, population_size, num_generations, mutation_rate):
        self.population = Population(jobs, population_size)
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate

    def run(self):
        best_solution = None
        best_fitness = float('inf')
        detailed_chromosomes = []  # List to store detailed chromosome info

        for generation in range(self.num_generations):
            for individual in self.population.individuals:
                fitness = individual.calculate_fitness()
                if fitness < best_fitness:
                    best_fitness = fitness
                    best_solution = individual
                # Store fitness and chromosome information
                chromosome_info = f"Chromosome: {self.format_chromosome(individual)} => fitness: {fitness}"
                detailed_chromosomes.append((chromosome_info, fitness))

            # Evolve population for the next generation
            self.population.evolve(self.mutation_rate)

        # Output only the first four chromosomes and the best one
        final_output = detailed_chromosomes[:4]  # First four chromosomes
        final_output.append(
            (f"Best chromosome: {self.format_chromosome(best_solution)} => fitness: {best_fitness}", best_fitness))

        # Log final output
        for info, fit in final_output:
            logger.info(info)

        return best_solution, detailed_chromosomes  # Return both the solution and all chromosome details

    def format_chromosome(self, individual):
        return ", ".join([f"(J{job.job_id}: " + ", ".join(
            [f"(M{m}, {t})" for m, t in zip(job.get_operation_machines(), job.get_operation_times())]) + ")" for job in
                          individual.genes])


if __name__ == "__main__":
    jobs = [Job(1, [(1, 0, 10), (2, 10, 5)]), Job(2, [(2, 0, 7), (1, 7, 8)])]
    ga = GeneticAlgorithm(jobs, population_size=50, num_generations=100, mutation_rate=0.05)
    best_solution, detailed_chromosomes = ga.run()
    logger.info(f"Best solution fitness: {best_solution.fitness}")
    logger.info("Best solution operations:")
    for job in best_solution.genes:
        logger.info(f"Job {job.job_id} operations: {job.operations}")
