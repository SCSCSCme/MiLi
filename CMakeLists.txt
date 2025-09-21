cmake_minimum_required(VERSION 3.12)
list(APPEND CMAKE_PREFIX_PATH "C:/pybind11")
project("MiLi")

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 REQUIRED)

add_library(MiLi STATIC MiLi/src/Intface.cpp)
target_include_directories(MiLi PUBLIC MiLi/include)