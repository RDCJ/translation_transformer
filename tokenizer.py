# %%
from utils import *
import os

# %%
class Tokenizer():
    def __init__(self, dic_dir) -> None:
        self.idx_2_wd = {}
        self.wd_2_idx = {}
        self.idx_2_wd['en'] = loadjson(os.path.join(dic_dir, "en_idx_2_wd.json"))
        self.wd_2_idx['en'] = loadjson(os.path.join(dic_dir, "en_wd_2_idx.json"))
        self.wd_2_idx['zh'] = loadjson(os.path.join(dic_dir, "zh_wd_2_idx.json"))
        self.idx_2_wd['zh']= loadjson(os.path.join(dic_dir, "zh_idx_2_wd.json"))
        self.en_word_num = len(self.idx_2_wd['en'])
        self.zh_word_num = len(self.wd_2_idx['zh'])

    def stc_2_idx(self, stc, lang):
        if lang == 'en':
            stc = stc.split(' ')
        else:
            stc = list(stc)
        out = [self.wd_2_idx[lang]["<BOS>"]]
        for x in stc:
            if x in self.wd_2_idx[lang]:
                out.append(self.wd_2_idx[lang][x])
            else:
                out.append(self.wd_2_idx[lang]["<UNK>"])
        out.append(self.wd_2_idx[lang]["<EOS>"])
        return out
    
    def idx_2_stc(self, idxs, lang):
        out = []
        for idx in idxs:
            if str(idx) in self.idx_2_wd[lang]:
                out.append(self.idx_2_wd[lang][str(idx)])
            else:
                out.append("<UNK>")
        return out



