#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Natasha
# DATE CREATED: 21Mar24                                 
# REVISED DATE: N/A
# PURPOSE: This function get_pet_labels creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Import python module
from os import listdir

# Define function to read and clean filenames from a folder 
def clean_pet_labels(filename):
    """
    Apply cleaning logic to generate the pet labels.

    """
    parts = filename.split('_')
    pet_label = ' '.join(parts[:-1]).lower().strip()
    
    # Make sure pet_label isreturned as a list to be used in the next function
    return [pet_label]


# Define get_pet_labels function 
def get_pet_labels(pet_image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function. 
    
    The filenames of the images should contain the true identity of the pet 
    in the image.
    
    The format the pet labels should; 
    -Be all lower case letters
    -Single space separating each word
    -Leading and trailing whitespace characters stripped 

    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. 
      The list contains for following item:
         index 0 = pet image label (string)
      i.e. when you access the value associated with a key in the dictionary 
      returned by the get_pet_labels function, you should expect to find the 
      pet image label as a string at index 0 of the list that corresponds to 
      that key. This ensures that the structure of the dictionary aligns with 
      the expected format where the pet image label is the first item in the 
      list value for each image filename key.
    """
   
    results_dic = {}  # Create an empty dictionary to store the results
        
    # Iterate over each file in the specified directory
    for filename in listdir(pet_image_dir):
        # Check if the filename already exists in the dictionary
        if filename in results_dic:
            print(f"Skipping duplicate file: {filename}")
            continue

        # Call the clean_pet_labels function to get the cleaned pet label 
        #for the current file
        pet_label = clean_pet_labels(filename)

        # Add the cleaned pet label to the dictionary as a list associated 
        # with its filename
        results_dic[filename] = pet_label
        # Print the individual filename and cleaned pet label
        # This checks that clean_pet_labels works as expected
        print(f"Filename: {filename}, Cleaned Pet Label: {pet_label}")
    
    # Print the entire results dictionary
    print("Results Dictionary:")
    for key, value in results_dic.items():
        print(f"Dict Key: {key}, Dict Value: {value}")

    # Returns a dictionary with the pet image filename as the key and a 
    # List that contains only the pet image label as the value for all 
    # pet images in the pet_image folder
    return results_dic
