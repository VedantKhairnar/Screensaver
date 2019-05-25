import string,random,time
chars = string.ascii_letters+"   "+"          "+"                  "+"                     "
size = 2100
def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for _ in range(str_size))

while 1:
    print(random_string_generator(size,chars))
    time.sleep(0.1)
