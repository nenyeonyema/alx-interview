#!/usr/bin/python3
def validUTF8(data):
    def is_valid_byte(byte):
        return 0 <= byte <= 255

    n = len(data)
    i = 0

    while i < n:
        byte = data[i]
        if not is_valid_byte(byte):
            return False
        
        if byte >> 7 == 0:  # 1-byte character
            i += 1
            continue
        
        # Determine the number of bytes in this character
        num_bytes = 0
        if (byte >> 5) == 0b110:  # 2-byte character
            num_bytes = 2
        elif (byte >> 4) == 0b1110:  # 3-byte character
            num_bytes = 3
        elif (byte >> 3) == 0b11110:  # 4-byte character
            num_bytes = 4
        else:
            return False
        
        if i + num_bytes > n:
            return False
