from flask import Flask, render_template, request, redirect, url_for

# Init app
app = Flask(__name__)

db = []

# URI, endpoint


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        new_task = request.form['new_task']
        if len(new_task) > 0 and new_task not in db:
            db.append(new_task)
    # context = {}
    return render_template('index.html', todo=db, name='Bin')

@app.route('/delete/<task>', methods=['GET'])
def delete(task):
    db.remove(task)
    return redirect(url_for('main'))

# Update list
@app.route('/update/<task>=<text>', methods=['GET'])
def update(task, text):
    db[int(task)-1] = text
    return redirect(url_for('main'))


if __name__ == '__main__':
    # Only in development
    app.run(debug=True)
