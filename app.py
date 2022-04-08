from flask import Flask, render_template, request
import config
import blog


def page_not_found(e):
    return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        if 'form1' in request.form:
            prompt = request.form['blogTopic']
            blogT = blog.generateBlogTopics(prompt)
            blogTopicIdeas = blogT.replace('\n', '<br>')

        if 'form3' in request.form:
            prompt = request.form['blogExpander']
            blogT = blog.blogSectionExpander(prompt)
            blogExpanded = blogT.replace('\n', '<br>')

    return render_template('index.html', **locals())


@app.route('/section', methods=["GET", "POST"])
def blogSections():
    if 'form2' in request.form:
        prompt = request.form['blogSection']
        blogT = blog.generateBlogSections(prompt)
        blogSectionIdeas = "<br>".join(blogT)

    return render_template('sections.html', **locals())


@app.route('/expanded', methods=["GET", "POST"])
def blogSectionsExpended():
    if 'form2' in request.form:
        prompt = request.form['blogSection']
        blogT = blog.blogSectionExpander(prompt)
        blogSectionExpanded = blogT

    return render_template('expanded.html', **locals())


@app.route('/blog', methods=["GET", "POST"])
def blogPage():
    if request.method == 'POST':
        if 'genBlog' in request.form:
            prompt = request.form['blogTopic']
            blogArticle = blog.generateBlog(prompt)

    return render_template('blog.html', **locals())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8888', debug=True)
