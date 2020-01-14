#!/usr/bin/env python
# coding: utf-8

# In[2]:


import feedparser
jma_news = feedparser.parse("http://www.jma-net.go.jp/rss/jma.rss")

print(jma_news['feed']['title'])

for article in jma_news['entries']:
  print(f'  タイトル: {article.get("title")}')
  print(f'  リンク: {article.get("link")}')
  print(f'  日付: {article.get("published")}')
  print(f'  概要: {article.get("summary")}')
  print()


# In[3]:


import feedparser
rss_news = feedparser.parse("https://kakuyasu-sim.jp/feed")

#フィードのタイトルを表示
print(rss_news['feed']['title'])

#要素を取り出す
#概要をキレイに出力できないか？
for article in jma_news['entries']:
  print(f'  タイトル: {article.get("title")}')
  print(f'  リンク: {article.get("link")}')
  print(f'  日付: {article.get("published")}')
  print(f'  概要: {article.get("summary")}')
  print()

