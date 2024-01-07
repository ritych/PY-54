import logging
import random


def get_random(a, b):
    return random.randint(a, b)


def main():
    min_range = int(input("Начальное значение интервала "))
    max_range = int(input("Финальное значение интервала "))
    count = int(input("Количество чисел для генерации "))
    if min_range > max_range:
        logging.error("стартовое значение меньше финального")
        print("Стартовое значение не может быть меньше финального Введите еще раз")
        main()
        return
    elif min_range < 0 or max_range < 0:
        logging.error("границы диапазона отрицательные")
        print("Границы диапозона дольжны быть больше 0. Введите еще раз")
        main()
        return
    for wrk in range(count):
        print(get_random(min_range,max_range))


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR, filename="log_ex6.txt", filemode="w", format="%(asctime)s %(levelname)s %(message)s")
    main()
