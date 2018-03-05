class Dna :

    def __init__(self, lifespan) :
        self.genes = []
        self.lifespan = lifespan

        for i in range(lifespan) :
            self.genes.append(PVector.random2D())
            self.genes[i].setMag(0.1)

    def crossover(self, partner) :
        newDNA = Dna(self.lifespan)

        # Generate a random midpoint, and perform crossover
        mid = int(random(len(self.genes)))
        for i in range(len(self.genes)) :
            if i > mid :
                newDNA.genes[i] = self.genes[i]
            else :
                newDNA.genes[i] = partner.genes[i]

        return newDNA

    def mutate(self, rate) :
        # Perform mutation with the given rate (ranging between 0 and 1)
        for g in self.genes :
            if random(1) < rate :
                g = PVector.random2D()
                g.setMag(0.1)