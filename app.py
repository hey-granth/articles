from flask import Flask, render_template, abort, url_for
import os
import markdown2
from pygments.formatters import HtmlFormatter
import frontmatter

app = Flask(__name__)

def  get_articles():
    articles = []
    for article in os.listdir('articles'):
        if article.endswith('.md'):
            with open(os.path.join('articles', article),'r',encoding='utf-8') as f:
                post = frontmatter.load(f)
                articles.append({
                    'title': post.get('title', 'Untitled'),
                    'date': post.get('date', 'No date'),
                    'slug': article.replace('.md', '')
                })

    return sorted(articles, key=lambda x: x['date'], reverse=True)
# returns a list of articles sorted by date in descending order

def render_markdown(article):
    try:
        with open(os.path.join('articles', article + '.md'), 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            content = markdown2.markdown(post.content, extras=['fenced-code-blocks', 'code-friendly', 'codehilite'])
            return {
                'content': content,
                'metadata': post.metadata
            }
        # returns the content of the article and its metadata in html format
    except FileNotFoundError:
        abort(404)
        # aborts the process and returns the 404 error if the file is not found

@app.route('/')
def index():
    articles = get_articles()
    return render_template('index.html', articles=articles)

@app.route('/article/<slug>')
def article(slug):
    filename = f'{slug}.md'
    article = render_markdown(filename)
    return render_template('article.html', content=article['content'], metadata=article['metadata'])



# to run the flask app, just run the command ```flask --app app.py --debug run``` in the terminal