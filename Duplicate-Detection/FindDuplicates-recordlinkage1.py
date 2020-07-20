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

    CreatorID   CreatorName
    108	        Thunberg, Carl Peter, 1743-1828
    3249	    Söderberg, Christopher, 1804-1833
    3229	    Kjellenberg, Fredrik Ulrik, 1795-1862
    6	        Grew, Nehemiah, 1641-1712
    7     	    Kindberg, N. C. (Nils Conrad), 1832-1910
    '''

    # Read the data into a Pandas dataframe
    authors_input = pd.read_csv("uniquecreators.txt", sep="\t", header=0, encoding="utf-8", index_col='CreatorID')

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
    rl_indexer.sortedneighbourhood(left_on='CreatorName', right_on='CreatorName')
    match_candidates = rl_indexer.index(authors_input)

    '''
    The Record Linkage Toolkit offers multiple options for performing comparisons.
    In this case, the CreatorName fields are compared using the Levenshtein method
    (which is the default) with a threshold value of 0.80.  All comparisons that 
    receive a Levenstein score higher than the threshold are given value of 1; all
    that score lower are given value of 0.  There is no absolute right or wrong value
    for this threshold; you need to experiment with your data to see what threshold
    value returns the best results.
    '''
    rl_compare = recordlinkage.Compare()
    rl_compare.string('CreatorName', 'CreatorName', method='levenshtein', threshold=0.80, label='CreatorName')
    computed_match_scores = rl_compare.compute(match_candidates, authors_input)

    # Show number of matches (value = 1) and non-matches (value = 0)
    print('Number of matches (1.0) and non-matches (0.0)')
    print()
    print(computed_match_scores.sum(axis=1).value_counts().sort_index(ascending=False))
    print()
        
    # Pick only the rows with a score > 0 (matches)
    potential_dupes = computed_match_scores[computed_match_scores.sum(axis=1) > 0].reset_index()

    # Clean up the output and merge it with the input
    merged_output = potential_dupes\
        .rename(columns={'CreatorID_1': 'CreatorID_x', 'CreatorID_2': 'CreatorID_y'})\
        .drop('CreatorName', axis=1)\
        .merge(authors_input, left_on='CreatorID_x', right_on='CreatorID')\
        .merge(authors_input, left_on='CreatorID_y', right_on='CreatorID')

    # Print the entire dataframe
    #pd.set_option('display.max_rows', None)
    #pd.set_option('display.max_columns', None)
    #pd.set_option('display.width', None)
    #pd.set_option('display.max_colwidth', -1)
    #print(potential_dupes)

    # Export the dataframe (with re-ordered columns) to a tab-separated file
    merged_output[['CreatorID_x', 'CreatorName_x', 'CreatorID_y', 'CreatorName_y']]\
        .to_csv('recordlinkage1output.txt', sep='\t', encoding='utf-8', index=False)

    print()
    print (dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

except Exception as e:
    print(e)
