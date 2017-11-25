import subprocess


class SandboxedPython:

    @staticmethod
    def run_script_shell(unique_id):
        python_binary = '/home/nap/.virtualenvs/sandbox/bin/python3.6'
        filename = '/home/nap/fizzbuzzcert/fizzbuzz/python_tests/scratch{}.py'.format(unique_id)
        returned = subprocess.run([python_binary, filename], timeout=10, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return returned.stdout

    @staticmethod
    def fizzbuzz(unique_id):
        result = SandboxedPython.run_script_shell(unique_id)
        print(result)
