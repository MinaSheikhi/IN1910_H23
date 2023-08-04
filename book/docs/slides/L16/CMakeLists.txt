project(calculator_project
    LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 14)

add_executable(calculator
    calculator.cpp
    test_calculator.cpp
)
