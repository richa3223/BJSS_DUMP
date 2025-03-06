"""
 Helper module for assertions and testing statements in the playing-with-lego.ipynb notebook

 Author: Matt McFahn
 Created: 06/06/2021
"""


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
        print('''( ͡❛ ͜ʖ ͡❛) Good job! Lego's looking pretty clean.''')
    else:
        print('''( ͡❛ ︵ ͡❛) This Lego still needs some cleaning...''')
    if extra_message:
        print(extra_message)

    return None


def data_loaded():
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
        extra_message = "The df variable wasn't found - have you loaded it properly?"

    give_message(outcome, extra_message)

    return None
