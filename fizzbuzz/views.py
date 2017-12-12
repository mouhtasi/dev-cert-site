from django.shortcuts import render, get_object_or_404
from .models import Lesson, Topic, Test
from .forms import PythonCodeInput, GuestUserDetailsInput
from .python_tests import TestEnclosure
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, letter
from django.http import HttpResponse
import os


def index(request):
    lessons = Lesson.objects.all()
    return render(request, 'fizzbuzz/index.html', {'lessons': lessons})


def lesson(request, topic_name):
    topic_id = Topic.objects.get(name=topic_name)
    lesson = get_object_or_404(Lesson, topic=topic_id)
    return render(request, 'fizzbuzz/lesson.html', {'lesson': lesson})


def test(request, topic_name):
    """

    :param request:
    :param topic_name:
    :type topic_name: str
    :return:
    """
    topic = Topic.objects.get(name=topic_name)
    test = get_object_or_404(Test, topic=topic)
    result = None
    correct = None
    is_student = None

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
                scratch_module_name=scratch_module_name, test=topic_name.lower())
            os.remove(filename)

            if correct:
                # if request.user.is_authenticated:
                #     is_student = True
                #     request.user.student.tests_passed = Topic(topic)
                #     request.user.save()
                # else:
                is_student = False
                request.session['tests_passed_topic_ids'] = topic.id
    else:
        code_text = test.default_code
        form = PythonCodeInput(initial={'code_text': code_text})

    return render(request, 'fizzbuzz/test.html', {'test': test, 'form': form, 'result': result, 'correct': correct,
                                                  'is_student': is_student})


def get_guest_certificate(request, topic_name):
    if request.method == 'POST':
        form = GuestUserDetailsInput(request.POST)
    else:
        form = GuestUserDetailsInput()
    return render(request, 'fizzbuzz/guest_user_details_input.html', {'form': form, 'topic_name': topic_name})


def certificate(request, topic_name):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="{}_certificate.pdf"'.format(topic_name)
        pdf = canvas.Canvas(response)
        pdf.setPageSize(landscape(letter))
        pdf.drawString(180, 500, '{} has been certified by this site to have passed the test for {}'.format(full_name,
                                                                                                            topic_name))
        pdf.drawString(180, 400, 'Yay.')
        pdf.showPage()
        pdf.save()
        return response
