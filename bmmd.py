#!/usr/bin/env python

import itertools
import datetime
import pprint
import sys
import os

import numpy as np
from sklearn import mixture

dataFileName = './data/breast-cancer-wisconsin.data'
delim        = ','
random_seed  = 0
data_dict    = dict({})
np.random.seed(random_seed)

##Data to NP array.
with open(dataFileName) as f:
    for line in f:
       (key, row) = line.strip().split(delim,1)
       row = row.replace('?','0') #Fill missing data.
       row = map(float, row.split(delim))
       data_dict[str(key)] = row
row_order = sorted(data_dict.keys())
rows = [ data_dict[key] for key in row_order ]
X = np.array( rows )
##Data to NP array.

##Train Unsupervised Classifier.
dpgmm = mixture.BayesianGaussianMixture(
            n_components=len(rows),
            covariance_type='full',
            weight_concentration_prior=1e-2,
            weight_concentration_prior_type='dirichlet_process',
            mean_precision_prior=1e-2,
            covariance_prior=1e0 * np.eye(len(rows[0])),
            init_params="random",
            max_iter=1000,
            random_state=random_seed).fit(X)
##Train Unsupervised Classifier.

##Predict class from the input data. 
'''
Yes it's true, in violation, of a good cross-validation.
Even more egregious still to split out test I had no will! 
I am cheating, this is true, fixing this I leave to you!
'''
predict_list = list(dpgmm.predict(X))
uniques      = sorted(set(predict_list))
result_map   = {k : predict_list[i] for (k,i) in zip(row_order, range(len(row_order)))} 

print('I found {} labels for {} rows, they are: {}'.format(len(uniques), len(rows), uniques)) 
pprint.pprint(result_map)
sys.exit(0)
