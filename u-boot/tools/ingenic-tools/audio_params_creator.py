#!/usr/bin/python

import math
import sys

exprate = (
    8000.0, 11025.0, 12000.0, 16000.0,
    22050.0, 24000.0, 32000.0, 44100.0,
    48000.0, 88200.0, 96000.0
)


def cacule_div(rate, pll):
    M = 1.0
    N = 1.0
    min = 65535.0
    SAVEM = 1.0
    SAVEN = 1.0

    M = pll % rate
    N = pll / rate
    if M == 0:
        SAVEM = 1
        SAVEN = N
    else:
        for M1 in range(1, 0xff):
            M = 0xff - M1
            N = int(pll * M / rate)
            if N > (65535 << 2):
                continue
            tmpval = abs(float(pll) * M / N - rate)
            if tmpval < min:
                min = tmpval
                SAVEM = M
                SAVEN = N

    print("\t{%d, %d},\\" % (int(SAVEM), int(SAVEN)))


def get_aduio_div(apll, mpll):

    print("#define AUDIO_DIV_VALUES { \\")
    for rate in exprate:
        cacule_div(rate, apll)

    for rate in exprate:
        cacule_div(rate, mpll)

    print("\t}\n")


def file_head_print():
    print("/*")
    print(" * DO NOT MODIFY. ")
    print(" *")
    print(" * This file was generated by audio_params_creator.py")
    print(" *")
    print(" */")
    print("")

    print("#ifndef __AUDIO_DIV_VALUES_H__")
    print("#define __AUDIO_DIV_VALUES_H__")
    print



def file_end_print():
    print("#endif /* __AUDIO_DIV_VALUES_H__ */")

def main(argv):
    if len(argv) - 1 < 2:
        print("input argument num %d < 2" % (len(argv) - 1))


    apll = int(argv[1])
    mpll = int(argv[2])

    file_head_print()
    get_aduio_div(apll, mpll)
    file_end_print()


if __name__ == '__main__':
    main(sys.argv)
