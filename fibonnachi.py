
print("Fibonnachi sequence...\n")


def get_input():

    input_list = []

    input_1 = int(input("Enter 1st number: "))

    input_2 = int(input("Enter 2nd number: "))

    input_list.append(input_1)
    input_list.append(input_2)

    return input_list

def fibo():

    fibo_list = []

    input_list = get_input()
    while len(input_list) != 2:
        input_list = get_input()

    fibo_list.append(input_list[0])
    fibo_list.append(input_list[1])

    max_length = int(input("enter maximum lentgh of the list: "))

    while len(fibo_list) != max_length:

        last_2 = fibo_list[-2:]

        fibo_sum = last_2[0] + last_2[1]

        fibo_list.append(fibo_sum)

    return fibo_list

if __name__ == "__main__":
    print(fibo())