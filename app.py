import pandas as pd
from flask import Flask, render_template, jsonify
from pyecharts.charts import Map
from pyecharts import options as opts
import json
import os

app = Flask(__name__)

# 加载数据
df = pd.read_csv('house_price.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map/<int:year>')
def get_map(year):  
    year_data = df[df['year'] == year]
    
    # ECharts 官方标准名称映射表
    name_map = {
        "北京": "北京市", "上海": "上海市", "天津": "天津市", "重庆": "重庆市",
        "河北": "河北省", "山西": "山西省", "辽宁": "辽宁省", "吉林": "吉林省",
        "黑龙江": "黑龙江省", "江苏": "江苏省", "浙江": "浙江省", "安徽": "安徽省",
        "福建": "福建省", "江西": "江西省", "山东": "山东省", "河南": "河南省",
        "湖北": "湖北省", "湖南": "湖南省", "广东": "广东省", "海南": "海南省",
        "四川": "四川省", "贵州": "贵州省", "云南": "云南省", "陕西": "陕西省",
        "甘肃": "甘肃省", "青海": "青海省", "台湾": "台湾省",
        "内蒙古": "内蒙古自治区", "广西": "广西壮族自治区", "西藏": "西藏自治区", 
        "宁夏": "宁夏回族自治区", "新疆": "新疆维吾尔自治区",
        "香港": "香港特别行政区", "澳门": "澳门特别行政区"
    }

    map_data = []
    for _, row in year_data.iterrows():
        name = str(row['province']).strip()
        # 转换为 ECharts 识别的全称
        final_name = name_map.get(name, name)
        map_data.append([final_name, float(row['price'])])
    
    chart = (
        Map()
        .add("房价(元/㎡)", map_data, "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title=f"{year}年中国各省房价分布"),
            visualmap_opts=opts.VisualMapOpts(
                min_=5000, 
                max_=30000,
                range_color=["#50a3ba", "#eac736", "#d94e5d"]
            )
        )
    )
    return jsonify(json.loads(chart.dump_options()))

if __name__ == '__main__':
    app.run(debug=True)