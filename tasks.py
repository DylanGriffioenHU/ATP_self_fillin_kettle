""" Task definitions for invoke command line utility for python bindings
    overview article.
"""
import invoke
import pathlib
import sys
import os
import shutil
import re
import glob

on_win = sys.platform.startswith("win")


@invoke.task
def clean(c):
    """Remove any built objects"""
    for file_pattern in (
        "*.o",
        "*.so",
        "*.obj",
        "*.dll",
        "*.exp",
        "*.lib",
        "*.pyd",
        "cffi_example*",  # Is this a dir?
        "cython_wrapper.cpp",
    ):
        for file in glob.glob(file_pattern):
            os.remove(file)
    for dir_pattern in "Release":
        for dir in glob.glob(dir_pattern):
            shutil.rmtree(dir)


def print_banner(msg):
    print("==================================================")
    print("= {} ".format(msg))

@invoke.task()
def test_ctypes_cpp(c):
    """Run the script to test ctypes"""
    print_banner("Testing ctypes Module for C++")
    # pty and python3 didn't work for me (win).
    if on_win:
        invoke.run("python main.py")
    else:
        invoke.run("python3 main.py", pty=True)

@invoke.task()
def build_tempSensor(c):
    """Build the shared library for the sample C++ code"""
    print_banner("Building C++ Library")
    invoke.run(
        "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC tempSensor.cpp "
        "-o libtempSensor.so "
    )
    print("* Complete")


def compile_python_module(cpp_name, extension_name):
    invoke.run(
        "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC "
        "`python3 -m pybind11 --includes` "
        "-I . "
        "{0} "
        "-o {1}`python3-config --extension-suffix` "
        "-L. -ltempSensor -Wl,-rpath,.".format(cpp_name, extension_name)
    )


@invoke.task(
    clean,
    build_tempSensor,
    test_ctypes_cpp,
)
def all(c):
    """Build and run all tests"""
    pass
