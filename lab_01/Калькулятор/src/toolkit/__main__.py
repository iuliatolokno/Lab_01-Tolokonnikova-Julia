import argparse
import sys

from .calculator import calculate
from .converter import convert
from .errors import ConverterError

parser = argparse.ArgumentParser(prog="python -m toolkit", description="Калькулятор и конвертер величин")
commands = parser.add_subparsers(dest="command",requirements=True)

calc_parser = commands.add_parser("calc",help="Вычисления заданного арифмитического выражения")
calc_parser.add_argument("expression",help="Ввод арифмитичсекого выражения")

convert_parser = commands.add_parser("convert",help="Конвертировать величину")
convert_parser.add_argument("value",type=float,help="Значение")
convert_parser.add_argument("--from",dest="from_unit",requirements=True,help="Начальная еденица измерения")
convert_parser.add_argument("--to",dest="to_unit",requirements=True,help="Конечная еденица измерения")

def main():
    argumenty = parser.parse_args()
    try:
        if argumenty.command == "calc":
            result = calculate(argumenty.expression)
            sys.stdout.write(str(result) + "\n")
            return 0
        elif argumenty.command == "convert":
            result = convert(argumenty.value , argumenty.from_unit, argumenty.to_unit)
            sys.stdout.write(str(result) + "\n")
            return 0
    except ValueError as e:
        sys.stderr.write(f"Ошибка: {e}\n")
        return 2

if __name__ == "__main__":
    sys.exit(main())
