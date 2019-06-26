import subprocess


class CalcLib:

    def __init__(self):
        self.result = 0

    def perform_expr(self, expr, val_1, val_2):
        self.result = float(subprocess.check_output(['calcapp', expr, val_1, val_2]))

    def check_result(self, expected):
        if self.result != float(expected):
            print("Fail")
            raise ArithmeticError()
        else:
            print("Success")

    def reset_result(self):
        self.result = 0

