import sys


class calcapp:

    def add(self, value_1, value_2):
        return float(value_1 + value_2)

    def sub(self, value_1, value_2):
        return float(value_1 - value_2)

    def mul(self, value_1, value_2):
        return float(value_1 * value_2)

    def div(self, value_1, value_2):
        try:
            div_val = value_1 / value_2
            return float(div_val)
        except ZeroDivisionError:
            raise ZeroDivisionError("check you value")


def start():
    calc_obj = calcapp()
    expr = sys.argv[1]
    value_1 = int(sys.argv[2])
    value_2 = int(sys.argv[3])
    if expr == "add":
        print(calc_obj.add(value_1, value_2))
    elif expr == "sub":
        print(calc_obj.sub(value_1, value_2))
    elif expr == "mul":
        print(calc_obj.mul(value_1, value_2))
    elif expr == "div":
        print(calc_obj.div(value_1, value_2))


if __name__ == "__main__":
    start()
