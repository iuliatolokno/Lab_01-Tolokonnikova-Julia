import argparse
import sys

from .calculator import calculate
from .converter import convert
from .errors import ConverterError

parser = argparse.ArgumentParser(prog="python -m toolkit", description="Калькулятор и конвертер величин")
commands = parser.add_subparsers(dest="command",required=True)

calculator_parser = commands.add_parser("calc",help="Вычисления заданного арифмитического выражения")
calculator_parser.add_argument("expression",help="Ввод арифмитичсекого выражения")

converter_parser = commands.add_parser("convert",help="Конвертировать величину")
converter_parser.add_argument("value",type=float,help="Число для перевода")
converter_parser.add_argument("--from",dest="from_unit",required=True,help="Начальная единица измерения")
converter_parser.add_argument("--to",dest="to_unit",required=True,help="Конечная единица измерения")

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
