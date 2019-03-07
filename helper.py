import random
import hashlib


def random_hash():
    try:
        x = str(random.randint(0, 9999))
        hash = hashlib.shake_256(str.encode(x)).hexdigest(3)
        return hash
    except TypeError:
        pass
