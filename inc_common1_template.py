"""

"""
from defaults import default_uni_stc_dir, default_project_name, default_console_baudrate, get_port


def generate_inc_common1(
        num_of_ports: int = 1,
        uni_stc_dir: str=default_uni_stc_dir, 
        project_name: str=default_project_name, 
        console_baudrate: int=default_console_baudrate ):
    '''
    generates the inc_common1.mk file
    '''
    ports = ""
    for i in range(num_of_ports):
        ports += f"\nCONSOLE_PORT := {get_port(i)}\nISP_PORT := {get_port(i)}\n"

    string = f"""
# Define UNISTC_DIR, HAL_DIR, DRIVER_DIR, and MAKE_DIR -----------------
include {uni_stc_dir}makefiles/0-directories.mk

# Project settings -----------------------------------------------------
PROJECT_NAME := {project_name}
PROJECT_FLAGS = -DBUILD_FOR_$(MCU_VARIANT)
BUILD_ROOT := build
{ports}
CONSOLE_BAUDRATE := {console_baudrate}
# Default is -a, override here if you have specific needs.
STCGAL_OPTIONS := -A rts -a
    """

    return string
