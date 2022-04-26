# %%
from utils import *
import os

# %%
data_dir = "./data/small_data/train"

# %%
data = loadjson(os.path.join(data_dir, "train.json"))

# %%
en_word_num = 3
en_wd_2_idx = {"<BOS>":1, "<EOS>":2, "<UNK>":3}
for x in data:
    sentence = x["en"].split(' ')
    for word in sentence:
        if word not in en_wd_2_idx:
            en_word_num += 1
            en_wd_2_idx[word] = en_word_num
en_idx_2_wd = {
    v:k for k, v in en_wd_2_idx.items()
}

# %%
savejson(en_wd_2_idx, os.path.join(data_dir, "en_wd_2_idx.json"))
savejson(en_idx_2_wd, os.path.join(data_dir, "en_idx_2_wd.json"))

# %%
zh_word_num = 3
zh_wd_2_idx = {"<BOS>":1, "<EOS>":2, "<UNK>":3}
for x in data:
    for word in x["zh"]:
        if word not in zh_wd_2_idx:
            zh_word_num += 1
            zh_wd_2_idx[word] = zh_word_num
zh_idx_2_wd ={
    v:k for k,v in zh_wd_2_idx.items()
}

# %%
savejson(zh_wd_2_idx, os.path.join(data_dir, "zh_wd_2_idx.json"))
savejson(zh_idx_2_wd, os.path.join(data_dir, "zh_idx_2_wd.json"))


