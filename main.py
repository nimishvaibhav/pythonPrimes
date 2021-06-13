
def find_prime():

    for i in range(1, 100):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_prime()

