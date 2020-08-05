# pan2020-rmit
Repository for RMIT participation at the "Profiling Fake News Spreaders on Twitter" at PAN @ CLEF 2020

## Installation

```bash
python3 -m pip install -r requirement.txt
```

## reproduce the TLSP
```bash
python3 modelTrainer.py
```
here you can get a tweet-level model which can predict whether a user is a fake news spreader or not.


## reprodece the user-profile level 

```bash
python3 main.py
```

here you can see a confusion matrix of our 10-fold validation(the result of tweet-level prediction model is already 
done and written on the csv files, this process is only reading from the csv files and do the cross validation)
