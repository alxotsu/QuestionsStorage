from core import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.VARCHAR(255), nullable=False)
    answer_text = db.Column(db.VARCHAR(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    was_shown = db.Column(db.Boolean, default=False, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'question_text': self.question_text,
            'answer_text': self.answer_text,
            'created_at': self.created_at
        }
