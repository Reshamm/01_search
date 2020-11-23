import csv


def read_from_csv():
    source = []  # list to get and store data from csv file.
    file_name = "devils_data.csv"
    with open(file_name, mode="r", encoding="utf-8")as file:
        # read CSV file
        csv_file = csv.reader(file)
        for item in csv_file:
            for each_item in item:
                source.append(each_item)  # add to the list.
    return source


def write_to_csv(new_item):
    file_name = "devils_data.csv"
    with open(file_name, mode="a", encoding="utf-8")as file:
        file.write(new_item)


def search():
    data = read_from_csv()
    word = input("enter a word to search... ")
    if word in data:
        print(f"{word} 見つかった")
    else:
        print(f"{word} 見つからなかったので追加しました。")
        if len(data) == 0:
            write_to_csv(word)
        else:
            write_to_csv("," + word)
    print(read_from_csv())


if __name__ == "__main__":
    search()

