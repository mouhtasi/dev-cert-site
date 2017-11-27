import subprocess
from importlib import import_module
import argparse
from os import path


class SandboxedPython:

    @staticmethod
    def run_script_call_self(scratch_module_name, test):
        python_binary = '/home/nap/.virtualenvs/sandbox/bin/python3.6'
        returned = subprocess.run([python_binary, path.realpath(__file__), '--modulename', scratch_module_name,
                                   '--testname', test], timeout=10, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if returned.stderr:
            result = 'Error: {}'.format(returned.stderr)
            correct = False
        else:
            returned = str(returned.stdout)
            result, correct = returned.lstrip('b').strip("'\"").split('separator')

        return result, correct == 'True'

    @staticmethod
    def fizzbuzz(modulename):
        SolutionClass = SandboxedPython.import_scratch_module(modulename)
        result = SolutionClass.fizzbuzz()
        expected = SandboxedPython.fizzbuzz_test_1()

        correct = result == expected

        return result, correct

    @staticmethod
    def fizzbuzz_test_1():
        l = []
        for i in range(1, 101):
            if i % 15 == 0:
                l.append('FizzBuzz')
            elif i % 3 == 0:
                l.append('Fizz')
            elif i % 5 == 0:
                l.append('Buzz')
            else:
                l.append(i)
        return l

    @staticmethod
    def test(modulename):
        SolutionClass = SandboxedPython.import_scratch_module(modulename)
        result = SolutionClass.test()
        expected = SandboxedPython.test_test_1()

        correct = result == expected

        return result, correct

    @staticmethod
    def test_test_1():
        return 1

    @staticmethod
    def import_scratch_module(modulename):
        scratch = import_module(modulename, 'Solution')
        return scratch.Solution


if __name__ == '__main__':
    """Run by sandboxed python"""
    parser = argparse.ArgumentParser(description='Only to be run by sandboxed python')
    parser.add_argument('--modulename', dest='modulename', type=str, required=True)
    parser.add_argument('--testname', dest='testname', type=str, required=True)
    args = parser.parse_args()

    test_method = getattr(SandboxedPython, args.testname)
    result, correct = test_method(args.modulename)
    print(result, correct, sep='separator', end='')  # sending to stdout for the subprocess

