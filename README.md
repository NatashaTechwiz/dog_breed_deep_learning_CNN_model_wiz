# Student Revsion
#  Dog Breed Classification Project -Deep Learning Model CNN
CNN model building exercise from Udacity course: AI Programming with Python.

## Description
This project utilises a deep learning model called a convolutional neural network (CNN) for classifying images of different dog breeds.

Exert from the course notes:
'CNNs work particularly well for detecting features in images like colours, textures, and edges; then using these features to identify objects in the images. The CNN selected has already learned the features from a giant dataset of 1.2 million images called [ImageNet](https://www.image-net.org/about.php). There are different types of CNNs that have different structures (architectures) that work better or worse depending on your criteria.'

This project includes the three different architectures (AlexNet, VGG, and ResNet). Using the match criteria calculated when executing the programme, it can be determined which model performs best for the image set being modelled.

## How to Execute the code for this Project
Recommend setting up a virtual environment before pip installing non-standard Python packages in order to protect the main installation.

- Download the 'new_project_files' folder with all the files included, ensuring the folders with 'pet_images' and 'uploaded_images' is in the same location as the project files.

- To run the scripts with only one of the CNN architecture models and output to your terminal window type one of the following;
```
python check_images.py --dir pet_images/ --arch resnet  --dogfile dognames.txt 
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt 
python check_images.py --dir pet_images/ --arch vgg  --dogfile dognames.txt 
```
- To batch process all 3 CNN architecture models and output to a txt file in your project folder;
```
#for pet_images files
sh run_models_batch.sh  #Linux shell
run_models_batch.bat # windows/anaconda promt/vscode terminal 

#for uploaded_images files
sh run_models_batch_uploaded.sh  #Linux shell
run_models_batch_uploaded.bat # windows/anaconda promt/vscode terminal
```
- Notes: Script fuctionality was tested in Linux shell and Visual Studio Code with python interpreter, with the following versions of the required packages;<br>
torch==2.2.1<br>
pillow==10.2.0<br>
torchvision==0.17.1

# Original Version
___________________________________________________________________________________________________________________
# AIPND-revision
This repository contains _REVISED_ code and associated files for the AI Programming with Python Nanodegree program. This repository consists of a number of tutorial notebooks for various coding exercises and programming labs that will be used to supplement the lessons of the course.

## Table Of Contents

### Tutorial Notebooks
* No revisions

### Programming Project
* [Intro to Python Project - Classifying Pet Images:](https://github.com/udacity/AIPND-revision/tree/master/intropyproject-classify-pet-images "Classifying Pet Images Project") Determine which CNN architecture model works best at classifying images of dogs and their breeds.

### NumPy and Pandas Mini-Projects
* No revisions 

### Matplotlib
* No revisions 

### Quiz Notes
* [Notes:](https://github.com/udacity/AIPND-revision/tree/master/notes "Notes") This directory contains more information about certain quizzes that are testing more challenging concepts. Additionally, one will find the [Frequently Asked Questions](https://github.com/udacity/AIPND-revision/blob/master/notes/project_intro-to-python.md) for the _Intro to Python Project_. Click on the filename to view the contents of the notes on a _quiz_ or the _Intro to Python Project_.

## Dependencies

Each directory has a `requirements.txt` describing the minimal dependencies required to run the notebooks in that directory.

### pip

To install these dependencies with pip, you can issue `pip3 install -r requirements.txt`.

