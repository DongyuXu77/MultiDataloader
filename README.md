During the internship in ByteDance, I implement an independent Dataloader, which means it can be used both in PyTorch, Tensorflow and other Deep Learning frameworks. The repo **MultiDataloader** is a toy demo to show the performance gap between different dataloaders *[NaiveDataloader, MultiDataloader, ...]*. It should be noticed that the code isn't the real implement, for example, the *shuffle* function doesn't realize in this repo.

## Installation
  1. Clone the repo.
  2. Using the `cd` command go to the MultiDataloader folder.
  3. Run `sh distribute.sh` if you have installed setuptools before.
  4. After installing successfully, you can go to the `test/` to run the `test.py` *(The loader parameters are the same as PyTorch dataloader)*
 
 ## Results
   It's very difficult for me to get the accurate speed-up rate because it's hardware related, but it's for sure that the MultiDataloader boosts the loading speed.  
   I roughly test on 10,000 fake data (It doesn't really load data, just sleep 0.01s), the batch_size set to 16, num_worker set to 8 for 10 times and get average in personal computer [MacBookPro2021 10cores]. The naive_dataloader spends 7.64146s and MultiDataloader spends 1.35452s, the speed-up rate is more than **5X**.
 
 ## Reference  
   The blog [DataLoaders Explained: Building a Multi-Process Data Loader from Scratch](https://teddykoker.com/2020/12/dataloader/) inspired me a lot at the beginning.
