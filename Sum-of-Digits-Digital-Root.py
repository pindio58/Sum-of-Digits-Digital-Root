def digital_root (n):
    summed = sum ([ int (num) for num in str (n) ])
    return summed if len (str (summed)) == 1 else digital_root (summed)