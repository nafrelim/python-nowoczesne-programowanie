blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
# the_bytes[1] = 4  # nie można modyfikować zmiennej typu bytes
print(the_bytes)

the_byte_array = bytearray(blist)
print(the_byte_array)
the_byte_array[1] = 127
print(the_byte_array)

the_bytes = bytes(range(0,255))
print(the_bytes)
the_byte_array = bytearray(range(0,255))
print(the_byte_array)

import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
print(data[:8])
print(data[16:20])
print(data[20:24])
print(0x9a)
print(0x8d)
if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24])
    print('Poprawny plik PNG, szerokość', width, 'wysokość', height)
else:
    print('To nie jest poprawny plik PNG')