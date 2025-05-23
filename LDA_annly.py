import re
import jieba
from gensim import corpora, models
import pyLDAvis.gensim_models as gensimvis
import pyLDAvis
import warnings

# 忽略警告信息
warnings.filterwarnings("ignore", category=DeprecationWarning)

# 读取弹幕文本数据
with open('danmus.csv', encoding='utf-8') as f:
    text = [line.split(',')[-1] for line in f.readlines()[1:]]

# 读取停词表
stopwords = set()
with open('wordstop.txt', encoding='gbk') as f:
    stopwords.update([line.strip() for line in f.readlines()])

# 文本预处理：分词、去除停用词
def preprocess_text(text):
    word_list = []
    for sentence in text:
        # 使用正则表达式去除特殊符号等非中文字符
        sentence = re.sub(r'[^\u4e00-\u9fa5]', '', sentence)
        seg_list = jieba.cut(sentence)
        seg_list = [word for word in seg_list if word not in stopwords and len(word) > 1]  # 去除停用词和单字词
        word_list.append(seg_list)
    return word_list

# 对文本进行预处理
processed_text = preprocess_text(text)

# 构建词典和语料库
dictionary = corpora.Dictionary(processed_text)
corpus = [dictionary.doc2bow(text) for text in processed_text]

# 训练LDA模型
lda_model = models.LdaModel(corpus, num_topics=3, id2word=dictionary, passes=20)

# 输出各个主题的词分布
for topic_id, topic_words in lda_model.print_topics(num_words=10):
    print(f"Topic {topic_id}: {topic_words}")

# 获取文档对应的主题分布
doc_topics = [lda_model[doc] for doc in corpus]

# 准备测试数据
test_text = ["这是一条测试弹幕", "真的好感动啊", "而你，我的朋友，是真正的英雄！！"]

# 对测试数据进行预处理和词典转换
processed_test = preprocess_text(test_text)
test_corpus = [dictionary.doc2bow(text) for text in processed_test]

# 应用LDA模型获取测试数据的主题分布
test_doc_topics = [lda_model[doc] for doc in test_corpus]

# 输出测试数据的主题分布
for i, doc_topics in enumerate(test_doc_topics):
    print(f"Test Document {i}: {doc_topics}")

# 可视化主题模型
vis_data = gensimvis.prepare(lda_model, corpus, dictionary)
pyLDAvis.save_html(vis_data, 'lda_visualization.html')
pyLDAvis.display(vis_data)