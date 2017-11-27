from django.shortcuts import render, get_object_or_404
from .models import Lesson, Topic, Test
from .forms import PythonCodeInput
from .python_tests import TestEnclosure
import os


def index(request):
    lessons = Lesson.objects.all()
    return render(request, 'fizzbuzz/index.html', {'lessons': lessons})


def lesson(request, topic):
    topic_id = Topic.objects.filter(name=topic)
    lesson = get_object_or_404(Lesson, topic=topic_id)
    return render(request, 'fizzbuzz/lesson.html', {'lesson': lesson})


def test(request, topic):
    """

    :param request:
    :param topic:
    :type topic: str
    :return:
    """
    passed = None
    topic_id = Topic.objects.filter(name=topic)
    test = get_object_or_404(Test, topic=topic_id)
    result = None
    correct = None

    if request.method == 'POST':
        # make a session so we can keep user's work isolated
        if not request.session.get('has_session'):
            request.session['has_session'] = True

        form = PythonCodeInput(request.POST)
        if form.is_valid():
            # get a session key to keep the script files unique between users
            session_key = request.session.session_key

            # get and write the user's code to a file so another script can later run it
            input_code = form.cleaned_data['code_text']
            filename = '/home/nap/fizzbuzzcert/fizzbuzz/python_tests/scratch{}.py'.format(session_key)
            with open(filename, mode='w') as file:
                file.write(input_code)

            scratch_module_name = 'scratch{}'.format(session_key)
            result, correct = TestEnclosure.SandboxedPython.run_script_call_self(
                scratch_module_name=scratch_module_name, test=topic.lower())
            os.remove(filename)

    else:
        code_text = """class Solution:
    def {}():
        """.format(topic.lower())
        form = PythonCodeInput(initial={'code_text': code_text})

    return render(request, 'fizzbuzz/test.html', {'test': test, 'form': form, 'result': result, 'correct': correct})
