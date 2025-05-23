# Bilibili Danmu Analysis Tool

This is a toolkit for collecting, processing, and analyzing danmu (bullet comments) from Bilibili videos. The project can crawl Bilibili video danmu, perform sentiment analysis, topic modeling, and highlight moment detection.

![Bilibili Logo](images/bilibili_logo.png)

## Dependencies

The project depends on the following Python libraries:

```bash
pip install requests snownlp pyecharts jieba gensim pyLDAvis
```

## Project Files Description

### 1. data_anlysis.py

Main script for crawling Bilibili video danmu:
- Obtains the video's oid (cid) through the video URL
- Uses Bilibili API to get danmu data
- Saves the raw danmu data as an XML file

### 2. processing.py

Processes the raw danmu data:
- Reads the XML format danmu file
- Extracts danmu content and attributes using regular expressions
- Saves the processed data in CSV format

### 3. emotionAnalysis.py

Danmu sentiment analysis:
- Uses SnowNLP for Chinese sentiment analysis
- Categorizes danmu as positive, negative, or neutral
- Generates a pie chart of sentiment distribution

Example output:
![Sentiment Analysis](images/emotion_analysis.png)

### 4. highlights.py

Video highlight moment analysis:
- Counts danmu density at different timestamps
- Generates a line chart of danmu density over time
- Marks the timestamps with highest danmu density (potential highlight moments)

Example output:
![Highlight Detection](images/highlights.png)

### 5. LDA_annly.py

Danmu topic modeling:
- Processes Chinese danmu using Jieba word segmentation
- Applies LDA (Latent Dirichlet Allocation) for topic modeling
- Generates an HTML visualization of the topics

Example output:
![Topic Modeling](images/lda_topics.png)

## Usage Process

1. Run `data_anlysis.py` to collect danmu data
2. Run `processing.py` to process the raw data
3. Run analysis scripts according to your needs:
   - `emotionAnalysis.py`: Sentiment analysis
   - `highlights.py`: Highlight moment detection
   - `LDA_annly.py`: Topic modeling analysis

## Notes

- A `wordstop.txt` file is required as a Chinese stopwords list (for LDA topic modeling)
- Analysis results will be saved as HTML files in the project directory
- You can place your analysis result screenshots in the `images` folder to include them in this README 