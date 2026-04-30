import random
from datetime import date, timedelta

from faker import Faker

from database import SessionLocal
from models import Grade, Group, Student, Subject, Teacher


def random_grade_date() -> date:
    start = date.today() - timedelta(days=365)
    return start + timedelta(days=random.randint(0, 365))


def seed_data() -> None:
    fake = Faker("uk_UA")

    with SessionLocal() as session:
        groups = [Group(name=f"Group-{idx}") for idx in range(1, 4)]
        session.add_all(groups)

        teachers_count = random.randint(3, 5)
        teachers = [Teacher(full_name=fake.name()) for _ in range(teachers_count)]
        session.add_all(teachers)
        session.flush()

        subjects_count = random.randint(5, 8)
        subjects = []
        for idx in range(1, subjects_count + 1):
            subject = Subject(
                name=f"Subject-{idx}",
                teacher_id=random.choice(teachers).id,
            )
            subjects.append(subject)
        session.add_all(subjects)
        session.flush()

        students_count = random.randint(30, 50)
        students = []
        for _ in range(students_count):
            student = Student(
                full_name=fake.name(),
                group_id=random.choice(groups).id,
            )
            students.append(student)
        session.add_all(students)
        session.flush()

        grades = []
        for student in students:
            grades_count = random.randint(10, 20)
            for _ in range(grades_count):
                subject = random.choice(subjects)
                grades.append(
                    Grade(
                        student_id=student.id,
                        subject_id=subject.id,
                        grade=random.randint(60, 100),
                        grade_date=random_grade_date(),
                    )
                )
        session.add_all(grades)
        session.commit()


if __name__ == "__main__":
    seed_data()
    print("Database was seeded successfully.")
