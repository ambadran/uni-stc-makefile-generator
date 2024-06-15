# Makefile Generator for ANY 'uni-stc' based STC MCU Project

Python program to automate the generation of the necessary Makefiles to ease the compilation and upload of any STC microcontroller
supported by the uni-stc library.

CLI interface for this Program

Installation:

After installing the uni-stc library from `https://codeberg.org/20-100/uni-STC` , edit the default_uni_stc_dir in the defaults.py file.

Usage: 

To creates the Makefile and the Makefiles directory with all the necessary Makfiles

    stcproject new <mcu_variant> <mcu_freq_khz> 

To Updates the inc_src.mk Makefile with the current project needed source files

    stcproject update 
