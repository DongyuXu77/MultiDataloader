from loader.naive import NaiveDataloader
from dataset.dataset import TestDataset
def test():
    dataset = TestDataset(fake_len=100)
    dataloader = NaiveDataloader(dataset, batch_size=16, drop_last=False)
    print(len(dataloader))
    for _ in dataloader:
        ...

if __name__=="__main__":
    test()
