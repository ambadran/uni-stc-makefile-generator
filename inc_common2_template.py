"""

"""

def generate_inc_common2():
    '''

    '''
    string = """
include $(MAKE_DIR)/1-mcu-settings.mk
-include $(DEP_FILE)
include $(MAKE_DIR)/2-mcu-rules.mk
    """
    return string
