W = 800
H = 600
JUMPPOWER = 25
GRAVITY = 2
SPEED = 10

class Dino(object):
    def __init__(self):
        self.x = width/10
        self.y = height/2
        self.xvelocity = 0
        self.yvelocity = 0
        self.width = 40
        self.height = 40
        self.img = loadImage("Dino.jpg")
        self.jump = False
    
    def update(self):
        if self.jump == True:
            self.yvelocity += GRAVITY
            self.y += self.yvelocity
        if self.y >= height/2:
            self.y = height/2
            self.jump = False        
        
    def draw(self):
        image(self.img, self.x, self.y, self.width, self.height)

class Donut(object):
    def __init__(self):
        self.x = width
        self.y = height/2
        self.xvelocity = SPEED
        self.width = 40
        self.height = 40
    
    def update(self):
        self.x -= self.xvelocity
    
    def draw(self):
        image(donutimg, self.x, self.y, self.width, self.height)

def check_collision(dino, donuts):
    global gameover
    for donut in donuts:
        if dist(dino.x, dino.y, donut.x, donut.y) < 40:
            gameover = True


def setup():
    size(W,H)
    background(0)
    global dino, donutimg, donuts, gameover, score, counter, new_donut_timing
    dino = Dino()
    donutimg = loadImage("Donut.jpg")
    donuts = []
    imageMode(CENTER)
    gameover = False
    score = 0
    counter = 0
    new_donut_timing = int(random(20,60))
    
def draw():
    global dino, score, counter, new_donut_timing
    if gameover == False:
        background(0)
        textSize(36)
        text("Score:"+str(score), 50,50)
        dino.update()
        dino.draw()
        counter += 1
        if counter == new_donut_timing:
            donuts.append(Donut())
            counter = 0
            new_donut_timing = int(random(15,40))
        for donut in donuts:
            donut.update()
            donut.draw()
            if donut.x < 0:
                score += 1
                donuts.remove(donut)
        check_collision(dino, donuts)
    else:
        textSize(48)
        text("Game Over", 50, 100)
        text("Press DOWN to play again", 50, 250)
    
def keyPressed():
    global donuts, gameover, score
    if keyCode==UP:
        if dino.jump == False:
            dino.jump = True
            dino.yvelocity = -JUMPPOWER
    if keyCode==DOWN:
        donuts = []
        gameover = False
        score = 0
