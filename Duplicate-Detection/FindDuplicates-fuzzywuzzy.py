'''
To select a specific Python environment in VS Code, use the "Python: Select Interpreter" 
command from the Command Palette (Ctrl+Shift+P).
'''

'''
Useful links

FuzzyWuzzy String-Matching Library example: https://www.datacamp.com/community/tutorials/fuzzy-string-python
'''

import datetime as dt
import pandas as pd
from fuzzywuzzy import fuzz
from pathlib import Path

try:
    # FUZZYWUZZY
    print("FUZZYWUZZY")
    print (dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("")

    '''
    Example of the data in the input file:

    CreatorID   CreatorName
    108	        Thunberg, Carl Peter, 1743-1828
    3249	    Söderberg, Christopher, 1804-1833
    3229	    Kjellenberg, Fredrik Ulrik, 1795-1862
    6	        Grew, Nehemiah, 1641-1712
    7     	    Kindberg, N. C. (Nils Conrad), 1832-1910
    '''

    # Read the data into a list
    f = open("uniquecreators.txt", "r", encoding="utf-8")
    authors = {}
    isHeaderRow = True
    for author in f.readlines():
        if isHeaderRow:
            isHeaderRow = False
        else:
            authors[author.split("\t")[0]] = author.split("\t")[1]
    f.close()

    # Make a copy of the list to compare the authors against
    authors2 = authors

    # Prepare the output file
    f = open("fuzzywuzzyoutput.txt", "w", encoding='utf-8')
    f.write("AuthorID1\tAuthorName1\tAuthorID2\tAuthorName2\tRatio\tPartialRatio\tTokenSortRatio\tTokenSetRatio\n")
    f.close()

    # Open the output file for appending the output
    f = open("fuzzywuzzyoutput.txt", "a", encoding='utf-8')

    # Compare each author to the whole list
    index = 0
    for author in authors:
        # For testing, just output the first ten authors in the file (takes too long to process everything)
        index+=1
        if index > 10:
            break

        for author2 in authors2:
            # Don't compare the author to itself
            if (author != author2):
                # First check for a high token_set_ratio value
                # token_set_ratio
                # The strings being compared are tokenized and preprocessed (made lower case
                # without punctuation).  Then, a set operation identifies the common tokens 
                # (the intersection) and ratio() comparisons between the following new strings:
                #    s1 = Sorted_tokens_in_intersection
                #    s2 = Sorted_tokens_in_intersection + sorted_rest_of_str1_tokens
                #    s3 = Sorted_tokens_in_intersection + sorted_rest_of_str2_tokens
                # The logic behind these comparisons is that since Sorted_tokens_in_intersection 
                # is always the same, the score will tend to go up as these words make up a larger
                # chunk of the original strings or the remaining tokens are closer to each other.
                TokenSetRatio = fuzz.token_set_ratio(authors[author], authors2[author2])

                # If token_set_ratio is at least 75, then look closer at these names
                if TokenSetRatio >= 75:
                    # Get the other ratios for these two authors

                    # ratio
                    # Levenshtein distance similarity ratio
                    Ratio = fuzz.ratio(authors[author], authors2[author2])

                    # partial_ratio
                    # If the shorter string being compared has length k and the longer string has
                    # length m, then partial_ratio seeks the score of the best matching length-k 
                    # substring.
                    PartialRatio = fuzz.partial_ratio(authors[author], authors2[author2])

                    # token_sort_ratio
                    # The strings being compared are tokenized and preprocessed (made lower case
                    # without punctuation).  The tokens are then sorted alphabetically and joined
                    # together. Then, a simple ratio() is applied to obtain the similarity percentage.
                    TokenSortRatio = fuzz.token_sort_ratio(authors[author], authors2[author2])

                    # If all of the ratios combined score greater than 300, then we have
                    # potential duplicates.
                    if Ratio + PartialRatio + TokenSortRatio + TokenSetRatio > 300:
                        # Output the author names and ratios
                        f.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\n".format(
                            author, authors[author].replace("\n", ""), author2, authors2[author2].replace("\n", ""), 
                            Ratio, PartialRatio, TokenSortRatio, TokenSetRatio))

    # Close the output file
    f.close()

    print (dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

except Exception as e:
    print(e)
