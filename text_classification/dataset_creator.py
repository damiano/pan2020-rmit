from xml_reader import read_twitters

def create_dataset():
    set =[]
    with open("text_classification/data/en/truth.txt") as file_in:
        for line in file_in:
            array = line.split(":::")
            user = array[0]
            posts= read_twitters(user+".xml")
            truth =bool(int(array[1][0]))
            set.append([user,posts,truth])
    return set

set = create_dataset()
print(set)