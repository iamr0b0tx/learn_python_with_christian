##import numpy
import numpy as np

dataset = np.genfromtxt('FL_insurance_sample.csv', delimiter=',', dtype=None)
# dataset = np.genfromtxt('FL_insurance_sample.csv', delimiter=',', dtype=[('f0', '<i4'), ('f1', '<f8'), ('f2', '|S14')])
print(dataset)