"""
MIT License

Copyright (c) 2021 B.Jothin kumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Author: Jothin kumar (https://jothin-kumar.github.io/)
Original repository link: https://github.com/Jothin-kumar/virtual-operating-system
"""
import sys
from os import listdir
from os.path import realpath, join
from current_dir import cd as cd_, get_VOS_dir
import time


def shutdown(args):
    print('Shutting down...')
    time.sleep(1.5)
    sys.exit()


def echo(args):
    for arg in args:
        print(arg, end=' ')
    print('', end='\n')


def cd(args):
    dir_ = ''
    for arg in args:
        dir_ += arg
    cd_(dir_)


def dir_(args):
    parent_dir = get_VOS_dir()
    for arg in args:
        parent_dir = realpath(join(parent_dir, arg))
    for file_or_folder in listdir(parent_dir):
        print(file_or_folder)
