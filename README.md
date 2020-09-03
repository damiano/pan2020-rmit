# RMIT at PAN-CLEF 2020: Profiling Fake News Spreaders on Twitter

Implementation of our system submitted to the "Profiling Fake News Spreaders on Twitter" at PAN @ CLEF 2020


## Citation

If you use this resource, please cite our paper:

*Xinhuan Duan, Elham Naghizade, Damiano Spina, and Xiuzhen Zhang. 2020. RMIT at PAN-CLEF 2020: Profiling Fake News Spreaders on Twitter. In CLEF 2020 Labs and Workshops, Notebook Papers. CEUR-WS.org (Sep 2020).*

### BibTeX

```bibtex
@InProceedings{duan2020rmit,
author = {Duan, Xinhuan and Naghizade, Elham and Spina, Damiano and Zhang, Xiuzhen},
title = {{RMIT at PAN-CLEF 2020: Profiling Fake News Spreaders on Twitter}},
booktitle = {{CLEF 2020 Labs and Workshops, Notebook Papers}},
year={2020}
}
```


## Data Preparation

Download the files from the github

```bash
cd path-to-your-repositrary
```
Then you are ready for the reproduction of our PAN2020 submission.

 - note: if you only want to use our software you can switch to the `software` branch, where you can use our software directly after you have done the installation
 - note: your computer should support cuda cudnn, if you haven't install cuda or cudnn, go to the following links:

## Installation


```bash
python3 -m pip install -r requirement.txt
```

## Build the TLSP model

### data preparation
The train data for our task is should not be exposed to the public according to the PAN restrictions, if you want to get access to the data, go to this link : https://pan.webis.de/clef20/pan20-web/author-profiling.html

After downloding the data, put them copy and paste the en and es folder into the relative path /text_classification/data

### Train a single model

```bash
python3 modelTrainer.py
```
In the folder you can then see a new file:"BERT-model.pt", which is a tweet-level model which can predict whether a user is a fake news spreader or not.


### reproduce a 10-fold validation

Since this project contains of both tweet-level and user level classifiction, So when implementing a 10-fold validation, the data trained on the tweet-level and user-profile level should be the same data. So the 10 fold validation is implemented manually. All the users together with their tweets are divided into 10 folds and they are saved in 10 csv file. The in the file modelTrainer, the method train_model() can do the 10 fold validation. 



## Build the profile-level model

```bash
python3 main.py
```

The script can produce a confusion matrix with the 10 fold validation result in the paper, and the features extracted from the user-level are already done and written with csv files in the  path:
```bash
csvs/3rd/user0-user9
```

and in main.py file line 56 and 57, you can add or delete word in the columns list and you are expected to see the change of the performance

```bash
  columns = ['median_score','mean_score','score_std','median_compound','mean_compound','compound_std','emoji','hash',
               'hash_median','hash_std','url','url_median','url_std']
```
you can edit my useer csv and add your customed value to do the evaluation or you can even use the function in line 58 to add a new data

```bash
  columns =assemble(columns,'trump')
```


<!-- # Reproducing preliminary results
*TO-DO*
The script produce a confusion matrix with the 10-fold cross-validation results in the paper. 
The result of tweet-level prediction model is already done and written on the csv files, this process is only reading from the csv files and do the cross validation)
-->


### Contact

For more information, please contact the first author Xinhuan Duan: [s3713321@student.rmit.edu.au](mailto:s3713321@student.rmit.edu.au)

