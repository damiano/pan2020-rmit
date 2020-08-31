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



## Build the profile-level model

```bash
python3 main.py
```

<!-- # Reproducing preliminary results
*TO-DO*
The script produce a confusion matrix with the 10-fold cross-validation results in the paper. 
The result of tweet-level prediction model is already done and written on the csv files, this process is only reading from the csv files and do the cross validation)
-->


### Contact

For more information, please contact the first author Xinhuan Duan: [s3713321@student.rmit.edu.au](mailto:s3713321@student.rmit.edu.au)

