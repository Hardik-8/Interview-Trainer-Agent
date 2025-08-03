from flask import Flask, render_template, request

app = Flask(__name__)

qa_data = {
    "python developer": [
        {"question": "What are Python decorators?",
         "answer": "Decorators allow modifying a function’s behavior without changing its source code."},
        {"question": "What is the difference between list and tuple?",
         "answer": "Lists are mutable, whereas tuples are immutable."}
    ],
    "data analyst": [
        {"question": "What is data cleaning?",
         "answer": "Data cleaning is the process of removing or fixing incorrect, incomplete, or irrelevant data."},
        {"question": "Explain correlation vs causation.",
         "answer": "Correlation is a mutual relationship, while causation means one variable causes the other to change."}
    ]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    output = []
    if request.method == 'POST':
        role = request.form['role'].lower()
        output = qa_data.get(role, [{"question": "No data found.", "answer": "Try another role."}])
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
