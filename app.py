import json
import os
from urllib.parse import unquote
from flask import Flask, render_template, abort
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension

app = Flask(__name__, static_folder='static')

# 讀取 JSON 檔案
def load_articles():
    with open('articles.json', mode='r', encoding='utf-8') as articles_file:
        return json.load(articles_file)

# 文章路由
@app.route('/articles')
def article_list():
    articles_data = load_articles()
    tags = sorted(set(tag for article in articles_data for tag in article['tags']))
    return render_template('articles.html', articles=articles_data, tags=tags)

# 顯示文章詳情
@app.route('/article/<title>')
def article_detail(title):
    articles = load_articles()
    article = next((a for a in articles if a['title'] == title), None)

    if article is None:
        return "文章未找到", 404

    if 'markdown_file' not in article:
        return "Markdown 文件未設定", 500

    md_path = os.path.join('articles', article['markdown_file'])
    if not os.path.exists(md_path):
        return "Markdown 文件未找到", 500

    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # 使用 Markdown 並啟用 CodeHilite 語法高亮
    html_content = markdown.markdown(md_content, extensions=['fenced_code', CodeHiliteExtension()])
    return render_template('article_detail.html', article=article, article_content=html_content)
    
# 首頁路由
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/owo')
def owo():
    return render_template('owo.html')

@app.route('/uwu')
def uwu():
    return render_template('uwu.html')

@app.route('/awa')
def awa():
    return render_template('awa.html')

@app.route('/tw1')
def tw1():
    return render_template('tw1.html')

@app.route('/fk')
def fk():
    return render_template('fk.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=20081, debug=True)
