cmake_minimum_required(VERSION 3.13)
project(CmakeExample)

set(CMAKE_CXX_STANDARD 11)

execute_process(COMMAND python preparing.py WORKING_DIRECTORY ../C/)

include_directories(C)

add_executable(CmakeExample B/main.cpp B/main.h C)

add_subdirectory(A)

target_link_libraries(CmakeExample MyLib)
