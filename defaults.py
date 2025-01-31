"""
This file is to manage the different specifications of the different STC MCUs easily
"""
from dataclasses import dataclass
import os
import sys

### MCU defaults
@dataclass
class STC_SPEC:
    name: str 
    xram_loc: int
    xram_size: int
    stack_size: int
    code_size: int
    has_dual_dptr: str

    @property
    def memory_model(self):
        return 'medium' if self.xram_size <=256 else 'large'

### Define all the STC MCUs to be used here, get the spec values from the datasheet ###
STC_MCU_dict = {"STC8H8K64U_SKDIP28": STC_SPEC(
            name='STC8H8K64U_SKDIP28',
            xram_loc = 0,
            xram_size = 8192,
            stack_size = 112,
            code_size = 65024,
            has_dual_dptr = 'y'
        ),
        "STC8H8K64U_SOP16": STC_SPEC(
            name='STC8H8K64U_SKDIP28',
            xram_loc = 0,
            xram_size = 8192,
            stack_size = 112,
            code_size = 65024,
            has_dual_dptr = 'y'
        ),

        "STC8H8K64U_PDIP40": STC_SPEC(
            name='STC8H8K64U_PDIP40',
            xram_loc = 0,
            xram_size = 8192,
            stack_size = 112,
            code_size = 65024,
            has_dual_dptr = 'y'
        ),


        "STC8G1K08_SOP16": STC_SPEC(
            name='STC8G1K08_SOP16',
            xram_loc=0,
            xram_size=1024,
            stack_size=112,
            code_size=8000,
            has_dual_dptr = 'y'
            ),

        "STC15W408AS_SKDIP28": STC_SPEC(
            name='STC15W408AS_SKDIP28',
            xram_loc=0,
            xram_size=512,
            stack_size=112,
            code_size=8000,
            has_dual_dptr = 'n'
        ),

        "STC15W408AS_DIP16": STC_SPEC(
            name='STC15W408AS_DIP16',
            xram_loc=0,
            xram_size=512,
            stack_size=112,
            code_size=8000,
            has_dual_dptr = 'n'
        )
        }


### PC defaults
# Project Name
default_project_name = os.path.basename(os.getcwd())  # defaults to the name of the directory I am in

# uni-stc directory path
default_uni_stc_dir = os.path.expanduser("~/.stc/uni-stc/")

# console_baudrate
default_console_baudrate = 115200

# console_port and isp_port 
def get_port(num):
    '''
    returns the default path of the TTL converter in each system 
    Parameter num is which ttl converter path to return in case >1
    stc uC to program at same time
    '''
    if num < 0:
        raise ValueError("wrong num range")

    if sys.platform == 'win32':
        raise NotImplementedError("Need to implement code to find the proper COM port")

    elif sys.platform == 'darwin':

        # mac paths are wierd like /dev/tty.usbserial101
        # this dictionary is to link the id of the stc mcu and the wierd numbering scheme of mac
        NUM_TO_MAC_DIGIT = [101, 102]

        return f"/dev/tty.usbserial{NUM_TO_MAC_DIGIT[num]}"

    elif sys.platform == 'linux':
        return f"/dev/ttyUSB{num}"

    else:
        raise NotImplementedError("unknown operating system")




