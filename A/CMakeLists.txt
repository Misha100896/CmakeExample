cmake_minimum_required(VERSION 3.13)
project(MyLib)

set(SOURCE_LIB lib.cpp)

add_library(MyLib STATIC ${SOURCE_LIB})

