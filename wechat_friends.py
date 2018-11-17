#@TIME :2018/6/13  21:11
import re,os,time
import itchat
import jieba
import numpy as np
import pandas as pd
import seaborn as sns
from collections import defaultdict
import matplotlib.pyplot as plt
from pyecharts import  Map, Style, Page
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import PIL.Image as Image
#1.获取好友信息
#2.性别占比图
#3.地域占比水平柱状图
#4.个性签名词云图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题-设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
########################1.登录 好友基本信息#########################
itchat.auto_login()
friends = itchat.get_friends(update=True)
df_firends = pd.DataFrame(friends)

def get_attr(friends, key):
    return list(map(lambda user: user.get(key), friends))
#函数 获取好友基本信息，以字典格式存储，  昵称，备注，性别，个性签名，省份，城市
def friends_info(friends):
    for i in friends:
        province_list = []
        user = dict(Province=get_attr(friends, "Province"),
                   city=get_attr(friends, "City"),
                   nickname=get_attr(friends, "NickName"),
                   Sex=get_attr(friends, "Sex"),
                   signature=get_attr(friends, "Signature"),
                   remarkname=get_attr(friends, "RemarkName")
                    )
    print(user)
    return user
########################2.性别占比图#########################
firends_num = len(friends) #好友数量

def sex_info(user):
    sex = df_firends['Sex']
    sex_count = sex.value_counts()

    # sex = pd.DataFrame.from_dict(user, orient='index').T
    # sex_cnt = sex.groupby('Sex', as_index=True, )['Sex'].count().sort_values()
    # sex_attr = list(map(lambda x: x if x != '' else '未知', list(sex_cnt.index)))
    # print(sex_attr , list(sex_count))

    x = np.array(['male','female','unknown'])
    sns.barplot(x,sex_count,palette='Pastel2')
    plt.title("Gender Distribution")
    plt.show()
    plt.savefig('性别占比图')
    # return sex_attr,list(sex_cnt)

########################3.地域占比水平柱状图#########################

def prov_info(user):
    province = pd.DataFrame.from_dict(user,orient='index').T
    prv_cnt = province.groupby('Province',as_index=True,)['Province'].count().sort_values()
    attr = list(map(lambda x: x if x != '' else '未知', list(prv_cnt.index)))

    print(attr,list(prv_cnt))
    sns.barplot(y = attr,x =list(prv_cnt) ,orient='h',palette='rainbow')
    plt.xticks(rotation='horizontal')
    plt.title('Area Distribution')
    plt.xlabel('Count')
    plt.ylabel('Area')
    plt.show()
    plt.savefig('地域占比柱状图')

    return attr,list(prv_cnt)
def prov_chart(user):

    data = prov_info(user)
    attr , value = data
    page = Page()

    chart = Map('中国地图')
    chart.add('', attr, value, is_label_show=True, is_visualmap=True, visual_text_color='#fff')
    page.add(chart)

    page.render()


#签名词云
def jieba_cut(friends):

    siglist=[]
    for i in friends:
        signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "").replace("一个","")
        rep = re.compile("1f\d+\w*|[<>/=]")
        signature = rep.sub("", signature)
        siglist.append(signature)
    text = "".join(siglist)
    words = ' '.join(signature)
    with open('signature.txt','w',encoding='utf-8') as f:
        word_list = jieba.cut(text, cut_all = True)
        word_space_split = ' '.join(word_list)
        f.write(word_space_split)
        f.close()

def draw_signature():
    text = open(u'signature.txt', encoding='utf-8').read()
    coloring = np.array(Image.open('ha.png'))

    stopwords = set(STOPWORDS)
    stopwords = stopwords.union(set(['一个','优惠','为了','优惠券','添加']))

    my_wordcloud = WordCloud(background_color="white", max_words=100,
                         mask=coloring, max_font_size=60, random_state=42, scale=2,
                         stopwords = stopwords,
                         font_path="fzktjt.ttf").generate(text)
    image_colors = ImageColorGenerator(coloring)
    plt.imshow(my_wordcloud.recolor(color_func=image_colors))
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()
    plt.savefig('词云图')

if __name__ =='__main__':
    user = friends_info(friends)
    print("您共有%d个狗子"%firends_num)
    # sex_info(user)
    # prov_info(user)
    # prov_chart(user)
    jieba_cut(friends)
    draw_signature()