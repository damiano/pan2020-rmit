from dataset_creator import get_seprate

def main():
    data = get_seprate()
    start_number = 0
    end_number = 3000
    index=0
    
    for i in range(0,10):
        new_frame = data[start_number:end_number]
        start_number+=3000
        end_number+=3000
        new_frame.to_csv ('text_classification/data/train-test/en/fold%d.csv' %index,  header=True,index =False)
        index+=1
        print(new_frame)
    
if __name__ == "__main__":
    main()       