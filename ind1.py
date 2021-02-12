#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Написать программу, которая считывает из текстового файла три предложения и выводит их
#в обратном порядке.

import sys

if __name__ == '__main__':
    with open("text.txt", 'r') as f:
        s = f.read().split('.')
        fs = '. '.join(reversed(s))
        print(fs)
