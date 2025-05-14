#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            num = my_list_1[i]
            den = my_list_2[i]
        except IndexError:
            print("out of range")
            result.append(0)
            continue
        try:
            div = num / den
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except (TypeError, ValueError):
            print("wrong type")
            div = 0
        finally:
            result.append(div)
    return result
