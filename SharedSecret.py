import numpy as np

def split_secret(s, n):
    '''
    :param s: character string
    :param n: number
    :return: numpy array. shape = (len(s), n). dtype = uint8. Codes to
    be distributed to n individuals.
    '''
    q = np.random.randint(0, 255, size=(len(s), n), dtype='uint8')
    for c_i, c in enumerate(s):
        c = ord(c)
        for i in range(0, n - 1):
            c = c ^ q[c_i, i]
        q[c_i, n-1] = c
    return q

def recover_secret(q):
    '''
    numpy array. shape = (len(s), n). dtype = uint8. Codes that were
    distributed to n individuals.
    :param q:
    :return:
    '''
    len_s, n = q.shape
    char_codes = np.zeros(len_s, dtype='uint8')
    for c_i in range(0, len_s):
        for i in range(0, n):
            char_codes[c_i] = char_codes[c_i] ^ q[c_i, i]
    chars = [chr(char_code) for char_code in char_codes]
    return ''.join(chars)


s = "The rain in Spain falls mainly on the plain"
n = 20
q = split_secret(s, n)
s_recovered = recover_secret(q)
print(s_recovered)