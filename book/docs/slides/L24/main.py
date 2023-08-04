import ctypes

library = ctypes.CDLL("estimate_pi_c.so")

library.estimate_pi.argtypes = [ctypes.c_uint]
library.estimate_pi.restype = ctypes.c_double


pi = library.estimate_pi(1_000_000)
print(pi)
