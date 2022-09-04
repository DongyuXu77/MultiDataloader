from dataset.dataset import TestDataset
from loader.naive import NaiveDataloader
from loader.multi import MultiDataloader

def test():
    dataset = TestDataset(fake_len=100)
    dataloader_naive = NaiveDataloader(dataset, batch_size=16, drop_last=False)
    dataloader_multi = MultiDataloader(dataset, batch_size=16, drop_last=False)
    print(len(dataloader_naive))
    for data in dataloader_naive:
        print(data)
    print('#'*100)
    for data in dataloader_multi:
        print(data)

if __name__=="__main__":
    test()
