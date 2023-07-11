import pytest

from tests.schedule.factories import (
    ClassFactory,
    ScheduleFactory,
    StudentFactory,
    SubjectFactory,
    TeacherFactory,
)


@pytest.fixture
def school_class():
    return ClassFactory()


@pytest.fixture
def student(school_class):
    return StudentFactory(classes=[school_class])


@pytest.fixture
def subject(teacher):
    return SubjectFactory(teacher=teacher)


@pytest.fixture
def teacher():
    return TeacherFactory()


@pytest.fixture
def schedule(school_class, subject):
    return ScheduleFactory(related_class=school_class, subject=subject)
