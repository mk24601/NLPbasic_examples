import MeCab
import pandas as pd

def tokenize(series):
    # MeCabオブジェクトの生成
    mt = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    mt.parse('')
    texts = []
    for line in series:
        text = ""
        node = mt.parseToNode(line.strip())
        while node:
            #############
            # 分かち書きパターン1
            """
            text += ' ' + str(node.surface)
            """
            # 分かち書きパターン2            
            fields = node.feature.split(",")
            if fields[0] == '名詞' or fields[0] == '動詞' or fields[0] == '形容詞':
                text += ' ' + str(fields[6])
            #############

            node = node.next
        texts.append(text)
    return texts  

def main():
    df = pd.read_csv("companies.csv")
    df['description'] = tokenize(df['description'])
    df.to_csv("companies_tokenized2.csv",index=None)
if __name__ == "__main__":
    main()