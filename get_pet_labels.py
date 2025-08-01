#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Anthony J Brickner
# DATE CREATED: June 14, 2025
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
from os import path

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    result_dic = {}

    #check that directory exists
    if not path.isdir(image_dir):
        print(f"The directory '{image_dir}'supplied is invalid.")
        return []
    try:
        for image in listdir(image_dir):
            #get rid of things that aren't animal/dog names
            filename = image.split('.')[0]
            animalname = filename.lower().split('_')
            animallabel = []
            for partofname in animalname:
                if partofname.isalpha():
                    animallabel.append(partofname)
            #take animal label and join all together so that only words of animal exist in string separated by space
            if len(animallabel) > 1:
                result_dic.update({image: [" ".join(animallabel)]})
            else:
                result_dic.update({image: [animallabel[0]]})
    except Exception as e:
        print(f"Encoutered general exception while getting data for '{image}'.")
        print(e)
        return {}
    # Replace None with the results_dic dictionary that you created with this
    # function
    return result_dic
