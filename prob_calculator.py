import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.balls = dict(kwargs)
    self.contents = []
    self.numBallsContained = 0
    keys = self.balls.keys()

    for key in keys:
      num = self.balls[key]
      for i in range(0,num):
        self.contents.append(key)
        self.numBallsContained += 1

  def draw(self, num_balls_drawn):
    if num_balls_drawn > self.numBallsContained:
      num_balls_drawn = self.numBallsContained
    drawn_balls = []
    for i in range(0, num_balls_drawn):
      index = random.randrange(self.numBallsContained)
      ball = self.contents[index]
      drawn_balls.append(ball)
      self.balls[ball] -= 1
      self.numBallsContained -= 1
      del self.contents[index]

    return drawn_balls

  def addBalls(self, balls):
    for ball in balls:
      self.contents.append(ball)
      if not(ball in self.balls):
        self.balls[ball] = 1
      else:
        self.balls[ball] += 1
      self.numBallsContained += 1

    return


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  numFails = 0
  numSuccess = 0
  expectedKeys = expected_balls.keys()

  for i in range(0, num_experiments):
    balls = {}
    drawn_balls = hat.draw(num_balls_drawn)

    for ball in drawn_balls:
      if not (ball in balls):
        balls[ball] = 1
      else:
        balls[ball] += 1
    
    success = True
    for key in expectedKeys:
      if not key in balls:
        success = False
        break
      if expected_balls[key] > balls[key]:
        success = False
        break
    if success:
      numSuccess += 1
    else:
      numFails += 1
    
    hat.addBalls(drawn_balls)

  return numSuccess / num_experiments

