import numpy as np

def random_array_sum():
    arr = np.random.randint(1, 100, size=5)
    total = np.sum(arr)
    return f"The sum of {arr} is {total}."

if __name__ == "__main__":
    print(random_greeting())