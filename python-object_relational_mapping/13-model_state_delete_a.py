#!/usr/bin/python3
"""Deletes all State objects containing the letter 'a' from the database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # الاتصال بالقاعدة
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # جلب جميع States التي تحتوي على الحرف "a"
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # حذفهم
    for state in states_to_delete:
        session.delete(state)

    # حفظ التغييرات
    session.commit()
    session.close()
