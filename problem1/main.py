def play_with_asterisk(n):
    pattern = ""
    for i in range(1, n + 1):
        # Menghitung jumlah spasi di awal baris
        spaces = " " * (n - i)
        # Membuat pola bintang dengan spasi di antara mereka
        stars = "* " * i
        # Menggabungkan spasi dan bintang, lalu menambahkan newline di akhir
        pattern += spaces + stars.rstrip() + " \n"
    return pattern


if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """
