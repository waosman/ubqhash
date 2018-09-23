#!/usr/bin/env python
import os
from distutils.core import setup, Extension
sources = [
    'src/python/core.c',
    'src/libubqhash/io.c',
    'src/libubqhash/internal.c',
    'src/libubqhash/sha3.c']
if os.name == 'nt':
    sources += [
        'src/libubqhash/util_win32.c',
        'src/libubqhash/io_win32.c',
        'src/libubqhash/mmap_win32.c',
    ]
else:
    sources += [
        'src/libubqhash/io_posix.c'
    ]
depends = [
    'src/libubqhash/ethash.h',
    'src/libubqhash/compiler.h',
    'src/libubqhash/data_sizes.h',
    'src/libubqhash/endian.h',
    'src/libubqhash/ethash.h',
    'src/libubqhash/io.h',
    'src/libubqhash/fnv.h',
    'src/libubqhash/internal.h',
    'src/libubqhash/sha3.h',
    'src/libubqhash/util.h',
]
pyethash = Extension('pyethash',
                     sources=sources,
                     depends=depends,
                     extra_compile_args=["-Isrc/", "-std=gnu99", "-Wall"])

setup(
    name='pyethash',
    author="Matthew Wampler-Doty",
    author_email="matthew.wampler.doty@gmail.com",
    license='GPL',
    version='0.1.23',
    url='https://github.com/ethereum/ethash',
    download_url='https://github.com/ethereum/ethash/tarball/v23',
    description=('Python wrappers for ethash, the ethereum proof of work'
                 'hashing function'),
    ext_modules=[pyethash],
)
