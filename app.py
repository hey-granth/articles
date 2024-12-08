from flask import Flask, render_template, abort, url_for
import os
import markdown2
from pygments.formatters import HtmlFormatter
import yaml

app = Flask(__name__)

def parse_frontmatter(content):
    # Split the content into frontmatter and markdown
    parts = content.split('---', 2)
    if len(parts) == 3:
        frontmatter = yaml.safe_load(parts[1])
        markdown_content = parts[2]
    else:
        frontmatter = {}
        markdown_content = content
    return frontmatter, markdown_content

def get_articles():
    articles = []
    for article in os.listdir('articles'):
        if article.endswith('.md'):
            with open(os.path.join('articles', article), 'r', encoding='utf-8') as f:
                content = f.read()
                frontmatter, _ = parse_frontmatter(content)
                articles.append({
                    'title': frontmatter.get('title', 'Untitled'),
                    'date': frontmatter.get('date', 'No date'),
                    'slug': article.replace('.md', '')
                })

    return sorted(articles, key=lambda x: x['date'], reverse=True)

def render_markdown(article):
    try:
        with open(os.path.join('articles', article + '.md'), 'r', encoding='utf-8') as f:
            content = f.read()
            frontmatter, markdown_content = parse_frontmatter(content)
            html_content = markdown2.markdown(markdown_content, extras=['fenced-code-blocks', 'code-friendly', 'codehilite'])
            return {
                'content': html_content,
                'metadata': frontmatter
            }
    except FileNotFoundError:
        abort(404)

@app.route('/')
def index():
    articles = get_articles()
    return render_template('index.html', articles=articles)

@app.route('/article/<slug>')
def article(slug):
    article = render_markdown(slug)
    return render_template('article.html', content=article['content'], metadata=article['metadata'])

if __name__ == '__main__':
    app.run(debug=True)

