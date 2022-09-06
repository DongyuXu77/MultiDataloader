import queue
import numpy.random as random

def worker_fn(dataset, index_queue, output_queue):
    r""" A simple way to load data asyncrounously
    """
    while True:
        try:
            index = index_queue.get(timeout=random.normal(loc=0.0, scale=0.5))
        except queue.Empty:
            continue
        output_queue.put(dataset[index])
