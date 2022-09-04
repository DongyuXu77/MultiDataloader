import math

class NaiveDataloader(object):
    def __init__(self, dataset, batch_size: int, shuffle: bool=False, drop_last: bool=True):
        r""" NaiveDataloader : Use single process to load data
        """
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.drop_last = drop_last
        self.index = 0

    def __iter__(self):
        self.index = 0 # reset the self.index
        return self

    def __next__(self):
        if not hasattr(self, 'len'):
            self.__len__()
        if self.index >= self.len:
            raise StopIteration
        index_list = [item for item in range(self.index*self.batch_size, (self.index+1)*self.batch_size)]
        data = self._get(index_list)
        self.index = self.index+1
        return data

    def __len__(self):
        chunk_index = len(self.dataset)/self.batch_size
        self.len = math.floor(chunk_index) if self.drop_last else math.ceil(chunk_index)
        return self.len 

    def _get(self, index):
        data = self.dataset[index]
        return data
