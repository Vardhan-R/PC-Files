from built_modules import import_ann as ann, import_geneticalgorithm as ga
import random

all_orgs = []
all_scores = []
orgs = 10
tests = 100

for i in range(orgs):
    all_orgs.append(ann.NeuralNetwork((1, 3)))

for i in range(tests):
    test_no = random.choice([-1, 0, 1]) * random.randint(0, 10 ** 5) / 10 ** 3
    for j in all_orgs:
        j.feedForward((test_no))
        j.best()
        ann.NeuralNetwork().best()