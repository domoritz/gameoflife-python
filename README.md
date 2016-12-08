# Conway's Game of Life in Python [![Build Status](https://travis-ci.org/domoritz/gameoflife-python.svg?branch=master)](https://travis-ci.org/domoritz/gameoflife-python)

Implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life) in an infinite space in Python. Alive cells are stored in a set. To calculate the next iteration, we compute the number of neighbors for each cell that has neighbors.

Peter Norvig has a fantastic explanation in a (Jupyter Notebook](https://nbviewer.jupyter.org/url/norvig.com/ipython/Life.ipynb).

## What I liked/disliked about python

* Python syntax is easy to read and write.
* Named tuples, iterators, defaultdict, and list comprehensions are awesome.
* Writing tests is really easy.
* I wish imports would always work as expected. Why do I have to add `export PYTHONPATH='.'` to run tests on travis?


## Run an example

```sh
python game_of_life.py
```


## Running the tests

Install nose and run `nosetests`.
