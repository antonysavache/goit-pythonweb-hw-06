from sqlalchemy import func, select
from sqlalchemy.orm import Session

from models import Grade, Group, Student, Subject, Teacher


def select_1(session: Session):
    stmt = (
        select(Student.full_name, func.round(func.avg(Grade.grade), 2).label("avg_grade"))
        .join(Grade, Grade.student_id == Student.id)
        .group_by(Student.id, Student.full_name)
        .order_by(func.avg(Grade.grade).desc())
        .limit(5)
    )
    return session.execute(stmt).all()


def select_2(session: Session, subject_id: int):
    stmt = (
        select(Student.full_name, func.round(func.avg(Grade.grade), 2).label("avg_grade"))
        .join(Grade, Grade.student_id == Student.id)
        .where(Grade.subject_id == subject_id)
        .group_by(Student.id, Student.full_name)
        .order_by(func.avg(Grade.grade).desc())
        .limit(1)
    )
    return session.execute(stmt).first()


def select_3(session: Session, subject_id: int):
    stmt = (
        select(Group.name, func.round(func.avg(Grade.grade), 2).label("avg_grade"))
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .where(Grade.subject_id == subject_id)
        .group_by(Group.id, Group.name)
        .order_by(Group.name)
    )
    return session.execute(stmt).all()


def select_4(session: Session):
    stmt = select(func.round(func.avg(Grade.grade), 2).label("avg_grade"))
    return session.execute(stmt).scalar_one()


def select_5(session: Session, teacher_id: int):
    stmt = select(Subject.name).where(Subject.teacher_id == teacher_id).order_by(Subject.name)
    return session.execute(stmt).scalars().all()


def select_6(session: Session, group_id: int):
    stmt = select(Student.full_name).where(Student.group_id == group_id).order_by(Student.full_name)
    return session.execute(stmt).scalars().all()


def select_7(session: Session, group_id: int, subject_id: int):
    stmt = (
        select(Student.full_name, Grade.grade, Grade.grade_date)
        .join(Grade, Grade.student_id == Student.id)
        .where(Student.group_id == group_id, Grade.subject_id == subject_id)
        .order_by(Student.full_name, Grade.grade_date)
    )
    return session.execute(stmt).all()


def select_8(session: Session, teacher_id: int):
    stmt = (
        select(func.round(func.avg(Grade.grade), 2).label("avg_grade"))
        .join(Subject, Subject.id == Grade.subject_id)
        .where(Subject.teacher_id == teacher_id)
    )
    return session.execute(stmt).scalar_one()


def select_9(session: Session, student_id: int):
    stmt = (
        select(Subject.name)
        .join(Grade, Grade.subject_id == Subject.id)
        .where(Grade.student_id == student_id)
        .group_by(Subject.id, Subject.name)
        .order_by(Subject.name)
    )
    return session.execute(stmt).scalars().all()


def select_10(session: Session, student_id: int, teacher_id: int):
    stmt = (
        select(Subject.name)
        .join(Grade, Grade.subject_id == Subject.id)
        .where(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
        .group_by(Subject.id, Subject.name)
        .order_by(Subject.name)
    )
    return session.execute(stmt).scalars().all()
