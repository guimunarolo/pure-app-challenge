import factory


class ClassFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")

    class Meta:
        model = "schedule.Class"


class StudentFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")

    class Meta:
        model = "schedule.Student"

    @factory.post_generation
    def classes(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for _class in extracted:
                self.classes.add(_class)


class TeacherFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")

    class Meta:
        model = "schedule.Teacher"


class SubjectFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    teacher = factory.SubFactory(TeacherFactory)

    class Meta:
        model = "schedule.Subject"


class ScheduleFactory(factory.django.DjangoModelFactory):
    related_class = factory.SubFactory(ClassFactory)
    subject = factory.SubFactory(SubjectFactory)
    day_of_week = factory.Faker("random_int", min=1, max=7)
    hour = factory.Faker("random_int", min=0, max=23)

    class Meta:
        model = "schedule.Schedule"
