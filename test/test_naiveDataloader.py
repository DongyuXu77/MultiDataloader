from loader import NaiveDataloader
from dataset import TestDataset
def test():
    dataset = TestDataset(fake_len=100)
    dataloader = NaiveDataloader(dataset, batch_size=16)
    for _ in dataloader:
        ...

if __name__=="__main__":
    test()
