from cpython.bytes cimport PyBytes_FromStringAndSize, PyBytes_AsStringAndSize
from libc.stdint cimport uint64_t, int64_t

DEF buf_max_len = 16

cdef bytes leb128_encode_unsigned(uint64_t i):
    assert i >= 0

    cdef int l = 0
    cdef char buf[buf_max_len];
    cdef unsigned char byte;

    for l in range(buf_max_len):
        byte = i & 0x7f
        i = i >> 7

        if i == 0:
            buf[l] = byte
            return PyBytes_FromStringAndSize(<char*> &buf, l + 1)

        buf[l] = 0x80 | byte

    raise OverflowError


cdef uint64_t leb128_decode_unsigned(bytes b):
    cdef Py_ssize_t l = 0;
    cdef char* buf;

    PyBytes_AsStringAndSize(b, &buf, &l)

    cdef uint64_t r = 0;

    for i in range(l):
        r = r + ((buf[i] & 0x7f) << (i * 7))
    return r



class LEB128U:
    @staticmethod
    def encode(i: int) -> bytes:
        return leb128_encode_unsigned(i)

    @staticmethod
    def decode(b: bytes) -> int:
        return leb128_decode_unsigned(b)


cdef bytes leb128_encode_signed(int64_t i):
    cdef int l = 0
    cdef char buf[buf_max_len];
    cdef unsigned char byte;

    for l in range(buf_max_len):
        byte = i & 0x7f
        i = i >> 7

        if (i == 0 and byte & 0x40 == 0) or (i == -1 and byte & 0x40 != 0):
            buf[l] = byte
            return PyBytes_FromStringAndSize(<char*> &buf, l + 1)

        buf[l] = 0x80 | byte

    raise OverflowError


cdef int leb128_decode_signed(bytes b):
    cdef Py_ssize_t l = 0;
    cdef char* buf;

    PyBytes_AsStringAndSize(b, &buf, &l)

    cdef int64_t r = 0;

    for i in range(l):
        r = r + ((buf[i] & 0x7f) << (i * 7))

    if buf[l - 1] & 0x40 != 0:
        r |= - (1 << (i * 7) + 7)

    return r


class LEB128S:
    @staticmethod
    def encode(i: int) -> bytes:
        return leb128_encode_signed(i)

    @staticmethod
    def decode(b: bytes) -> int:
        return leb128_decode_signed(b)
