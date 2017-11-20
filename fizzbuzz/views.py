from django.shortcuts import render, get_object_or_404
from .models import Lesson, Topic, Test


def index(request):
    lessons = Lesson.objects.all()
    return render(request, 'fizzbuzz/index.html', {'lessons': lessons})


def lesson(request, topic):
    topic_id = Topic.objects.filter(name=topic)
    lesson = get_object_or_404(Lesson, topic=topic_id)
    return render(request, 'fizzbuzz/lesson.html', {'lesson': lesson})


def test(request, topic):
    topic_id = Topic.objects.filter(name=topic)
    test = get_object_or_404(Test, topic=topic_id)
    return render(request, 'fizzbuzz/test.html', {'test': test})
