def get_inputs_from_file(file_name):
    read_file = open(file_name, "r")
    text = read_file.read()
    text_list = text.split("\n")
    read_file.close()
    return text_list


def write_output_file(text):
    write_file = open("sheep.out", "w")
    write_file.write(text)
    write_file.close()
    return True


def register_digits(num, m_list):
    # print(num)
    for i in num:
        # print(i)
        if m_list[i] is "n":
            m_list[i] = "*"
    return m_list


def get_digits(number):
    digit_list = [];
    num = int(number)
    while num > 0:
        digit_list.append(int(num % 10))
        num /= 10
        num = int(num)
    # print(digit_list)
    return digit_list


def track_numbers(case_no, input_val):
    # max_lim = 1000000
    marked_list = ["n", "n", "n", "n", "n", "n", "n", "n", "n", "n"]
    number = int(input_val)
    mul_counter = 1
    while True:
        # print(number)
        marked_list = register_digits(get_digits(str(number)), marked_list)
        # print(marked_list)
        if "n" not in marked_list:
            print(number)
            return "Case #" + str(case_no) + ": " + str(number) + "\n"
        mul_counter += 1
        number_2 = int(input_val) * mul_counter
        # print(number_2)
        if number is number_2:
            print("insomnia")
            return "Case #" + str(case_no) + ": INSOMNIA\n"
        number = number_2
    return "Case #" + str(case_no) + ": INSOMNIA\n"


file_values = get_inputs_from_file("A-large-practice.in")

m_text = ''
for i in range(1, len(file_values) - 1):
    m_text += track_numbers(i, file_values[i])
write_output_file(m_text)
