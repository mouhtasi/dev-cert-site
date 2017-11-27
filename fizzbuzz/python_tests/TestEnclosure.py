import subprocess
from importlib import import_module
import argparse
from os import path


class SandboxedPython:

    @staticmethod
    def run_script_call_self(scratch_module_name, test):
        python_binary = '/home/nap/.virtualenvs/sandbox/bin/python3.6'
        print(path.realpath(__file__))
        returned = subprocess.run([python_binary, path.realpath(__file__), '--modulename', scratch_module_name,
                                   '--testname', test], timeout=10, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if returned.stderr:
            result = 'Error: {}'.format(returned.stderr)
            correct = False
        else:
            returned = str(returned.stdout)
            result, correct = returned.lstrip('b').strip("'").split('separator')

        return result, correct == 'True'

    @staticmethod
    def fizzbuzz(modulename):
        expected_result = 'hi'  # giving only print('hi') as test input
        SolutionClass = SandboxedPython.import_scratch_module(modulename)
        result = SolutionClass.fizzbuzz()
        correct = result == expected_result

        return result, correct

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

