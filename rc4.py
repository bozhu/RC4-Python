#!/usr/bin/env python

def KSA(key):
    keylength = len(key)

    S = []
    for i in range(256):
        S.append(i)

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i] # swap

    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i] # swap
        
        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key):
    S = KSA(key)
    return PRGA(S)


if __name__ == '__main__':
    key = 'Key'
    #key = 'Wiki'
    #key = 'Secret'
    # test vectors are from http://en.wikipedia.org/wiki/RC4

    def convert_key(string):
        output_list = []
        for c in string:
            output_list.append(ord(c))
        return output_list

    key = convert_key(key)

    keystream = RC4(key)

    import sys
    for i in range(10):
        sys.stdout.write("%02x" % keystream.next())
    print

