
def show_bitboard(bitboard: int) -> None:
    bits = []
    while bitboard > 0:
        bits.append(bitboard % 2);
        bitboard //= 2
    

    if len(bits) < 32:
        while len(bits) < 32:
            bits.append(0)
    else:
        while len(bits) < 64:
            bits.append(0)

    for i, bit in enumerate(reversed(bits)):
        print(bit, end=' ')
        if (i + 1) % 8 == 0 and i != 0:
            print(end='\n')


