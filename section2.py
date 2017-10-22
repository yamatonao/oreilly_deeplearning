# -*- coding: utf_8 -*-

"""
    section 2 programs
    this is doc string
"""

import numpy as np

def and_block(input1, input2):
    "this is function doc string"
    matrix_input = np.array([input1, input2])
    matrix_weight = np.array([0.5, 0.5])
    bias = -0.7
    tmp = np.sum(matrix_weight * matrix_input) + bias
    if tmp <= 0:
        return 0
    return 1

def nand_block(input1, input2):
    "this is function doc string"
    matrix_input = np.array([input1, input2])
    matrix_weight = np.array([-0.5, -0.5])
    bias = 0.7
    tmp = np.sum(matrix_input * matrix_weight) + bias
    if tmp <= 0:
        return 0
    return 1

def or_block(input1, input2):
    "this is fuction doc string"
    matrix_input = np.array([input1, input2])
    matrix_weight = np.array([0.5, 0.5])
    bias = -0.2
    tmp = np.sum(matrix_weight*matrix_input) + bias
    if tmp <= 0:
        return 0
    return 1

def xor_block(input1, input2):
    "this is function doc string"
    section1 = nand_block(input1, input2)
    section2 = or_block(input1, input2)
    output = and_block(section1, section2)
    return output

#main point
print(xor_block(0, 0), end='')
print(xor_block(0, 1), end='')
print(xor_block(1, 0), end='')
print(xor_block(1, 1))
