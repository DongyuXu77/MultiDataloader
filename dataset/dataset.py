class TestDataset(object):
    def __init__(self, fake_len :int=10):
        self.len = fake_len

    def __len__(self):
        return self.len

    def __getitem__(self, fake_index):
        return fake_index
