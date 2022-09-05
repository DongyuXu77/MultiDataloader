During the internship in ByteDance, I implement an independent Dataloader which can be used both in PyTorch, Tensorflow and other Deep Learning frameworks. The repo ***MultiDataloader*** is a toy demo to show the performance gap between different dataloaders *[NaiveDataloader, MultiDataloader, ...]*. It should be noticed that the code isn't the real implement, for example, the *shuffle* function doesn't implement in this repo.

## Installation
  1. Clone the repo.
  2. Using `cd` command go to the `MultiDataloader/` folder.
  3. Run `sh distribute.sh` if you have installed setuptools before.
  4. After installing successfully, you can go to the `test/` and run `test.py` *(The loader parameters are the same as PyTorch dataloader)*
   
  ## Theoretical speed-up rate
   Let's assume loading batch_size data costs $C_l$ second, training in one step costs $C_t$ second.  
   If $C_l \lt C_t$:  
   &ensp;&ensp; $T_M=C_l+C_t*n$ &emsp;&ensp;  $n$ is the training steps for each epoch &emsp; $M$ denotes for MultiDataloader  
   &ensp;&ensp; $T_N=(C_l+C_t)*n$ &ensp; $N$ denotes for NaiveDataloader  
   &ensp;&ensp; $S_{rate} = \frac{T_N}{T_M} = \frac{(C_l+C_t)n}{C_l+nC_t}$ &emsp; $S_{rate}$ is the theoretical speed-up rate
    
 ## Experiments
   It's very difficult to get the accurate speed-up rate because it's hardware related, but it's for sure that the MultiDataloader boosts the loading speed.  
   I roughly test on 10,000 fake data (It doesn't really load data, just sleep 0.01s), the batch_size set to 16, num_worker set to 8 for 10 times and get average in personal computer *[MacBookPro2021 10cores]*. The naive_dataloader spends 6.86533s and MultiDataloader spends 0.87841s, the speed-up rate is more than **7X**.  
 
 ## Reference  
   The blog [DataLoaders Explained: Building a Multi-Process Data Loader from Scratch](https://teddykoker.com/2020/12/dataloader/) inspired me a lot at the beginning.
