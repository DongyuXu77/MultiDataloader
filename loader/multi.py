import multiprocessing as mp
from multiprocessing import Manager, Process, Queue

from loader import NaiveDataloader
from .utils.function import worker_fn

class MultiDataloader(NaiveDataloader):
    def __init__(self, dataset, batch_size: int, shuffle: bool=False, drop_last: bool=True, num_worker:int=1):
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
        for worker_id in range(self.num_worker):
            seld.worker_id_queue[worker_id].put([l for l in range(worker_id*self.batch_size, (worker_id+1)*self.batch_size)])

    def __next__(self):
        if not hasattr(self, 'len'):
            self.__len__()
        if self.index > self.len:
            raise StopIteration
        data = self._get(self.index)
        self.index = self.index+1
        return data
        
    def _get(self, self.fake_index):
        while True:
            data  = self.data_queue.put()
            return data
