import statistics
import argparse

parser = argparse.ArgumentParser(description="Räkna ut siffror.")
parser.add_argument("numbers", nargs="+", type=float, help="Listade siffror.")
args = parser.parse_args()

numbers = args.numbers

while True:
    user_input = input("Write a number (or press Enter to finish): ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Error: That wasn't a valid number.")

if len(numbers) == 0:
    print("No numbers entered.")
else:
    print("\nStatistics:")
    print("Minimum:", min(numbers))
    print("Maximum:", max(numbers))
    print("Sum:", sum(numbers))
    print("Mean:", statistics.mean(numbers))
    print("Median:", statistics.median(numbers))
    try:
        print("Mode:", statistics.mode(numbers))
    except statistics.StatisticsError:
        print("Mode: No unique mode found.")
