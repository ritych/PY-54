import logging
import math


def main():
    a = int(input("Введите коэффициент A "))
    b = int(input("Введите коэффициент B "))
    c = int(input("Введите коэффициент C "))
    discriminant = find_d(a, b, c)
    try:
        sqrt_desc = math.sqrt(discriminant)
    except:
        logging.exception("Discriminant < 0")
        print('Ошибка. Дискриминант отрицательный, попробуйте задать коэффициенты еще раз')
        main()
        return

    print('Дискриминант =', discriminant)
    result = find_x1_x2(a, b, sqrt_desc)
    logging.info(f"Уравнение решено. Корни = {result}")
    print('Корни =', result)


def find_d(a, b, c):
    d = b ** 2 - 4 * a * c
    return d


def find_x1_x2(a, b, sqrt_desc_wrk):
    try:
        x1 = (-b - sqrt_desc_wrk) / (2 * a)
        if sqrt_desc_wrk > 0:
            x2 = (-b + sqrt_desc_wrk) / (2 * a)
            return x1, x2
        return x1
    except:
        logging.exception("a = 0")
        print('Ошибка. Коэффициент A равен 0, попробуйте задать коэффициенты еще раз')
        main()
        return


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="log_ex5.txt", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
    main()
