import os
import torch
from torch.utils.data import Dataset
from utils import loadjson
from tokenizer import Tokenizer

class TranslationDataset(Dataset):
    def __init__(self, data_dir, source, target) -> None:
        super().__init__()
        self.data = loadjson(os.path.join(data_dir, "train.json"))
        self.tker = Tokenizer(os.path.join(data_dir))
        self.len = len(self.data)
        self.source = source
        self.target = target
    
    def __getitem__(self, index):
        x = self.tker.stc_2_idx(self.data[index][self.source], self.source)
        label = self.tker.stc_2_idx(self.data[index][self.target], self.target)

        x = torch.tensor(x)
        label = torch.tensor(label)
        return x, label
    
    def __len__(self):
        return self.len

if __name__ == "__main__":
    data_dir = "./data/small_data/train"
    train_set = TranslationDataset(data_dir, "en", 'zh')
    print(train_set.__getitem__(5))