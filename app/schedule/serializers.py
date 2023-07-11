from rest_framework import serializers

from schedule.models import Class, Schedule, Subject, Teacher


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ("name", "student_count")


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("name",)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("name",)


class ScheduleSerializer(serializers.ModelSerializer):
    related_class = ClassSerializer()
    subject = SubjectSerializer()
    teacher = TeacherSerializer(source="subject.teacher")

    class Meta:
        model = Schedule
        fields = ("day_of_week", "hour", "related_class", "subject", "teacher")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # TODO: this looks hacky, I would try to change this name requirement
        data["class"] = data.pop("related_class")

        return data
