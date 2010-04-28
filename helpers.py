def ip_to_long(text):
    w, x, y, z = map(int, text.split('.'))
    return 16777216*w + 65536*x + 256*y + z

def long_to_ip(number):
    number = long(number)
    z = number % 256
    number >>= 8
    y = number % 256
    number >>= 8
    x = number % 256
    number >>= 8
    w = number % 256
    return '%d.%d.%d.%d' % (w, x, y, z)
