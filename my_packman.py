import struct

def ushort_uint(buffer):

	short_int = buffer[:2]
	short_int = int.from_bytes(short_int, byteorder='big')

	uint = buffer[2:6]
	uint = int.from_bytes(uint, byteorder='big')

	return short_int, uint

def buf2latin(buf):
    size = struct.unpack(">H", buf[:2])[0]
    s = buf[2:2+size].decode("latin1")
    return size, s

def ascii2buf(*strings):
    num_elements = len(strings)
    buf = struct.pack(">I", num_elements)
    for s in strings:
        size = len(s)
        buf += struct.pack(">H", size)
        buf += s.encode("ascii")
    return buf


