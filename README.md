# B站弹幕分析工具
这是一个用于获取、处理和分析B站视频弹幕的工具集。该项目可以爬取B站视频弹幕，进行情感分析、主题建模和高光时刻检测

### Dependencies
```bash
pip install requests snownlp pyecharts jieba gensim pyLDAvis
```

### 1. data_anlysis.py

爬取B站视频弹幕的主要脚本：
- 通过视频URL获取视频的oid（cid）
- 使用B站API获取弹幕数据
- 将原始弹幕数据保存为XML文件

### 2. processing.py

处理原始弹幕数据：
- 读取XML格式的弹幕文件
- 使用正则表达式提取弹幕内容和属性
- 将处理后的数据保存为CSV格式

### 3. emotionAnalysis.py

弹幕情感分析：
- 使用SnowNLP进行中文情感分析
- 将弹幕分类为积极、消极和中性
- 生成情感分布饼图

### 4. highlights.py

视频高光时刻分析：
- 统计不同时间点的弹幕密度
- 生成弹幕密度随时间变化的折线图
- 标记弹幕密度最高的时间点（可能的高光时刻）

### 5. LDA_annly.py

弹幕主题建模：
- 使用结巴分词处理中文弹幕
- 应用LDA（潜在狄利克雷分配）进行主题建模
- 生成主题可视化HTML文件

## Quick Start
1. 运行`data_anlysis.py`获取弹幕数据 # 通过视频的URL进行获取
2. 运行`processing.py`进行数据预处理
3. 根据需求运行分析脚本：
   - `emotionAnalysis.py`：情感分析
   - `highlights.py`：高光时刻检测
   - `LDA_annly.py`：主题建模分析
* `Note`: 只能爬取url为video类型的视频like：https://www.bilibili.com/video/BV18sJHz5ENR/?spm_id_from=333.934.0.0
* `Note`: 需要准备`wordstop.txt`作为中文停用词表（用于LDA主题建模）
* `Note`: 分析结果会以HTML文件形式保存在项目目录中

