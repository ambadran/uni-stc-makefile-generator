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

print(files_to_check)

# Step 2: get the names of all the hal files from the uni-stc library
hal_files = []
all_files = os.listdir(os.path.expanduser(default_uni_stc_dir) + 'hal/')
is_h_file = lambda x: os.path.splitext(x)[1] in ['.h', '.asm']
hal_files_to_be_included = list(filter(is_h_file, all_files))

print(hal_files_to_be_included)

# Step 3: find the file in the project from step 1 that has any of the hal files found in step 2
included_hal_files = []
for file in files_to_check:
    with open(file, 'r') as f:
        f_content = f.read()
        for hal_file in hal_files_to_be_included:
            print(hal_file, file)
            if hal_file in f_content:
                file_name, _ = os.path.splitext(hal_file)
                included_hal_files.append(file_name)  # adding the basename only, the .c will be added in step4

print(included_hal_files)

# Step 4: include all the src c files in the inc_src.mk
if not os.path.isfile('Makefiles/inc_src.mk'):
    raise FileNotFoundError("inc_src.mk is yet generated! please run `stcproject` first!")

with open('Makefiles/inc_src.mk', 'w') as f:
    f.write("SRCS := ")

    for included_hal_file in included_hal_files:
            f.write(f"\\ \n\t$(HAL_DIR)/{included_hal_file}.c")

    for project_src_file in project_src_files:
            f.write(f"\\ \n\t{project_src_file}")

        


