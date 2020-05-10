cmake_minimum_required(VERSION 3.13)
project(CmakeExample)

set(CMAKE_CXX_STANDARD 11)

execute_process(COMMAND python preparing.py WORKING_DIRECTORY ../C/)

include_directories(C)

add_executable(CmakeExample B/main.cpp B/main.h C)

add_subdirectory(A)

target_link_libraries(CmakeExample MyLib)

# first we can indicate the documentation build as an option and set it to ON by default
option(BUILD_DOC "Build documentation" ON)

# check if Doxygen is installed
find_package(Doxygen)
if (DOXYGEN_FOUND)
    # set input and output files
    set(DOXYGEN_IN ${CMAKE_CURRENT_SOURCE_DIR}/doc/config.dxg)
    set(DOXYGEN_OUT ${CMAKE_CURRENT_SOURCE_DIR}/doc)

    # request to configure the file
    configure_file(${DOXYGEN_IN} ${DOXYGEN_OUT} @ONLY)
    message("Doxygen build started")

    # note the option ALL which allows to build the docs together with the application
    add_custom_target( doc_doxygen ALL
        COMMAND ${DOXYGEN_EXECUTABLE} ${DOXYGEN_OUT}
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
        COMMENT "Generating API documentation with Doxygen"
        VERBATIM )
else (DOXYGEN_FOUND)
  message("Doxygen need to be installed to generate the doxygen documentation")
endif (DOXYGEN_FOUND)