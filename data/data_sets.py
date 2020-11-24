"""
Dataset in charge of knowing where the source of data, labels and transforms.
Should provide access to the data by indexing.
"""

import os
import pandas as pd
import numpy as np
import soundfile as sf
import torch.utils.data as data


class FolderDataset(data.Dataset):

    def __init__(self, data_arr, load_func, transforms=None):
        
        self.transforms = transforms
        self.data_arr = data_arr
        self.load_func = load_func


    def __len__(self):
        return len(self.data_arr)

    def __getitem__(self, index):

        elem = self.data_arr[index]
        data, label = self.load_func(elem['path']), elem['class_idx']

        if self.transforms is not None:
            audio, sr, label = self.transforms.apply(data, label)
            check = audio
            check = check.tolist()
            if check[3][0] == 0 and check[100][0]==0 and check[-1][0]==0:
                print(audio)
                print(label)
                return [[-0.005443328060209751],[-0.006913329008966684], [-0.0075414907187223434]], sr, 0

            else :
                return audio, sr, label

        return data, label




if __name__ == '__main__':

    pass










