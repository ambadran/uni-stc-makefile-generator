"""
Variables to define:

"""

# ********************* DICTs **************************** #
# Mapping stack size of each STC uC to the proper value from the datasheet
stack_size_dict = {
        'STC8H8K64U_SKDIP28': 112
        }

# Mapping memory sizes of each STC uC to the proper value from the datasheet
#TODO: the only options I know of that need setting is:
# --xram-loc
# --xram-size
# --stack-size SAME AS BEFORE
# --code-size

# memory_sizes_dict = {
#         'STC8H8K64U_SKDIP28': 
#         }

has_dual_dptr_dict = {
        "STC8H8K64U_SKDIP28": 'y'
        }

# this one depend on the amount of RAM available, see iPad refrence
# i will make it a function that looks at memory_sizes_dict and decides
# memory_model = ''
# ****************************************************** #

# ****************** implementation ***************** #
class ProjectParameters:
    def __init__(self):
        pass

    def get_parameters(self):
        '''
        assigns the parameters
        '''
        pass

def generate_Makefile(project_parameters: ProjectParameters):
    '''

    '''
    string = f"""
# Prerequisites --------------------------------------------------------
#
# Besides make, his project requires: 
#
# - sdcc
# - stcgal-patched
# - minicom
# - doxygen

# Usage ----------------------------------------------------------------
#
# Build executable in release mode:
#   make
#
# Build executable in debug mode:
#   make BUILD_MODE=debug
#
# Build documentation:
#   make doc
#
# Upload executable to MCU:
#   make upload
#
# Open serial console in new window:
#   make console
#
# Clean project (remove all build files):
#   make clean

# Target MCU settings --------------------------------------------------

# Note: using a system clock around 24MHz works with all MCU
# having an internal RC oscillator.
MCU_FREQ_KHZ := {}

STACK_SIZE := {}

MEMORY_SIZES := \
	--xram-loc {} \
	--xram-size {} \
	--stack-size $(STACK_SIZE) \
	--code-size {} 

MEMORY_MODEL := {}

HAS_DUAL_DPTR := {}

MCU_VARIANT = {}

include ./Makefiles/inc_common1.mk
include ./Makefiles/c_src.mk
include ./Makefiles/inc_common2.mk"""
    return string

if __name__ == '__main__':
    # testing

    # defining inc_comm1 variables
    project_name = 'test' 
    console_port = '/dev/ttyUSB0'
    isp_port = '/dev/ttyUSB0'

    # defining Makefile variables
    mcu_variant = "STC8H8K64U_SKDIP28"

    mcu_freq_khz = 23961

    stack_size = stack_size_dict[mcu_variant]
    # memory_sizes = memory_sizes_dict[mcu_variant]
    memory_sizes = "\ \n\t--xram-loc 0 \ \n\t--xram-size 8192 \ \n\t--stack-size $(STACK_SIZE) \ \n\t--code-size 65024"

    # memory_model = memory_model_get(mcu_variant)
    memory_model = '--model-large'

    has_dual_dptr = has_dual_dptr_dict[mcu_variant]







