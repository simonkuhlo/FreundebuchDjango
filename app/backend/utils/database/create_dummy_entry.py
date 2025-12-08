#create / remove dummy user and entry
from sqlalchemy.orm import Session
from utils.secret_generator import generate_secret
from models.user import User
from models.entry import Entry
from models.answer import Answer

def create_dummy_entry(session: Session, user: User = None) -> Entry:
    if user is None:
        user = create_dummy_user(session)
    entry = Entry(
        user = user,
        secret= generate_secret(),
    )
    session.add(entry)
    session.commit()
    create_dummy_answers(session=session, entry=entry, user=user)
    session.refresh(entry)
    return entry

def create_dummy_user(session: Session) -> User:
    user = User(
        name = "Dummy User",
        admin = False,
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def create_dummy_answers(session: Session, entry:Entry, user: User) -> list[Answer]:
    answers = [create_dummy_answer(session=session, user=user, entry=entry, question_id=1),
               create_dummy_answer(session=session, user=user, entry=entry, question_id=2),
               create_dummy_answer(session=session, user=user, entry=entry, question_id=3),
               ]
    return answers

def create_dummy_answer(session: Session, user: User, entry:Entry, question_id:int) -> Answer:
    answer = Answer(
        question_id=question_id,
        user=user,
        entry = entry,
        value=f"Fake value for question #{question_id}",
    )
    session.add(answer)
    session.commit()
    session.refresh(answer)
    return answer