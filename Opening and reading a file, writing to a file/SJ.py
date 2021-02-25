from pprint import pprint
import os


def reading_sorting():
    with open('1.txt', 'r', encoding='utf-8') as a:
        txt_list_a = []
        count_a = 0
        file_name_a = os.path.basename('1.txt')

        for sting_count in a:
            count_a += 1
            txt_list_a.append(sting_count.strip())

    with open('2.txt', 'r', encoding='utf-8') as b:
        txt_list_b = []
        count_b = 0
        file_name_b = os.path.basename('2.txt')

        for sting_count in b:
            count_b += 1
            txt_list_b.append(sting_count.strip())

    with open('3.txt', 'r', encoding='utf-8') as c:
        txt_list_c = []
        count_c = 0
        file_name_c = os.path.basename('3.txt')

        for sting_count in c:
            count_c += 1
            txt_list_c.append(sting_count.strip())

    count = [count_a, count_b, count_c]
    text = [txt_list_a, txt_list_b, txt_list_c]
    file_names = [file_name_a, file_name_b, file_name_c]

    keys = zip(count, file_names)

    txt_dict = dict(zip(keys, text))

    return txt_dict


def recording_txt(t):
    with open('result.txt', 'w', encoding='utf-8') as d:
        keys = []

        for number in t:
            keys.append(number[0])

        keys = sorted(keys)

        for key in keys:
            for number, text in t.items():
                if number[0] == key:
                    d.write(number[1] + '\n')
                    d.write(str(number[0]) + '\n')
                    for string in text:
                        string += '\n'
                        d.write(string)


recording_txt(reading_sorting())



