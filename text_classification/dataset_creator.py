
def create_dataset():
    set =[]
    with open("text_classification/data/en/truth.txt") as file_in:
        for line in file_in:
            set.append([line.split(":::")[0],bool(int(line.split(":::")[1][0]))])
    return set

set = create_dataset()
print(set)