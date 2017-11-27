import subprocess


class SandboxedPython:

    @staticmethod
    def run_script_shell(unique_id):
        python_binary = '/home/nap/.virtualenvs/sandbox/bin/python3.6'
        filename = '/home/nap/fizzbuzzcert/fizzbuzz/python_tests/scratch{}.py'.format(unique_id)
        returned = subprocess.run([python_binary, filename], timeout=10, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if returned.stderr:
            output = 'Error: {}'.format(returned.stderr)
        else:
            output = returned.stdout
        return output

    @staticmethod
    def fizzbuzz(unique_id):
        expected_result = b'hi\n'  # giving only print('hi') as test input
        result = SandboxedPython.run_script_shell(unique_id)
        correct = result == expected_result

        print(result)
        return correct
