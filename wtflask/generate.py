import random

# generate random int between given numbers
class Randomizer:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def make_random_number(self):
        return random.randint(self.start, self.end)


# generate prediction based on given list of numbers
class Predictor:
    def __init__(self, given_numbers):
        self.train = given_numbers
    def make_prediction(self):
        next_step = round((self.train[-1] - self.train[0]) / (len(self.train)-1))
        prediction = self.train[-1] + next_step
        return prediction
