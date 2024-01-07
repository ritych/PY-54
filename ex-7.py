import logging


def calc_average(input_list):
    total = sum(input_list)
    average = total / len(input_list)
    return average


def main():
    try:
        input_list = input("Введите список чисел через запятую: ")
        numbers = [int(x) for x in input_list.split(",")]
        result = calc_average(numbers)
        print("Среднее арифметическое:", result)
    except ValueError as e:
        logging.error(f"Error: {e}")
        print("Ошибка: некорректный формат чисел.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="log_ex7.txt", filemode="w", format="%(asctime)s %(levelname)s %(message)s")
    main()
