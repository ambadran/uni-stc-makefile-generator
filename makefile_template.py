"""

"""
from defaults import STC_MCU_dict, STC_SPEC

def generate_Makefile(mcu_variant: str, mcu_freq_khz: int):
    '''

    returns the string content of the Makefile
    '''
    mcu_specs = STC_MCU_dict[mcu_variant]
    string = f"""
MCU_FREQ_KHZ := {mcu_freq_khz}
STACK_SIZE := {mcu_specs.stack_size}
XRAM_SIZE := {mcu_specs.xram_size}
FLASH_SIZE := {mcu_specs.code_size} 
MEMORY_MODEL := --model-{mcu_specs.memory_model}
HAS_DUAL_DPTR := {mcu_specs.has_dual_dptr}

MCU_VARIANT = {mcu_variant}

include ./Makefiles/inc_common1.mk
include ./Makefiles/inc_src.mk
include ./Makefiles/inc_common2.mk"""
    return string


