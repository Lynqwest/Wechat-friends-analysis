# Wechat-friends-analysis
A project to analyze wechat friends
# 微信朋友分析<br>
通过 itchat 接口实现对微信朋友信息的抓取， 共实现以下功能：<br>

### 1. 获取好友信息
  通过itchat的het_friends得到朋友信息，经过清洗得到需要的数据：昵称，备注，性别，个性签名，省份，城市<br>
### 2. 性别占比图
  sns柱状图画出男女占比
### 3. 地域占比水平柱状图
  pyechart的中国省份地图画出每个省份的朋友占比
### 4. 个性签名词云图
  抓取所有个性签名，通过结巴分词，抓出关键词，去除无用词，wordcloud画出词云
  
 # A project to analyze wechat friends
### 1. Get friends' info
    Get info which include nicknames,remarks,sex,signature,province,city by API itchat 
### 2.Sex ratio barchart 
    sex comparison barchat by seaborn
### 3. Province ratio barchart
    Friends from different provinces in China map by pyechart
### 4. Signature wordcloud
    All friends' signature cut by jieba,get the keywords and drew by wordcloud
 
<br><br>
### Result <br>
![province_ratio](https://github.com/Lynqwest/Wechat-friends-analysis/blob/master/Result%20img/Figure_3.png)
![sex_ratio](https://github.com/Lynqwest/Wechat-friends-analysis/blob/master/Result%20img/gender2.png)
![china_map](https://github.com/Lynqwest/Wechat-friends-analysis/blob/master/Result%20img/%E4%B8%AD%E5%9B%BD%E5%9C%B0%E5%9B%BE.png)
![signature_wordcloud](https://github.com/Lynqwest/Wechat-friends-analysis/blob/master/Result%20img/%E7%BB%93%E5%B7%B42.png)
