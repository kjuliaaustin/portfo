from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# @app.route('/index.html')
# def index():
#     return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/work1.html')
# def work1():
#     return render_template('work1.html')

# @app.route('/work2.html')
# def work2():
#     return render_template('work2.html')

# @app.route('/work3.html')
# def work3():
#     return render_template('work3.html')