"""
This file is to manage the different specifications of the different STC MCUs easily
"""
from dataclasses import dataclass
import os
import sys

### PC defaults
# Project Name
default_project_name = os.path.basename(os.getcwd())  # defaults to the name of the directory I am in

# uni-stc directory path
default_uni_stc_dir = "~/.stc/uni-stc/"

# console_port and isp_port 
if sys.platform == 'win32':
    raise NotImplementedError("Need to implement code to find the proper COM port")

elif sys.platform == 'darwin':
    default_console_port = '/dev/tty.usbserial' #TODO: complete this from mac
    default_isp_port = '/dev/tty.usbserial' #TODO: complete this from mac

elif sys.platform == 'linux':
    default_console_port = '/dev/ttyUSB0'
    default_isp_port = '/dev/ttyUSB0'

else:
    raise NotImplementedError("unknown operating system")

# console_baudrate
default_console_baudrate = 115200


### MCU defaults

@dataclass
class STC_SPEC:
    name: str 
    xram_loc: int
    xram_size: int
    stack_size: int
    code_size: int
    has_dual_dptr: str = 'y'  # all STC to compiled by SDCC must have dual dptr register

    @property
    def memory_model(self):
        return 'medium' if self.xram_size <=256 else 'large'

### Define all the STC MCUs to be used here, get the spec values from the datasheet ###
STC_MCU_dict = {"STC8H8K64U_SKDIP28": STC_SPEC(
        name='STC8H8K64U_SKDIP28',
        xram_loc = 0,
        xram_size = 8192,
        stack_size = 112,
        code_size = 65024
        ) }


