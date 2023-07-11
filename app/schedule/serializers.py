from rest_framework import serializers

from schedule.models import Class, Schedule, Subject, Teacher


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ("name",)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("name",)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("name",)


class ScheduleSerializer(serializers.ModelSerializer):
    related_class = serializers.SerializerMethodField()
    subject = SubjectSerializer()
    teacher = TeacherSerializer(source="subject.teacher")

    class Meta:
        model = Schedule
        fields = ("day_of_week", "hour", "related_class", "subject", "teacher")

    def get_related_class(self, instance):
        class_data = ClassSerializer(instance.related_class).data
        # TODO: not 100% happy with this solution but I didn't find a better
        # way to inject this to ClassSerializer without extra queries.
        class_data["student_count"] = instance.class_student_count

        return class_data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # TODO: this looks hacky, I would rather change this name requirement
        # because it's a reserved word.
        data["class"] = data.pop("related_class")

        return data
