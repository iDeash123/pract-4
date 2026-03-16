from flask import Flask, render_template

app = Flask(__name__)


college = {
    'name': 'Фаховий коледж інформаційних технологій',
    'founded': 1995,
    'address': 'м. Київ, вул. Хрещатик, 10',
    'phone': '+380 44 123 45 67',
    'email': 'info@kfkit.edu.ua',
}

students = [
    {
        'id': 1,
        'name': 'Олександр Петренко',
        'group': 'КІ-21',
        'course': 2,
        'gpa': 4.8,
        'is_active': True,
        'subjects': ['Програмування', 'Бази даних', 'Веб-технології', 'Математика'],
    },
    {
        'id': 2,
        'name': 'Марія Коваленко',
        'group': 'КІ-21',
        'course': 2,
        'gpa': 3.7,
        'is_active': True,
        'subjects': ['Програмування', 'Мережі', 'Англійська мова', 'Фізика'],
    },
    {
        'id': 3,
        'name': 'Іван Шевченко',
        'group': 'КІ-22',
        'course': 1,
        'gpa': 3.2,
        'is_active': False,
        'subjects': ['Основи IT', 'Математика', 'Українська мова'],
    },
    {
        'id': 4,
        'name': 'Анна Бондаренко',
        'group': 'КІ-22',
        'course': 1,
        'gpa': 4.5,
        'is_active': True,
        'subjects': ['Основи IT', 'Веб-дизайн', 'Алгоритми', 'Англійська мова'],
    },
    {
        'id': 5,
        'name': 'Дмитро Мельник',
        'group': 'КІ-20',
        'course': 3,
        'gpa': 2.9,
        'is_active': True,
        'subjects': ['Програмування', 'Бази даних', 'Операційні системи'],
    },
]

schedule = {
    'Понеділок': [
        {'subject': 'Програмування', 'time': '08:30 – 10:05', 'type': 'лекція', 'room': '301'},
        {'subject': 'Бази даних', 'time': '10:15 – 11:50', 'type': 'практика', 'room': '205'},
    ],
    'Вівторок': [
        {'subject': 'Веб-технології', 'time': '08:30 – 10:05', 'type': 'лабораторна', 'room': '410'},
        {'subject': 'Математика', 'time': '10:15 – 11:50', 'type': 'лекція', 'room': '102'},
        {'subject': 'Англійська мова', 'time': '12:10 – 13:45', 'type': 'практика', 'room': '308'},
    ],
    'Середа': [
        {'subject': 'Алгоритми', 'time': '08:30 – 10:05', 'type': 'лекція', 'room': '301'},
    ],
    'Четвер': [
        {'subject': 'Операційні системи', 'time': '08:30 – 10:05', 'type': 'лекція', 'room': '102'},
        {'subject': 'Програмування', 'time': '10:15 – 11:50', 'type': 'лабораторна', 'room': '410'},
    ],
    "П'ятниця": [
        {'subject': 'Фізика', 'time': '08:30 – 10:05', 'type': 'лекція', 'room': '201'},
        {'subject': 'Мережі', 'time': '10:15 – 11:50', 'type': 'практика', 'room': '305'},
    ],
    'Субота': [],
    'Неділя': [],
}



@app.route('/')
def index():
    return render_template('index.html', college=college, total_students=len(students))


@app.route('/students')
def students_list():
    return render_template('students.html', students=students)


@app.route('/student/<int:student_id>')
def student_detail(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    return render_template('student.html', student=student)


@app.route('/schedule')
def schedule_page():
    return render_template('schedule.html', schedule=schedule)


@app.route('/about')
def about():
    return render_template('about.html', college=college, current_year=2026)


if __name__ == '__main__':
    app.run(debug=True)
