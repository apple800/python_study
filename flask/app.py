from flask import Flask, render_template, request, redirect, url_for

# Init app
app = Flask(__name__)

db = []


# URI, endpoint
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        new_task = request.form['new_task']
        modify_task = request.form['mo']
        num = request.form['num']

        if len(new_task) > 0 and new_task not in db:
            db.append(new_task)

        if len(modify_task) > 0 and new_task not in db:
            db[int(num)-1] = modify_task

    return render_template('index.html', todo=db, name='Bin')


@app.route('/delete/<task>', methods=['GET'])
def delete(task):
    db.remove(task)
    return redirect(url_for('main'))


# Update list
@app.route('/update/<task>', methods=['GET'])
def update(task):
    num = db.index(task)
    text = '수정'
    db[num] = text

    return redirect(url_for('main'))


if __name__ == '__main__':
    # Only in development
    app.run(debug=True)
