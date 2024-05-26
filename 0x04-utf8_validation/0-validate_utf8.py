#!/usr/bin/python3
""" UTF8 Validation """


def validUTF8(data):
    """ UTF8 Validation """
    def is_valid_byte(byte):
        """validate byte """
        return 0 <= byte <= 255

    n = len(data)
    i = 0

    while i < n:
        byte = data[i]
        if not is_valid_byte(byte):
            return False
        
        # Determine the number of bytes in this character
        num_bytes = 0
        if (byte >> 7) == 0:  # 1-byte character
            num_bytes = 1
        elif (byte >> 5) == 0b110:  # 2-byte character
            num_bytes = 2
        elif (byte >> 4) == 0b1110:  # 3-byte character
            num_bytes = 3
        elif (byte >> 3) == 0b11110:  # 4-byte character
            num_bytes = 4
        else:
            return False
        
        if i + num_bytes > n:
            return False
        
        for j in range(1, num_bytes):
            if (data[i + j] >> 6) != 0b10:
                return False
        
        i += num_bytes
    
    return True
