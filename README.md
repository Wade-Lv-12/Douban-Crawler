# 豆瓣电影TOP250爬虫

这是一个使用 Python 编写的爬虫程序，旨在抓取豆瓣网站的 **TOP 250 电影** 列表，并打印出每部电影的中文名称。爬虫程序使用了 `requests` 和 `BeautifulSoup` 库来获取和解析网页内容。该项目适用于学习如何进行网页抓取，尤其是从静态网页中提取信息的基本方法。

## 项目链接

[GitHub 仓库](https://github.com/Wade-Lv-12/Douban-Crawler)

## 安装依赖

在使用爬虫之前，你需要安装必要的 Python 库。我们使用了 `requests` 和 `beautifulsoup4` 来处理 HTTP 请求和 HTML 解析。

### 克隆项目

首先，克隆本项目到本地：

```bash
git clone https://github.com/Wade-Lv-12/Douban-Crawler.git
cd Douban-Crawler
```

### 创建虚拟环境（可选）

建议使用虚拟环境来管理项目依赖。在项目目录下创建虚拟环境：

```bash
python -m venv venv
```

激活虚拟环境：

- Windows:

	```bash
	venv\Scripts\activate
	```

- macOS/Linux:

	```bash
	source venv/bin/activate
	```

### 安装依赖

使用 `pip` 安装项目所需的依赖：

```bash
pip install -r requirements.txt
```

如果没有 `requirements.txt` 文件，你可以手动安装：

```bash
pip install requests beautifulsoup4
```

## 使用方法

### 运行爬虫

在项目目录下，执行以下命令来启动爬虫：

```bash
python scraper.py
```

程序会自动抓取豆瓣网站 TOP 250 的电影列表（共 10 页），并打印出每部电影的中文名称。

### 输出示例

执行爬虫后，终端将显示类似如下的电影标题：

```
肖申克的救赎
控方证人
这个杀手不太冷
霸王别姬
...
```

## 代码说明

### 1. **请求和解析网页**

爬虫通过 `requests.get()` 方法向豆瓣的 TOP 250 页面发送请求，获取 HTML 内容，并使用 `BeautifulSoup` 解析网页。

```python
response = requests.get(f"https://movie.douban.com/top250?start={start_num}&filter=", headers=headers)
html = response.text
soup = BeautifulSoup(html, "html.parser")
```

### 2. **提取电影标题**

爬虫提取页面中所有电影的中文标题。豆瓣电影的标题存储在 `span` 标签中，`class` 为 `title` 的元素内。

```python
all_titles = soup.findAll("span", attrs={"class": "title"})
```

程序会检查每个标题，跳过包含斜杠 `/` 的电影（即包含英文名称的电影）。

### 3. **分页处理**

爬虫处理分页问题，每次抓取一页的数据。豆瓣的每页包含 25 部电影，爬虫通过调整 `start` 参数来访问每一页。

```python
for start_num in range(0, 250, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}&filter=", headers=headers)
```

### 4. **请求头与延时**

为了模拟真实用户请求，爬虫添加了 `User-Agent` 和 `Referer` 请求头。此外，为了避免对服务器造成过多压力，爬虫在每次请求之间会等待 1 秒钟。

```python
time.sleep(1)
```

### 5. **异常处理**

爬虫还包含异常处理，能够捕获请求中的错误，并在发生问题时继续执行。

```python
try:
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}&filter=", headers=headers)
    response.raise_for_status()  # 确保响应状态是200
except requests.RequestException as e:
    print(f"请求失败: {e}")
```

## 注意事项

1. **遵守豆瓣网站的 `robots.txt`**： 本爬虫仅供个人学习和研究使用。请遵守豆瓣网站的 `robots.txt` 文件规定，避免过度抓取。
2. **反爬虫机制**： 豆瓣可能会实施反爬虫措施，如 IP 限制或验证码。如果你遇到请求被封的问题，可以尝试增加请求间隔，避免频繁访问。
3. **合法性问题**： 请确保该爬虫仅用于学习用途，不得用于商业目的或违反豆瓣的使用条款。

## 扩展功能

### 1. **保存数据到文件**

你可以修改爬虫代码，将抓取到的数据保存到 CSV、JSON 文件，或者数据库中，方便后续使用。

### 2. **抓取更多信息**

爬虫目前只抓取电影标题。如果你需要抓取其他信息（如电影评分、导演、演员等），可以扩展程序来实现。

## 结语

这是一个简单的爬虫项目，旨在帮助学习 Python 爬虫的基础。你可以通过此项目了解如何使用 `requests` 和 `BeautifulSoup` 库从网页中提取信息。你可以根据需要扩展项目，抓取更多的数据。

如果你对爬虫开发有兴趣，欢迎进一步修改和扩展此项目！如果有任何问题或建议，欢迎提出！
