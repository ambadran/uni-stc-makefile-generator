"""

"""
from defaults import *
from makefile_template import generate_Makefile
from inc_common1_template import generate_inc_common1
from inc_common2_template import generate_inc_common2
import os

# ****************** User inputs **************** #

### Mandatory Program input
mcu_variant = "STC8H8K64U_SKDIP28"  #TODO: get them from terminal input

mcu_freq_khz = 35000  #TODO: get them from terminal input


def main():
    '''
    generates and writes the makefiles
    '''
    ### Step 1: aquire the file contents
    makefile_content = generate_Makefile(mcu_variant, mcu_freq_khz)

    #TODO: implement a check if one of the default values for this function is passed in the command line and should be passed here instead of the default values
    inc_common1_content = generate_inc_common1()

    inc_common2_content = generate_inc_common2()


    ### Step 2: create the directory and the files
    # Step 2a: Create the Makefile file
    with open('Makefile', 'w') as file:
        file.write(makefile_content)

    # Step 2b: Create the Makefiles directory if not already created
    directory = "Makefiles"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Step 2c: add the inc_common1 file
    file_path = os.path.join(directory, "inc_common1.mk")
    with open(file_path, 'w') as file:
        file.write(inc_common1_content)

    # Step 2d: add the inc_common2 file
    file_path = os.path.join(directory, "inc_common2.mk")
    with open(file_path, 'w') as file:
        file.write(inc_common2_content)

    # Step 2c: add the inc_src file
    file_path = os.path.join(directory, "inc_src.mk")
    with open(file_path, 'w') as file:
        file.write("# No files added yet!")

if __name__ == '__main__':
    main()
