#!/bin/sh

# This file is executed by build/envsetup.sh, and can use anything
# defined in envsetup.sh.
#
# In particular, you can add lunch options with the add_lunch_combo
# function: add_lunch_combo generic-nand-eng

#note:
#		eng         --->    Developer mode
#       userdebug   --->    release mode

add_lunch_combo halley2_norflash-eng
add_lunch_combo halley2_norflash-user

