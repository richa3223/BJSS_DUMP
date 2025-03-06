"""
 Helper module for assertions and testing statements in the playing-with-lego.ipynb notebook

 Author: Matt McFahn
 Created: 06/06/2021
"""

import pandas as pd
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def give_message(outcome, extra_message=None):
    """
    Pretty print a message based on whether or not you pass a test

    Parameters
    ----------
    outcome : bool
        Did the test pass?
    extra_message : str / NoneType
        Another message to print
    Returns
    -------
    None
    """
    if outcome:
        print('''( ͡❛ ͜ʖ ͡❛) Good job! Lego's looking pretty good.''')
    else:
        print('''( ͡❛ ︵ ͡❛) This Lego still needs some cleaning...''')
    if extra_message:
        print('\n\n')
        print(extra_message)

    return None


def data_loaded(df):
    extra_message = None

    try:
        shape = df.shape
        if shape == (12261, 15):
            outcome = True
        else:
            outcome = False
            extra_message = f"The data you've loaded has shape: {shape}, rather than (12261, 15) as expected. Have you loaded the right data?"
    except:
        outcome = False
        extra_message = "The df variable doesn't seem to be a DataFrame object - have you loaded it properly?"

    give_message(outcome, extra_message)

    return None


def column_renaming(df_cleaned):
    observed = list(df_cleaned.columns)
    expected = ['Ages', 'ListPrice', 'NumReviews', 'PieceCount', 'ProdDesc', 'ProdID',
                'ProdLongDesc', 'ReviewDifficulty', 'SetName', 'ThemeName',
                'ValStarRating', 'Country', 'LaunchDate', 'WeightGrs']

    outcome = observed == expected
    if not outcome:
        extra_message = f'''The columns in df_cleaned are: {observed}
    The expected columns are: {expected}
                         '''
    else:
        extra_message = None

    give_message(outcome, extra_message)
    return None


def column_reordering(df_cleaned):
    observed = list(df_cleaned.columns)
    expected = ['ProdID', 'SetName', 'ProdDesc', 'ProdLongDesc', 'ThemeName',
                'Country', 'Ages', 'ReviewDifficulty', 'NumReviews', 'ListPrice',
                'WeightGrs', 'PieceCount', 'ValStarRating', 'LaunchDate']

    outcome = observed == expected
    if not outcome:
        extra_message = f'''The columns in df_cleaned are: {observed}
    The expected columns are: {expected}
                         '''
    else:
        extra_message = None

    give_message(outcome, extra_message)
    return None


def country_cleaning(df_cleaned):
    observed = list(df_cleaned['Country'].unique())
    observed.sort()
    expected = ['AT', 'AU', 'BE', 'CA', 'CH', 'CZ', 'DE', 'DN', 'ES', 'FI', 'FR', 'GB', 'IE', 'IT', 'LU', 'NL',
                'NO', 'NZ', 'PL', 'PT', 'US']

    outcome = observed == expected
    if not outcome:
        extra_message = f'''The unique countries in df_cleaned are: {observed}
    The expected list is: {expected}
                         '''
    else:
        extra_message = None

    give_message(outcome, extra_message)
    return None


def unique_themes(unique_themes):
    observed = unique_themes
    observed.sort()
    expected = ['Angry Birds™',
                'Architecture',
                'BOOST',
                "Blue's Helicopter Pursuit",
                'BrickHeadz',
                'Carnotaurus Gyrosphere Escape',
                'City',
                'Classic',
                'Creator 3-in-1',
                'Creator Expert',
                'DC Comics™ Super Heroes',
                'DC Super Hero Girls',
                'DIMENSIONS™',
                'DUPLO®',
                'Dilophosaurus Outpost Attack',
                'Disney™',
                'Elves',
                'Friends',
                'Ghostbusters™',
                'Ideas',
                'Indoraptor Rampage at Lockwood Estate',
                'Juniors',
                'Jurassic Park Velociraptor Chase',
                'LEGO® Creator 3-in-1',
                'MINDSTORMS®',
                'Marvel Super Heroes',
                'Minecraft™',
                'Minifigures',
                'NEXO KNIGHTS™',
                'NINJAGO®',
                'Power Functions',
                'Pteranodon Chase',
                'SERIOUS PLAY®',
                'Speed Champions',
                'Star Wars™',
                'Stygimoloch Breakout',
                'T. rex Transport',
                'THE LEGO® BATMAN MOVIE',
                'THE LEGO® NINJAGO® MOVIE™',
                'Technic']
    outcome = observed == expected
    if not outcome:
        extra_message = f'''The unique themes in df_cleaned are: {observed}
    The expected list is: {expected}
                             '''
    else:
        extra_message = None

    give_message(outcome, extra_message)
    return None


def set_count_by_product(set_count_by_product):
    observed = list(set_count_by_product.ProdID)
    observed.sort()
    expected = [2304, 8293, 10816, 41150, 71171, 75060]
    outcome = observed == expected
    if not outcome:
        extra_message = f'''The set of ProdID's you've identified are: {observed}
    The expected list is: {expected}
                            '''
    else:
        extra_message = None

    give_message(outcome, extra_message)
    return None


def duped_sets(duped_sets):
    observed = list(duped_sets.SetName)
    observed.sort()
    expected = ['Green LEGO® DUPLO® Baseplate',
                'LEGO® DIMENSIONS™ PLAYSTATION® 4 Starter Pack',
                'LEGO® DUPLO® Green Baseplate', 'LEGO® Power Functions Motor Set',
                "Moana's Ocean Voyage", 'Moana’s Ocean Voyage',
                'My First Cars and Trucks', 'My First Vehicles',
                'Power Functions Motor Set', 'Slave I', 'Slave I™',
                'Starter Pack PLAYSTATION® 4', "Vaiana's Ocean Voyage"]

    outcome = observed == expected
    if not outcome:
        extra_message = f'''The sets you've identified are: {observed}
    The expected list is: {expected}
                            '''
    else:
        extra_message = None

    give_message(outcome, extra_message)
    return None


def cleaned_set_names(df_cleaned):
    observed = set(df_cleaned['SetName'].unique())
    banned = set(
        ['LEGO® DUPLO® Green Baseplate', 'LEGO® Power Functions Motor Set', "Replace 'My First Cars and Trucks",
         'Moana’s Ocean Voyage', "Vaiana's Ocean Voyage", 'LEGO® DIMENSIONS™ PLAYSTATION® 4 Starter Pack', 'Slave I™'])

    intersect = observed & banned
    if intersect:
        outcome = False
        extra_message = f'''The SetName column in your dataframe, df_cleaned, still has the following entries: {intersect}'''
    else:
        outcome = True
        extra_message = None

    give_message(outcome, extra_message)
    return None


def unique_ages(unique_ages):
    observed = unique_ages
    observed.sort()
    expected = ['0', '02-May', '04-Jul', '05-Aug', '05-Dec', '06-Dec', '07-Dec', '08-Dec', '09-Dec', '10+', '12+',
                '14+', '16+', '1½-3', '1½-5', '4+', '5+', '6+', '7+', '8+', '9+', 'Apr-99', 'Aug-14', 'Dec-16',
                'Jul-14', 'Jun-14', 'Nov-16', 'Oct-14', 'Oct-16', 'Oct-21', 'Sep-14', 'Sep-16']

    outcome = observed == expected
    if not outcome:
        extra_message = f'''The values you've identified in unique_ages are: {observed}
    The expected list is: {expected}
                            '''
    else:
        extra_message = None

    give_message(outcome, extra_message)
    return None


def ages_cleaned(df_cleaned):
    observed = [x for x in df_cleaned['Ages'].unique() if not np.isnan(x)]
    observed.sort()

    expected = [0.0, 1.5, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0]

    outcome = observed == expected
    if not outcome:
        extra_message = f'''The ages column in your dataframe has the following values in it: {observed}
    After cleaning, it should only have: {expected}
                            '''
    else:
        extra_message = None

    give_message(outcome, extra_message)
    return None


def difficulty_cleaned(df_cleaned):
    observed = [x for x in df_cleaned['ReviewDifficulty'].unique() if type(x) == str]
    observed.sort()

    expected = ['Average', 'Challenging', 'Easy', 'Very Challenging', 'Very Easy']

    outcome = observed == expected
    if not outcome:
        extra_message = f'''The ReviewDifficulty column in your dataframe has the following values in it: {observed}
    After cleaning, it should only have: {expected}
                            '''
    else:
        extra_message = None

    give_message(outcome, extra_message)
    return None


def new_reviews(observed):

    # Test datatype
    if not type(observed) == pd.DataFrame:
        extra_message = "Your variable, 'new_reviews' is not a pandas dataframe. Review the type."
        give_message(False, extra_message)
        return None

    # Test cols
    columns = list(observed.columns)
    columns.sort()
    if not columns == ['ProdID', 'ReviewDifficulty']:
        extra_message = "Your variable, 'new_reviews' does not have columns ['ProdID', 'ReviewDifficulty']"
        give_message(False, extra_message)
        return None

    # Test ProdIDs all contained
    expected = pd.read_csv('../Data/Assertions/NewReviews.csv')
    expected_ids = set(expected['ProdID'].unique())
    observed_ids = set(observed['ProdID'].unique())
    diff_ids = expected_ids.difference(observed_ids)
    if diff_ids:
        extra_message = f"Your dataframe is missing the following ProdID values: \n {diff_ids}"
        give_message(False, extra_message)
        return None

    # Test uniqueness of ProdIDs
    dupes = observed.groupby(['ProdID'])['ReviewDifficulty'].count().reset_index()
    dupes = dupes.loc[dupes['ReviewDifficulty'] > 1]
    if not dupes.empty:
        dupes = list(dupes['ProdID'])
        extra_message = f"Your dataframe has >1 row for the following ProdIDs: \n {dupes}"
        give_message(False, extra_message)
        return None

    # Test matching of ReviewDifficulty
    merged = expected.merge(observed, on='ProdID', how='inner',
                            suffixes = ('_exp','_obs'))
    merged = merged.loc[~(merged['ReviewDifficulty_exp'] == merged['ReviewDifficulty_exp'])]
    if not merged.empty:
        dupes = list(merged['ProdID'])
        extra_message = f"Your dataframe has incorrect 'ReviewDifficulty' values for the following ProdIDs: \n {dupes}"
        give_message(False, extra_message)
        return None
    else:
        give_message(True)

    return None


def updated_reviews(df_cleaned):

    observed = df_cleaned[['ProdID','ReviewDifficulty']].drop_duplicates()
    return new_reviews(observed)


def new_weights(df_cleaned):
    observed = df_cleaned[['ProdID','WeightGrs']].drop_duplicates()
    expected = pd.read_csv('../Data/Assertions/NewWeights.csv')

    # Test matching of ReviewDifficulty
    merged = expected.merge(observed, on='ProdID', how='inner',
                            suffixes=('_exp', '_obs'))
    merged = merged.loc[~(merged['WeightGrs_exp'] == merged['WeightGrs_exp'])]
    if not merged.empty:
        dupes = list(merged['ProdID'])
        extra_message = f"Your dataframe has incorrect 'WeightGrs' values for the following ProdIDs: \n {dupes}"
        give_message(False, extra_message)
        return None
    else:
        give_message(True)

    return None


def unique_piececount(unique_piececount):
    observed = list(unique_piececount['ProdID'].unique())
    observed.sort()
    expected = [42033, 75181, 75212]

    outcome = observed == expected
    if not outcome:
        extra_message = f'''The values observed in unique_piececount are: {observed}
        The expected list is: {expected}
                                 '''
    else:
        extra_message = None

    give_message(outcome, extra_message)
    return None


def new_piececounts(df_cleaned):
    observed = df_cleaned[['ProdID','PieceCount']].loc[df_cleaned['ProdID'].isin([42033, 75181, 75212])].drop_duplicates()
    outcome = len(observed) == 3
    if not outcome:
        extra_message = f'''Something is wrong with the update of 'PieceCount'!'''
    else:
        extra_message = None

    give_message(outcome, extra_message)
    return None


def country_additions(df_cleaned):
    cols = set(df_cleaned.columns)
    target_cols = {'Country', 'CountryName', 'Currency'}
    diff = target_cols.difference(cols)
    if diff:
        extra_message = f"Your dataframe doesn't contain the following columns: {diff}"
        give_message(False, extra_message)
        return None

    # Test duplicates
    expected = pd.read_csv('../Data/Assertions/CountryVals.csv')
    observed = df_cleaned[['Country', 'CountryName', 'Currency']].drop_duplicates()
    observed_counts = observed.groupby('Country')['CountryName', 'Currency'].count().reset_index()
    observed_counts = observed_counts.loc[(observed_counts['CountryName'] > 1 ) | (observed_counts['Currency'] > 1 )]
    if not observed_counts.empty:
        extra_message = f"There were duplicates in your data: {observed_counts}"
        give_message(False, extra_message)
        return None

    merge = expected.merge(observed, on='Country', how='inner', suffixes=('_Expected','_Observed'))
    merge = merge.loc[~(merge['CountryName_Expected'] == merge['CountryName_Observed']) | ~(merge['Currency_Expected'] == merge['Currency_Observed'])]
    if not merge.empty:
        extra_message = f"There were some inconsistencies in the results of your dataframe: {merge}"
        give_message(False, extra_message)
        return None
    else:
        give_message(True)
        return None

    return None


