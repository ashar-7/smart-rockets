import dna

lifespan = 200

class Rocket :
    maxSpeed = 2
    maxForce = 2
    count = 0
    obstacleLocs = []
    obstacleSizes = []

    def __init__(self, x, y, target, lifespan) :
        self.location = PVector(x, y)
        self.target = target
        self.velocity = PVector(0, 0)
        self.acc = PVector(0, 0)

        self.lifespan = lifespan
        self._dna = dna.Dna(self.lifespan)
        self.fitness = 0
        self.reached = False
        self.crashed = False

    def applyForce(self, force) :
        force.limit(self.maxForce)
        self.acc += force

    def update(self) :
        if self.count == self.lifespan :
            self.count = 0
        self.applyForce(self._dna.genes[self.count])
        self.count += 1

        if PVector.dist(self.location, self.target) < 10 :
            self.location = self.target.copy()
            self.reached = True
            self.fitness = 1

        for i in range(len(self.obstacleLocs)) :
            if(self.location.x > self.obstacleLocs[i].x and 
                    self.location.x < self.obstacleLocs[i].x + self.obstacleSizes[i].x and
                    self.location.y > self.obstacleLocs[i].y and
                    self.location.y < self.obstacleLocs[i].y + self.obstacleSizes[i].y) :

                self.crashed = True
                continue

        if self.reached == False and self.crashed == False:
            self.velocity += self.acc
            self.velocity.limit(self.maxSpeed)
            self.location += self.velocity

        self.acc *= 0

    def draw(self) :
        pushMatrix()  # PUSH
        translate(self.location.x, self.location.y)
        rotate(self.velocity.heading())
        rectMode(CENTER)
        noStroke()
        fill(255)
        rect(0, 0, 30, 7)
        popMatrix()  # POP

    def edgeCollision(self) :
        if self.location.x > width :
            #self.location.x = width
            #self.velocity.x *= -1
            self.crashed = True
        elif self.location.x < 0 :
            #self.location.x = 0
            #self.velocity.x *= -1
            self.crashed = True
        if self.location.y > height :
            #self.location.y = height
            #self.velocity.y *= -1
            self.crashed = True
        elif self.location.y < 0 :
            #self.location.y = 0
            #self.velocity.y *= -1
            self.crashed = True

    def stayWithinWalls(self, dist) :
        if self.location.x < dist :
            desired = PVector(self.maxSpeed, self.velocity.y)
            steer = desired - self.velocity
            steer.limit(self.maxForce)
            self.applyForce(steer)
        if self.location.x > width - dist :
            desired = PVector(-self.maxSpeed, self.velocity.y)
            steer = desired - self.velocity
            steer.limit(self.maxForce)
            self.applyForce(steer)
        if self.location.y < dist :
            desired = PVector(self.velocity.x, self.maxSpeed)
            steer = desired - self.velocity
            steer.limit(self.maxForce)
            self.applyForce(steer)
        if self.location.y > height - dist :
            desired = PVector(self.velocity.x, -self.maxSpeed)
            steer = desired - self.velocity
            steer.limit(self.maxForce)
            self.applyForce(steer)

    def calcFitness(self) :
        if self.reached == False and self.crashed == False:
            d = PVector.dist(self.location, self.target)
            self.fitness = 1/d