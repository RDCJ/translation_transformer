# %%
import json
import os
import jieba
import re
from tqdm import tqdm

# %%
def savejson(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    f.close()

# %%
raw_data_dir = "./data/raw"

# %%
with open(os.path.join(raw_data_dir,"train.en"), "r", encoding="utf-8") as f:
    train_en = f.readlines()
train_en = [re.sub('\n', '', x) for x in train_en]

# %%
punc = set('.,?![]{}();:"\'@#$%^&*+-/|\\=_~`')

# %%
def preprocess_sentence(sentence):
    out = []
    #sentence = sentence.encode('utf_8').decode("unicode_escape").encode('latin1').decode('utf-8')
    for i, ch in enumerate(sentence):
        if (ch in punc) & (i>0) & (sentence[i-1] != ' '):
            out.append(' ' + ch)
        elif (ch != ' ') & (i>0) & (sentence[i-1] in punc):
            out.append(' ' + ch)
        else:
            out.append(ch)
    return ''.join(out)
    

# %%
train_en = [
    preprocess_sentence(x).lower().split(' ')
    for x in tqdm(train_en)
]
try:
    savejson(train_en, "./data/train_en.json")
except:
    pass

# %%
en_idx_2_wd = {}
en_wd_2_idx = {}
word_num = 0
for sentence in tqdm(train_en):
    for word in sentence:
        if word not in en_wd_2_idx:
            word_num += 1
            en_wd_2_idx[word] = word_num
            en_idx_2_wd[word_num] = word

# %%
savejson(en_wd_2_idx, "./data/en_word_2_index.json")
savejson(en_idx_2_wd, "./data/en_index_2_word.json")



