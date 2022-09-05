import math
import queue
import multiprocessing as mp
from multiprocessing import Manager, Process, Queue

from .naive import NaiveDataloader
from .utils.function import worker_fn

mp.set_start_method("fork") # Operating System related

class MultiDataloader(NaiveDataloader):
    def __init__(self, dataset, batch_size: int, shuffle: bool=False, drop_last: bool=True, num_worker: int=1):
        super().__init__(dataset, batch_size, shuffle, drop_last)
        self.num_worker = num_worker
        self.data_queue = Queue()
        self.index_queue = [Queue() for _ in range(self.num_worker)]
        self.worker = [Process(target=worker_fn, args=(self.dataset, self.index_queue[index], self.data_queue)) for index in range(self.num_worker)]
        for worker in self.worker:
            worker.daemon = True
            worker.start()
        self._prefetch()

    def _prefetch(self):
        if not hasattr(self, 'len'):
            self.__len__()
        times = self.len/self.num_worker
        if times!=int(times):
            times = math.ceil(times)
        for time in range(int(times)+1):
            for worker_id in range(self.num_worker):
                index_pointer = time*self.num_worker*self.batch_size
                self.index_queue[worker_id].put([l for l in range(index_pointer+worker_id*self.batch_size, min(index_pointer+(worker_id+1)*self.batch_size, len(self.dataset)))])
                if len(self.dataset) < index_pointer+(worker_id+1)*self.batch_size:
                    break

    def __next__(self):
        if not hasattr(self, 'len'):
            self.__len__()
        if self.index >= self.len:
            raise StopIteration
        data = self._get(self.index)
        self.index = self.index+1
        return data
        
    def _get(self, fake_index):
        while True:
            try:
                data  = self.data_queue.get()
            except queue.Empty:
                continue
            break
        return data
