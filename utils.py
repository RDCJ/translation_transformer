import json
import zhconv

def savejson(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    f.close()


def loadjson(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    f.close()
    return data

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

def en_process(s):
    punc = set('.,?![]{}();:"\@#$%^&*+-/|\\=_~`0123456789')
    out = []
    for i, ch in enumerate(s):
        if (ch in punc) & (i>0) & (s[i-1] != ' '):
            out.append(' ' + ch)
        elif (ch != ' ') & (i>0) & (s[i-1] in punc):
            out.append(' ' + ch)
        else:
            out.append(ch)
    return ''.join(out)