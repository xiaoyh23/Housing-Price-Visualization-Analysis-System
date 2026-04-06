# import pandas as pd
# import random

# # 使用地图插件最易识别的简称
# provinces = ['广东', '江苏', '浙江', '山东', '河南', '四川', '湖北', '湖南', '河北', '安徽', 
#              '北京', '上海', '重庆', '天津', '福建', '江西', '陕西', '辽宁', '吉林', '黑龙江']
# years = list(range(2012, 2022))

# data = []
# for prov in provinces:
#     for year in years:
#         price = random.randint(5000, 30000)
#         data.append([prov, year, price])

# df = pd.DataFrame(data, columns=['province', 'year', 'price'])
# df.to_csv('house_price.csv', index=False, encoding='utf-8')
# print("house_price.csv 生成成功！")

import pandas as pd
import random

# 中国完整的 34 个省级行政区名单（简称）
provinces = [
    '上海', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', 
    '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', 
    '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆', '北京', 
    '天津', '台湾', '香港', '澳门'
]
years = list(range(2012, 2022))

data = []
for prov in provinces:
    for year in years:
        # 模拟房价数据
        price = random.randint(5000, 30000)
        data.append([prov, year, price])

df = pd.DataFrame(data, columns=['province', 'year', 'price'])
df.to_csv('house_price.csv', index=False, encoding='utf-8')
print(f"成功生成 34 个省份的模拟数据，共 {len(df)} 行记录。")