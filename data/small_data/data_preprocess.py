# %%
import json
import os
import zhconv
import random

# %%
def savejson(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    f.close()

def zh_process(s):
    q2b = {
        '，':',',
        '。':'.',
        '？':'?',
        '！':'!',
        '：':':',
        '（':'(',
        '）':')',
        '”':'"',
        '“':'"'
    }
    s = zhconv.convert(s, "zh-hans")
    for k, v in q2b.items():
        s = s.replace(k, v)
    return s

punc = set('.,?![]{}();:"\@#$%^&*+-/|\\=_~`0123456789')
def en_process(s):
    out = []
    for i, ch in enumerate(s):
        if (ch in punc) & (i>0) & (s[i-1] != ' '):
            out.append(' ' + ch)
        elif (ch != ' ') & (i>0) & (s[i-1] in punc):
            out.append(' ' + ch)
        else:
            out.append(ch)
    return ''.join(out)

# %%
raw_data_dir = "./raw"

# %%
with open(os.path.join(raw_data_dir, "english_chinese.txt"), "r") as f:
    raw_data = f.readlines()
f.close()
raw_data = [x.replace("\n","").replace("\u2019",'\'') for x in raw_data]

# %%
raw_data = [{
    "en":en_process(x[0:x.find('\t')]).lower(),
    "zh":zh_process(x[x.find('\t')+1:])
} for x in raw_data]

# %%
random.seed(1024)
random.shuffle(raw_data)

# %%
val_size = 0.2
val_num = int(len(raw_data) * val_size)
val_num

# %%
val = raw_data[0:val_num]
train = raw_data[val_num+1:]

# %%
savejson(train, "./train/train.json")

savejson(val, "./val/val.json")



