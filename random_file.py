import random
import string

text = "".join(random.sample(string.ascii_letters, k=10))
with open(f"{text}.txt", 'w') as file:
    file.write(text)
