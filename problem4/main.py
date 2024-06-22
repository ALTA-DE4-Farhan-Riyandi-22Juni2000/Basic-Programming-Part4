def ubah_huruf(sentence):
    # Buat peta pengganti berdasarkan penggeseran alfabet sebanyak 10 posisi
    standard_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = "KLMNOPQRSTUVWXYZABCDEFGHIJ"

    # Buat dictionary untuk peta pengganti
    substitution_map = {standard_alphabet[i]: shifted_alphabet[i] for i in range(len(standard_alphabet))}

    # Proses setiap karakter dalam kalimat masukan
    result = []
    for char in sentence:
        if char in substitution_map:
            result.append(substitution_map[char])
        else:
            result.append(char)

    return ''.join(result)


if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB