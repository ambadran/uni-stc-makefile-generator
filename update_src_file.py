'''
This script updates inc_src.mk with all the .c files in the Project or in used from the uni-stc hal library

#TODO: this script should be run automatically when running `make`

it checks the inc_src.mk file everytime it's run for:
    1- any `hal` file from the uni-stc library included in the code
    2- any c file added in the project directory

if any is found it addes them in the inc_src.mk file
'''
import os
from defaults import default_uni_stc_dir

def update_src_file():
    '''
    Re-writes the inc_src.mk file with current needed src files
    '''
    # Step 1: get the names of all the files in the project directory that could have a `#include` statement
    #           also find the project source files to be added too in step5
    files_to_check = []
    project_src_files = []
    for file in os.listdir():
        _, ext = os.path.splitext(file)

        if ext in ['.h', '.c']:
            files_to_check.append(file)

        if ext == '.c':
            project_src_files.append(file)

    # Step 2: get the names of all the hal files from the uni-stc library
    hal_files = []
    all_files = os.listdir(default_uni_stc_dir + 'hal/')
    is_h_file = lambda x: os.path.splitext(x)[1] in ['.h', '.asm']
    hal_files_to_be_included = list(filter(is_h_file, all_files))
    hal_files_to_be_included.remove('hal-defs.h')

    # Step 3: find the file in the project from step 1 that has any of the hal files found in step 2
    included_hal_files = []
    for file in files_to_check:
        with open(file, 'r') as f:
            f_content = f.read()
            for hal_file in hal_files_to_be_included:
                if hal_file in f_content:
                    file_name, _ = os.path.splitext(hal_file)
                    included_hal_files.append(file_name)  # adding the basename only, the .c will be added in step4

    # Step 4: find the needed hal files that is included in the included hal files of the source code ;)
    included_inside_included_hal_files = set()
    for file in included_hal_files:
        with open(f"{default_uni_stc_dir}hal/{file}.h", 'r') as f:
            f_content = f.read()
            for hal_file in hal_files_to_be_included:
                if hal_file in f_content:
                    file_name, _ = os.path.splitext(hal_file)
                    included_inside_included_hal_files.add(file_name)  # adding the basename only, the .c will be added in step4

        with open(f"{default_uni_stc_dir}hal/{file}.c", 'r') as f:
            f_content = f.read()
            for hal_file in hal_files_to_be_included:
                if hal_file in f_content:
                    file_name, _ = os.path.splitext(hal_file)
                    included_inside_included_hal_files.add(file_name)  # adding the basename only, the .c will be added in step4

    included_inside_included_hal_files.update(included_hal_files)
    all_hal_files = list(included_inside_included_hal_files)

    # Step 4: include all the src c files in the inc_src.mk
    if not os.path.isfile('Makefiles/inc_src.mk'):
        raise FileNotFoundError("inc_src.mk is yet generated! please run `stcproject` first!")

    with open('Makefiles/inc_src.mk', 'w') as f:
        f.write("SRCS := ")

        for hal_file in all_hal_files:
            f.write(f" \\\n\t$(HAL_DIR)/{hal_file}.c")

        for project_src_file in project_src_files:
            f.write(f" \\\n\t{project_src_file}")

        f.write("\n")
            


