import copy
import random
# Consider using the modules imported above.

class Hat:
    """hat method get user input and convert to list

    Atttibutes:
        **kwargs: get user input in a form of list

    Methods:
        draw: check user input is valid and note ball drawn and remove
            drawn balls form list
    """
    #get user input from a kwargs and append the key value to the list
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            while value > 0:
                self.contents.append(key)
                value -= 1

    #check if user input is correct and if it's append draw ball to a list
    #and remove from orignal list
    def draw(self, draw_num):
        if draw_num > len(self.contents):
            return self.contents
        else:
            balls_drawn = []
            balls_left = self.contents
            for i in range(draw_num):
                draw = random.randint(0, len(balls_left) - 1)
                balls_drawn.append(balls_left[draw])
                balls_left.remove(balls_left[draw])
                self.contents = balls_left
            return sorted(balls_drawn)



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  #create list of expected_balls
  exptd = []
  for k, v in expected_balls.items():
    while v > 0:
      exptd.append(k)
      v-=1
  #create results list
  results = []
  #perform experiment num_experiments times
  for i in range(num_experiments):
    #create copies of hat, exptd
    hat_n = copy.deepcopy(hat)
    exptd_n = copy.deepcopy(exptd)
    #draw from hat_n
    draw_n = hat_n.draw(num_balls_drawn)
    #ensure exptd_n is in draw_n
    exptd_in_draw = []
    for i in range(len(exptd_n)):
      if exptd_n[i] in draw_n:
        exptd_in_draw.append(True)
        draw_n.remove(exptd_n[i])
      else:
        exptd_in_draw.append(False)
    #add True if exptd_n is in hat_n, False otherwise
    if sum(exptd_in_draw) == len(exptd_n):
      results.append(True)
    else:
      results.append(False)
  #sum True counts / num_experiments for probability
  prob = sum(results)/num_experiments
  return prob