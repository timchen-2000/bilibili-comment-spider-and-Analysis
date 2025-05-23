# wordCloud.py
'''依赖模块
pip install jieba, pyecharts
'''
from pyecharts import options as opts
from pyecharts.charts import WordCloud
import jieba

# 读取停词表
stopwords = set()
with open('wordstop.txt', encoding='gbk') as f:
    stopwords.update([line.strip() for line in f.readlines()])

with open('danmus.csv', encoding='utf-8') as f:
    text = " ".join([line.split(',')[-1] for line in f.readlines()])

words = jieba.cut(text)
word_freq = {}
for word in words:
    if len(word) >= 2 and word not in stopwords:
        word_freq[word] = word_freq.get(word, 0) + 1

filtered_items = list(word_freq.items())
filtered_items.sort(key=lambda x: x[1], reverse=True)

c = (
    WordCloud()
    .add(
        "",
        filtered_items,
        word_size_range=[20, 120],
        textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
    )
    .render("wordcloud.html")
)
