from random import randrange as random
import time

def generate_id(i):
    return f"{time.time()}.{random(0, 10000)}.{i}"