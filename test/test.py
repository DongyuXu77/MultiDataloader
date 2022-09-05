import time
from multiprocessing import Manager, Process

from dataset.dataset import TestDataset
from loader.naive import NaiveDataloader
from loader.multi import MultiDataloader

BATCH_SIZE = 16
def train_with_naive(dataset, dataset_len):
    dataloader_naive = NaiveDataloader(dataset, batch_size=BATCH_SIZE, drop_last=False)
    start_time = time.time()
    for _ in dataloader_naive:
        ...
    naive_time = time.time()-start_time
    print(f"naive_time (dataset_len:{dataset_len} batch_size:{BATCH_SIZE}): {naive_time: .4f}")
    
def train_with_multi(dataset, dataset_len):
    dataloader_multi = MultiDataloader(dataset, batch_size=BATCH_SIZE, drop_last=False, num_worker=8)
    start_time = time.time()
    for _ in dataloader_multi:
        ...
    multi_time = time.time()-start_time
    print(f"multi_time (dataset_len:{dataset_len} batch_size:{BATCH_SIZE}): {multi_time: .4f}")

def test():
    dataset_len = [1000*time for time in range(10, 11)]
    for index_1 in range(len(dataset_len)):
        process_1 = Process(target=train_with_naive, args=(TestDataset(fake_len=dataset_len[index_1]), dataset_len[index_1], ), )
        process_2 = Process(target=train_with_multi, args=(TestDataset(fake_len=dataset_len[index_1]), dataset_len[index_1], ), )
        process_list = [process_1, process_2]
        for index in range(len(process_list)):
            process_list[index].start()

if __name__=="__main__":
    test()
