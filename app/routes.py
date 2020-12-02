from flask import render_template
from app import app
from app.forms import SearchForm

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        flash('Search for Item: {}'.format(
            form.searchQuery.data))
        return redirect('/index')
    return render_template('index.html', title='Search', form = form)
