import multiprocessing as mp
from multiprocessing import Manager, Process, Queue

class MultiDataloader(object):
    def __init__(self, dataset, batch_size: int, shuffle: bool=False, drop_last: bool=True, num_worker:int=1):
        ...
