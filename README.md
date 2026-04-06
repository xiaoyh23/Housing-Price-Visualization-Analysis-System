# 中国历年房价动态热力图 (China-House-Price-Visualization) 🏠📊

### 🚀 项目简介
本项目是一个基于 Python 的数据分析与可视化实践，利用 **Pyecharts** 库对 2012 年至 2021 年间中国各省份的平均房价进行了多维度分析。通过动态热力地图的形式，直观地展示了十年间全国房地产市场的价格演变与区域差异。

### 💡 核心价值
* **时空演变分析**：利用 Pyecharts 的 `Timeline`（时间轮播图）组件，实现了跨越 10 年的数据动态切换，一眼识别房价上涨的拐点与高峰期。
* **空间布局洞察**：通过 `Map` 组件的颜色梯度，清晰识别出京津冀、长三角、珠三角等核心增长极的辐射效应。
* **交互式体验**：支持鼠标悬浮查看具体数值、视觉映射过滤（VisualMap），方便用户进行下钻式的细节观察。

### 🛠️ 技术栈
- **数据处理**: Pandas (数据清洗、透视表转换)
- **可视化引擎**: Pyecharts (基于 Echarts 的 Python 包装库)
- **Web 框架**: Flask (用于托管生成的 HTML 结果)
- **地理数据**: 内置中国省级行政区划矢量地图

### 📂 目录结构说明
- `app.py`: Flask 后端程序，负责渲染地图并启动 Web 服务。
- `house_price_analysis.py`: 数据预处理脚本，将原始数据转换为 Pyecharts 可读格式。
- `data/`: 存放 2012-2021 年全国各省房价 CSV 原始数据。
- `templates/`: 存放渲染后的 `index.html`。
- `requirements.txt`: 项目运行所需的环境依赖清单。

### ⚡ 快速开始
1.  **克隆仓库**:
    ```bash
    git clone git@github.com:xiaoyh23/China-House-Price-Visualization.git
    ```
2.  **创建并激活虚拟环境**:
    ```bash
    python -m venv .venv
    source .venv/Scripts/activate  # Windows 用户
    ```
3.  **一键安装依赖**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **启动可视化页面**:
    ```bash
    python app.py
    ```
    访问浏览器 `http://127.0.0.1:5000` 即可查看动态热力图。

---

> **项目亮点备注**：
> 在数据清洗阶段，本项目对部分缺失的省份数据进行了**线性插值处理**，并统一了各年份的行政区划名称，确保了时间轴动画的连贯性与准确性。