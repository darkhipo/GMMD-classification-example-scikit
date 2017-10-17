# GMMD Classification Example with Scikit
A starting point from scikit for getting a generic classifier independent of starting class assumption. 

## Resources
* Tools, http://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_sin.html#sphx-glr-auto-examples-mixture-plot-gmm-sin-py
* Data example, https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29

## Install

### OS Environment
* Ubuntu 16.04
* Python 2.7
* Git

### Instructions 
```bash
sudo apt-get install python-pip ;
sudo pip install virtualenv ;
mkdir ~/VENV ;
cd ~/VENV ;
virtualenv -p python2.7 GMMD ;
source ~/VENV/GMMD/bin/activate ;
mkdir ~/GMMD ;
cd ~/GMMD ;
git clone https://github.com/darkhipo/GMMD-classification-example-scikit ;
cd GMMD-classification-example-scikit ;
pip install requirements.txt ;
```

## Execution

### Start Up
```bash
cd ~/GMMD/GMMD-classification-example-scikit ;
python ./bmmd.py ;
```

### Shut Down
```bash
deactivate
```
