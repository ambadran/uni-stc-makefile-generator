"""
CLI interface for this Program

Usage: 

    - stcproject new <mcu_variant> <mcu_freq_khz> 
        -> creates the Makefile and the Makefiles directory with all the necessary Makfiles

    - stcproject update 
        -> updates the inc_src.mk Makefile with the current project needed source files
"""
import argparse
from main import main
from defaults import STC_MCU_dict
import os
from update_src_file import update_src_file

def cli():
    '''
    function to creat the cli functionality
    '''
    # Create the parser
    parser = argparse.ArgumentParser(description=__doc__)

    # Add arguments
    supported_commands = ['new', 'update']

    parser.add_argument('command', type=str, choices=supported_commands, help='`new` to create Makefiles for this project, `update` to update SRC files')
    parser.add_argument('mcu_variant', type=str, nargs='?', default='', help='STC MCU variant, e.g- STC8H8K64U_SKDIP28')
    parser.add_argument('mcu_freq_khz', type=int, nargs='?', default=0, help='STC MCU running frequency in kHz, e.g - 35000 for 35MHz')
    #TODO: add an optional parameter for the number of mcus to include, it must default to 1.

    # Parse the arguments
    args = parser.parse_args()

    if args.command == 'new':

        ### Checks before executing main()
        known_STC_MCUs = list(STC_MCU_dict.keys())
        if not args.mcu_variant:
            raise ValueError("Please Enter the STC MCU Variant, e.g- STC8H8K64U_SKDIP28")

        elif type(args.mcu_variant) != str:
            raise ValueError("mcu_variant must be a string\n")

        elif args.mcu_variant not in known_STC_MCUs:
            current_dir = os.getcwd()
            raise ValueError(f"Unknown STC MCU, please add it's specifications in the {current_dir}default.py file\nSupported STC MCUs:\n{known_STC_MCUs}\n")

        if not args.mcu_freq_khz:
            raise ValueError("Please Enter the MCU Clock Frequency parameter\n")

        ### Executing main()
        main(args.mcu_variant, args.mcu_freq_khz)

    elif args.command == 'update':

        ### Checking for no arguments
        if args.mcu_variant or args.mcu_freq_khz:
            raise ValueError("`update` command doesn't take any arguments")

        ### Executing update_src_files()
        update_src_file()

if __name__ == '__main__':
    cli()
