# -*- coding: utf-8 -*-
from requests import get
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

url = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoCountryMerge'
data = get(url).json()['data']['FAutoCountryMerge']['美国']['list']

dates = []
confirms = []
now_confirms = []
heals = []
deads = []

for day_data in data[35:]:
    dates.append(day_data['date'])
    confirms.append(day_data['confirm'])
    heals.append(day_data['heal'])
    deads.append(day_data['dead'])
    now_confirms.append(confirms[-1] - heals[-1] - deads[-1])

# 绘制文本
plt.figure(figsize=(11.4, 7.7))

confirm_line, = plt.plot(dates, confirms, color='#8B0000')
now_confirm_line, = plt.plot(dates, now_confirms, color='red', linestyle=':')
heal_line, = plt.plot(dates, heals, color='green', linestyle='--')
dead_line, = plt.plot(dates, deads, color='black', linestyle='-.')

# 绘制图形
my_font = FontProperties(fname=r'fonts\msyh.ttc')
plt.legend(handles=[confirm_line, now_confirm_line, heal_line, dead_line], labels=['累计确诊', '现存确诊', '治愈', '死亡'], prop=my_font)
plt.xlabel('日期', fontproperties=my_font)
plt.ylabel('人数', fontproperties=my_font)
plt.title('美国2019-nCov疫情情况', fontproperties=my_font)
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(7))

# 保存并显示统计图
plt.savefig('results/images/AmericaNCovData.png')
plt.show()
