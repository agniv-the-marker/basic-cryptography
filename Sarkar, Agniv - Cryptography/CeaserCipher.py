start_letter = "a"
end_letter   = "z"

start = ord(start_letter)
end = ord(end_letter)
length = end - start + 1

encrypt = lambda message, shift : ''.join(map(chr, [(ord(m) - start + shift) % length + start for m in message]))
decrypt = lambda message, shift : encrypt(message, (-1 * shift) % length)

substitution = lambda message, key : ''.join([key[ord(m) - start] for m in message])

def inverse(key):
    undo = [''] * length
    for i, k in enumerate(key):
        undo[ord(k) - start] = chr(i + start)
    return ''.join(undo)

undo_substitution = lambda message, key : substitution(message, inverse(key))
