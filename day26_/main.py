import pandas

if __name__ == '__main__':
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    data_dict = {key: value for (key, value) in data.values}

    user_input = input("Give me a word: ").strip()
    top_secret = []
    while user_input != "exit":
        for letter in user_input:
            top_secret.append(data_dict.get(letter.upper()))

        print(top_secret)
        top_secret.clear()
        user_input = input("Give me a word: ").strip()
