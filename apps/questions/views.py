from requests import get as get_req
from flasgger import swag_from
from flask import request, Response
from core import Config
from .models import Question, db


@swag_from(Config.SWAGGER_FORMS + 'index.yml')
def index():
    previous_questions = db.session.query(Question).filter_by(was_shown=False)
    response_data = list()
    for question_obj in previous_questions:
        response_data.append(question_obj.serialize())
        question_obj.was_shown = True
        db.session.add(question_obj)

    questions_num = request.json["questions_num"]
    while questions_num > 0:
        questions = get_req(f'https://jservice.io/api/random?count={questions_num}').json()
        for question in questions:
            question_obj = Question(
                id=question['id'],
                question_text=question["question"],
                answer_text=question["answer"],
                created_at=question["created_at"]
            )
            if Question.query.filter_by(id=question['id']).first() is not None:
                continue
            db.session.add(question_obj)
            questions_num -= 1

    db.session.commit()
    return response_data
