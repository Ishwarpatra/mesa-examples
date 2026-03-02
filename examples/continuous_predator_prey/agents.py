import math
from mesa.experimental.continuous_space import ContinuousSpaceAgent

class Prey(ContinuousSpaceAgent):

    "a prey create which hase very random motion the a continous space"
    def __init__(self, unique_id, space, model, pos, speed=1.0):
        # ContinuousSpaceAgent requires (space, model)
        super().__init__(space, model)
        # assign the unique identifier and starting position
        self.unique_id = unique_id
        self.position = pos
        self.speed = speed
    #now we need make it motion randomso we need move agent to random position based it's spee
    def random_move(self):
        #random angle between 0 and 2pi would taken 
        angle=self.random.uniform(0,2*math.pi)
        #change in x and y by trigonometry
        dx=math.cos(angle)*self.speed
        dy=math.sin(angle)*self.speed
        #NEW POSITION  calculated
        new_x=self.pos[0]+dx
        new_y=self.pos[1]+dy

        new_pos=(new_x,new_y)
        
        # to make sure it doesn't go off the map; use the new helper
        if self.model.space.torus:
            new_pos = self.model.space.torus_correct(new_pos)

        # update the stored position
        self.position = new_pos

    def step(self):
        #it calls the random move function to move the agent in each step of the simulation
        self.random_move()

class Predator(ContinuousSpaceAgent):
    "a predator agent which move move randomly but also try to catch the prey if it is nearby"

    def __init__(self, unique_id, space, model, pos, speed=1.5): #it need faster than prey to catch it
        super().__init__(space, model)
        self.unique_id = unique_id
        self.position = pos
        self.speed = speed
    
    def step(self):
        #here we make it hunt the prey if it is nearby
        #we will same random walk logic used in prey agent
        angle=self.random.uniform(0,2*math.pi)
        dx=math.cos(angle)*self.speed
        dy=math.sin(angle)*self.speed

        new_pos=(self.pos[0]+dx,self.pos[1]+dy)
        if self.model.space.torus:
            new_pos = self.model.space.torus_correct(new_pos)
        self.position = new_pos