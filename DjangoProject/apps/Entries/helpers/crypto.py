import random
import string

def generate_secret(length: int = 8) -> str:
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_string