def block_decode(blocks: list[int], block_size: int = 1) -> str:
    """Performs the inverse of block_encode

    Args:
        blocks: a list of integers that encode the message
        block_size: how many bytes each block contains. The final block is padded
            with zeros.

    Returns:
        message: the original string

    Examples:
        >>> block_decode([1685022522, 552640400, 3053453312], 4)
        'dog: 🐶'
    """
    decoded = [block.to_bytes(block_size, 'big') for block in blocks]
    decoded[-1] = decoded[-1].rstrip(int(0).to_bytes(1, 'big'))
    seq = b''
    for d in decoded:
        seq += d
    return seq.decode()

def block_encode(message: str, block_size: int = 1) -> list[int]:
    """Perform our encoding scheme to convert a string into a list of integers.
    The string is encoded into UTF-8 and then split into consecutive blocks.
    Each block of bytes is then returned as the corresponding order, in big-byte
    order.

    Args:
        message: string to be encoded
        block_size: how many bytes each block contains. The final block is padded
            with zeros.

    Returns:
        blocks: a list of integers that encode the message

    Examples:
        >>> block_encode('dog: 🐶', 4)
        [1685022522, 552640400, 3053453312]
    """
    seq = message.encode()
    seq += int(0).to_bytes((-1 * len(seq)) % block_size, 'big')
    blocks = [seq[i:i+block_size] for i in range(0, len(seq), block_size)]
    return list(map(int.from_bytes, blocks))


if __name__ == "__main__":
    s = 'dog: 🐶'
    k = 4

    assert block_encode(s, 4) == [1685022522, 552640400, 3053453312]
    assert block_decode([1685022522, 552640400, 3053453312], 4) == s
    assert s == block_decode(block_encode(s, k), k)