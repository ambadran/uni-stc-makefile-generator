"""

"""
from defaults import default_uni_stc_dir, default_project_name, default_console_baudrate, default_console_port, default_isp_port


def generate_inc_common1(uni_stc_dir: str=default_uni_stc_dir, project_name: str=default_project_name, console_baudrate: int=default_console_baudrate, console_port: str=default_console_port, isp_port: str=default_isp_port):
    '''
    generates the inc_common1.mk file
    '''
    string = f"""
# Define UNISTC_DIR, HAL_DIR, DRIVER_DIR, and MAKE_DIR -----------------
include {uni_stc_dir}makefiles/0-directories.mk

# Project settings -----------------------------------------------------
PROJECT_NAME := {project_name}
PROJECT_FLAGS = -DBUILD_FOR_$(MCU_VARIANT)
BUILD_ROOT := $(MCU_VARIANT)
CONSOLE_BAUDRATE := {console_baudrate}
CONSOLE_PORT := {console_port}
ISP_PORT := {isp_port}
# Default is -a, override here if you have specific needs.
STCGAL_OPTIONS := -A rts -a
    """

    return string
