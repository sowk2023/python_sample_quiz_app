from flask import Flask, render_template, request

app = Flask(__name__)

# Sample quiz questions
questions = [
    {
        'question': "1. How do you create a comment in Python?",
        'options': ['//', '#', '/* ',
                    '<!--  -->'],
        'answer': '# This is a comment'
    },
    {
        'question': "2. What is the output of print(""Hello, World!""[7:])?",
        'options': ['Hello,', 'World!', 'Hello, World!', 'Error'],
        'answer': 'World!'
    },
    {
        'question': "3. Which of the following is a mutable data type in Python?",
        'options': ['tuple', 'list', 'str', 'int'],
        'answer': 'list'
    },
    {
        'question': "4. How do you start a block of code in Python?",
        'options': ['{ }', 'indentation', ':', '()'],
        'answer': 'indentation'
    }
]


@app.route('/')
def home():
    return render_template('quiz.html', questions=questions)


@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for i, question in enumerate(questions):
        user_answer = request.form.get(f'question-{i}')
        print(user_answer)
        if user_answer == question['answer']:
            score += 1
            print(score)

    return f'Your score: {score}/{len(questions)}'


if __name__ == '__main__':
    app.run(debug=True)
