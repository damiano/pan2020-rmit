# pan2020-rmit
Repository for RMIT participation at the "Profiling Fake News Spreaders on Twitter" at PAN @ CLEF 2020
Dowload the files from the github

```bash
cd path-to-your-repositrary
```
Then you are ready for the reproduction of our PAN2020 submission.

note: if you only want to use our software you can switch the branch to software, where you can use our software directly after you have done the installation
## Installation
### data preparation
The train data for our task is should not be exposed to the public according to the PAN restrictions, if you want to get access to the data, you can go to this link : https://pan.webis.de/clef20/pan20-web/author-profiling.html

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
