'''
To select a specific Python environment in VS Code, use the "Python: Select Interpreter" 
command from the Command Palette (Ctrl+Shift+P).
'''

'''
Useful links

Record Linkage Toolkit documentation: https://recordlinkage.readthedocs.io/en/latest/about.html
Record Linkage Toolkit comparison options: https://recordlinkage.readthedocs.io/en/latest/ref-compare.html
Record Linkage Toolkit example: https://pbpython.com/record-linking.html
How to read a TSV into a dataframe: https://stackoverflow.com/questions/9652832/how-to-load-a-tsv-file-into-a-pandas-dataframe
'''

import datetime as dt
import pandas as pd
from pathlib import Path
from recordlinkage import recordlinkage

try:
    # RECORDLINKAGE
    print("RECORDLINKAGE")
    print (dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("")

    '''
    Example of the data in the input file:

    AuthorID	AuthorNameID	AuthorTypeName	AuthorName	                    StartDate	EndDate
    108	        82	            Person	        Thunberg, Carl Peter,  	        1743	    1828
    3249	    2933	        Person       	Söderberg, Christopher,         1804        1833
    3229	    2913	        Person	        Kjellenberg, Fredrik Ulrik,     1795	    1862
    6       	6	            Person	        Grew, Nehemiah,  	            1641	    1712
    7       	7	            Person      	Kindberg, N. C. (Nils Conrad),  1832	    1910
    '''

    # Read the data into a Pandas dataframe
    authors_rl = pd.read_csv("authors.txt", sep="\t", header=0, encoding="utf-8", index_col='AuthorNameID')

    '''
    Set up an index for the record linkage toolkit to use when comparing values.
    Use the "sortedneighborhood" blocking strategy to determine the match candidates.
    With a "full" index, every author is commpared to every other author.  On the other
    hand, with the "sortedneighborhood" strategy, the two lists being compared are sorted
    as one, and only those names that are near each other (in the same "neighorhood") are
    considered to be candidates for comparison.  This reduces the amount of comparisons 
    that need to be done and focuses on only those names that are most likely to match.
    '''
    rl_indexer = recordlinkage.Index()
    rl_indexer.sortedneighbourhood(left_on='AuthorName', right_on='AuthorName')
    match_candidates = rl_indexer.index(authors_rl)

    '''
    The Record Linkage Toolkit offers multiple options for performing comparisons.
    In this case, one numeric field (AuthorID) and three string fields (AuthorName,
    StartDate, EndDate) are compared.  
    
    Numeric fields that match are given a score of 1, no match scores 0.

    The string fields are compared using the Levenshtein method (which is the 
    default).  All comparisons that receive a Levenstein score higher than the 
    threshold are given value of 1; all that score lower are given value of 0.  
    There is no absolute right or wrong value for this threshold; you need to
    experiment with your data to see what threshold value returns the best 
    results.

    Since four fields are being compared, every output row has four separate
    score values.
    '''
    r1_compare = recordlinkage.Compare()
    r1_compare.numeric('AuthorID', 'AuthorID', method='step', label='AuthorID')
    r1_compare.string('AuthorName', 'AuthorName', method='levenshtein', threshold=0.80, label='AuthorName')
    r1_compare.string('StartDate', 'StartDate', method='levenshtein', threshold=0.90, label='StartDate')
    r1_compare.string('EndDate', 'EndDate', method='levenshtein', threshold=0.90, label='EndDate')
    computed_match_scores = r1_compare.compute(match_candidates, authors_rl)

    # Give negative weight to AuthorID matches.
    # When the Author IDs match, the names for the same author.  In this case, we want
    # to disregard the match, so we assign a large negative weight to this score.
    computed_match_scores['AuthorID'] = computed_match_scores['AuthorID'] * -100

    # Give additional weight to AuthorName matches (name matches are more important
    # than date matches)
    computed_match_scores['AuthorName'] = computed_match_scores['AuthorName'] * 10

    # Sum the scores for each row and show the number of matches (value > 0) and 
    # non-matches (value = 0)
    print(computed_match_scores.sum(axis=1).value_counts().sort_index(ascending=False))
    print()
        
    # Pick only the rows with a score >= 10.  Scores >= 10 mean that the names match, 
    # the Author IDs do not, and the Start/End dates may or may not.
    potential_dupes = computed_match_scores[computed_match_scores.sum(axis=1) >= 10].reset_index()

    # Add a "Score" column to the dataset
    potential_dupes['Score'] = potential_dupes.loc[:, 'AuthorName':'EndDate'].sum(axis=1)

    # Clean up the output and merge it with the input
    merged_output = potential_dupes\
        .rename(columns={'AuthorName': 'AuthorName_Score', 'StartDate': 'StartDate_Score', 'EndDate': 'EndDate_Score'})\
        .rename(columns={'AuthorNameID_1': 'AuthorNameID_x', 'AuthorNameID_2': 'AuthorNameID_y'})\
        .drop('AuthorID', axis=1)\
        .merge(authors_rl, left_on='AuthorNameID_x', right_on='AuthorNameID')\
        .merge(authors_rl, left_on='AuthorNameID_y', right_on='AuthorNameID')

    # Print the entire dataframe
    #pd.set_option('display.max_rows', None)
    #pd.set_option('display.max_columns', None)
    #pd.set_option('display.width', None)
    #pd.set_option('display.max_colwidth', -1)
    #print(merged_output)

    # Export the dataframe (with re-ordered columns) to a tab-separated file
    merged_output[['AuthorID_x', 'AuthorNameID_x', 'AuthorTypeName_x', 'AuthorName_x', 'StartDate_x', 'EndDate_x',\
        'AuthorID_y', 'AuthorNameID_y', 'AuthorTypeName_y', 'AuthorName_y', 'StartDate_y', 'EndDate_y',\
        'AuthorName_Score', 'StartDate_Score', 'EndDate_Score', 'Score']]\
            .to_csv('recordlinkage2output.txt', sep='\t', encoding='utf-8', index=False)

    print()
    print (dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

except Exception as e:
    print(e)
