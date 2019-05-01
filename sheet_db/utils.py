import string
import itertools

ALPHA_COLS = list(
    itertools.chain(
        string.ascii_uppercase, 
       (''.join(pair) for pair in itertools.product(string.ascii_uppercase, repeat=2))
))