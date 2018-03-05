import Rocket
import dna

class Population :
    count = 0

    def __init__(self, popSize, x, y, lifespan, target) :
        self.population = []
        self.popSize = popSize
        self.matingPool = []
        self.lifespan = lifespan
        self.startX = x
        self.startY = y
        self.target = target
        self.maxFitness = -1
        self.avgFitness = -1

        # SETUP: (1 step)
            # Step 1: Initialize
            # Create a population of N elements (N = popSize) each with randomly generated DNA.
        for i in range(self.popSize) :
            self.population.append(Rocket.Rocket(x, y, target, lifespan))
            # ~Step 1: Initialize

    def run(self) :
        # Move and display rockets
        for p in self.population :
            p.update()
            p.draw()
            p.edgeCollision()

    def loop(self   ) :
        # LOOP: (2 steps)
            # Step 2: Selection
            # Evaluate the fitness of each element of the population and build a mating pool.
        self.matingPool = []

        # Calculate fitness, and build the matingPool according to it
        totalFitness = 0
        for p in self.population :
            p.calcFitness()

            totalFitness += p.fitness # Used to calculate Average Fitness
            # Calculate Maximum Fitness
            if p.fitness > self.maxFitness :
                self.maxFitness = p.fitness
            # Append p to the matingPool * p.fitness
            for f in range(int(p.fitness * 100)) :
                self.matingPool.append(p)

        # Calculate average fitness
        self.avgFitness = totalFitness / self.popSize
            # ~Step 2: Selection

            # Step 3: Reproduction (4 substeps)
            # Repeat N times (N = popSize).
        if self.matingPool :
            newPopulation = []

            # Looping N times (N = popSize)
            for i in range(self.popSize) :
                    # Substep a: Pick two parents with probability according to relative fitness.
                a = int(random(len(self.matingPool)))
                b = int(random(len(self.matingPool)))

                parentA = self.matingPool[a]
                parentB = self.matingPool[b]
                    # ~Substep a
                
                    # Substep b: Crossover--create a "child" by combining the DNA of these two parents.
                child = Rocket.Rocket(self.startX, self.startY, self.target, self.lifespan)
                child._dna = parentA._dna.crossover(parentB._dna)
                    # ~Substep b

                    # Substep c: Mutation--mutate the child's DNA based on a given probability (Mutation Rate).
                child._dna.mutate(0.01) # Mutation Rate: 1%
                    # ~Substep c

                    # Substep d: Add the new child to a new population.
                newPopulation.append(child)
                    # ~Substep d
                 
            # ~Step 3: Reproduction

                # Step 4: Replace the old population with the new population.
            self.population = newPopulation
                # ~Step 4