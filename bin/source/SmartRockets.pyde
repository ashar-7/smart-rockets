import Rocket
import Population
import dna

population = []
lifespan = 400
count = 0
target = None
genNumber = 0
totalPopulation = 500
obstacleLoc = None
obstacleSize = None

def setup() :
    global population; global target; global obstacleLoc; global obstacleSize;
    size(600, 600)
    
    target = PVector(width / 2, height / 4)
    obstacleLoc = PVector(target.x - 50, target.y + 40)
    obstacleSize = PVector(100, 15)

    population = Population.Population(totalPopulation, width / 2, height / 2, lifespan, target)

    # Add obstacle
    population.population[0].obstacleLocs.append(obstacleLoc)
    population.population[0].obstacleSizes.append(obstacleSize)

def draw() :
    global population; global count; global genNumber; global maxFitness;
    background(51)
    ellipse(target.x, target.y, 30, 30)
    rectMode(CORNER)
    rect(obstacleLoc.x, obstacleLoc.y, obstacleSize.x, obstacleSize.y)

    population.run()

    textSize(20)
    text("Generation Number: " + str(genNumber), 50, 30)
    text("Cycles Completed: " + str(count) + "/" + str(lifespan), 50, 60)
    text("Maximum Fitness (in %): " + str(population.maxFitness * 100), 50, 90)
    text("Average Fitness (in %): " + str(population.avgFitness * 100), 50, 120)

    count += 1
    if count == lifespan :
        count = 0
        population.loop()
        genNumber += 1