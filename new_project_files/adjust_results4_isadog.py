#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Natasha
# DATE CREATED: 23Apr24                                
# REVISED DATE: N/A
# PURPOSE: Function adjust_results4_isadog adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          
#          All dog labels from both the pet images and the classifier function
#          are in the dognames.txt file. 
#          
#          Read all the dog names in dognames.txt into a dictionary where the 
#          'key' is the dog name (from dognames.txt) and the 'value' is one. 
#          If a label is found to exist within this dictionary of dog names then 
#          the label is of-a-dog, otherwise the label isn't of a dog. 

#          This function inputs:
#          -The results dictionary as results_dic within adjust_results4_isadog 
#          function and results for the function call within main.
#          -The text file with dog names as dogfile within adjust_results4_isadog
#          function and in_arg.dogfile for the function call within main. 
#
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. 
#           - Adds the pet image label is of-a-dog as the item at index
#           3 of the list. 
#           -Adds whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. 
#           - Values at indices 3 & 4 are 1 when the label is of-a-dog and 0 when 
#           the label isn't a dog.
#
##
# Define adjust_results4_isadog function 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """           
    # Creates dognames dictionary for quick matching to results_dic labels from
    # real answer & classifier's answer
    dognames_dic = dict()
    
    # Reads in dognames from file, 1 name per line & automatically closes file
    with open(dogfile, "r") as infile:
        # Reads in dognames from first line in file
        line = infile.readline()

        # Processes each line in file until reaching EOF (end-of-file) by 
        # processing line and adding dognames to dognames_dic with while loop
        while line != "":
            # Potential trailing whitespace characters (e.g. newline characters) are 
            # removed specifically from the right end of the string before converting 
            # the string to lowercase and further stripping any remaining leading and 
            # trailing whitespace
            line = line.rstrip().lower().strip()
            # If dog name doesn't exist, add the dictionary as a key with the value of 1
            if line not in dognames_dic:
                dognames_dic[line] = 1

            else:
                # Check since you shouldn't find any duplicate dog names in dognames.txt
                print("** Warning: dog name '{}' already exist in our dictionary!".format(line))

            # Iterate through each line of the file until the end is reached
            line = infile.readline()

    # Add two items to end of value(List) in results_dic. 
    # List Index 3 = whether(1) or not(0) Pet Image Label is a dog AND 
    # List Index 4 = whether(1) or not(0) Classifier Label is a dog
    # Iterate through results_dic if labels are found in dognames_dic
    # then label "is a dog" index3/4=1 otherwise index3/4=0 "not a dog"
    for key in results_dic:

        # Pet Image Label IS of Dog (e.g. found in dognames_dic)
        if results_dic[key][0] in dognames_dic:
            
            # Classifier Label IS image of Dog (e.g. found in dognames_dic)
            # appends (1, 1) because both labels are dogs
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((1, 1))
            
            # Classifier Label IS NOT image of dog (e.g. NOT in dognames_dic)
            # appends (1,0) because only pet label is a dog
            else:
                results_dic[key].extend((1, 0))

        # Pet Image Label IS NOT a Dog image (e.g. NOT found in dognames_dic)   
        else:
            # Classifier Label IS image of Dog (e.g. found in dognames_dic)
            # appends (0, 1)because only Classifier label is a dog
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((0, 1))
            
            # Classifier Label IS NOT image of Dog (e.g. NOT in dognames_dic)
            # appends (0, 0) because both labels aren't dogs
            else:
                results_dic[key].extend((0, 0))
    

    # Print statement to check the results
    print("Results after processing:")
    print(results_dic)
    
    return None 