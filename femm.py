import os


class Interface:
    ans_filename = None

    def __init__(self, filename=None):
        self._filename = filename

    @staticmethod
    def _run_command(command):
        os.system(command)

    def mesh(self):
        self._run_command(f'./fem/fmesher {self._filename}.fem')

    def solve(self):
        self._run_command(f'./fem/fsolver {self._filename}')
        self.ans_filename = f'{self._filename}.ans'
        return self.ans_filename
