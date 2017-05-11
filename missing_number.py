def find_missing(list_one, list_two):
    
    #find the missing number between two lists
    
    # check if both lists are empty
    if len(list_one) == len(list_two) == 0:
        return 0

    # check if both lists are similar
    if not set(list_one).symmetric_difference(set(list_two)):
        return 0
    else:
        #list(set(list_one) - set(List_two)) #error for list with integers
        return list(set(list_one).symmetric_difference(set(list_two)))[0]