Python program to automate the generation of the necessary Makefiles to ease the compilation and upload of any STC microcontroller
supported by the uni-stc library.

CLI interface for this Program

Usage: 

    - stcproject new <mcu_variant> <mcu_freq_khz> 
        -> creates the Makefile and the Makefiles directory with all the necessary Makfiles

    - stcproject update 
        -> updates the inc_src.mk Makefile with the current project needed source files

