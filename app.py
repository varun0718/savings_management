from flask import Flask, render_template, request, redirect

app = Flask(__name__)

expenses = []
savings = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        name = request.form['name']
        amount = float(request.form['amount'])
        date = request.form['date']
        expenses.append({'name': name, 'amount': amount, 'date': date})
        return redirect('/view_report')
    return render_template('add_expense.html')

@app.route('/add_savings', methods=['GET', 'POST'])
def add_savings():
    if request.method == 'POST':
        name = request.form['name']
        amount = float(request.form['amount'])
        date = request.form['date']
        savings.append({'name': name, 'amount': amount, 'date': date})
        return redirect('/view_report')
    return render_template('add_savings.html')

@app.route('/view_report')
def view_report():
    return render_template('view_report.html', expenses=expenses, savings=savings)

if __name__ == '__main__':
    app.run(debug=True)
