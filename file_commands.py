def command_get_file_ids() -> list:
    '''
    6F: Get File IDs
    This gets a list of file IDs in the selected application.
    '''
    apdu = [0x90, 0x6F, 0x00, 0x00]
    le = [0x00]
    apdu += le
    return apdu


def get_iso_file_ids() -> list:
    '''
    61: Get File IDs
    This gets a list of ISO file IDs in the selected application.
    '''
    apdu = [0x90, 0x61, 0x00, 0x00]
    le = [0x00]
    apdu += le
    return apdu


def command_get_file_settings(fileno: list) -> list:
    '''
    F5: Get File Settings
    This gets the file settings for a specific file in the application. These are the settings used when
    creating the file. The response depends on the file type. 

    NOTE: Details in RevK's manual, page 11.
    '''
    apdu = [0x90, 0xF5, 0x00, 0x00]
    lc = [0x01]
    apdu += lc
    apdu += fileno
    le = [0x00]
    apdu += le
    return apdu


def command_change_file_settings(fileno: list, encrypted_data: list) -> list:
    '''
    5F: Change File Settings
    This allows file settings to be changed for a specific file in the application.
    '''
    apdu = [0x90, 0x5F, 0x00, 0x00]
    lc = [len(encrypted_data) + 1]
    apdu += lc
    apdu += fileno
    le = [0x00]
    apdu += le
    return apdu


def command_create_std_data_file(fileno: list,
                                 comms_setting_byte: list,
                                 access_rights: list,
                                 file_size: list) -> list:
    '''
    CD: Create StdDataFile
    Create a standard data file.
    '''
    apdu = [0x90, 0xCD, 0x00, 0x00]
    lc = [0x07]
    apdu += lc
    apdu += fileno
    apdu += comms_setting_byte
    apdu += access_rights
    apdu += file_size
    le = [0x00]
    apdu += le
    return apdu


def command_create_backup_data_file() -> list:
    pass


def command_create_value_file(fileno: list,
                              comms_setting_byte: list,
                              access_rights: list,
                              lower_limit: list,
                              upper_limit: list,
                              initial_value: list,
                              limited_credit_available: list) -> list:
    '''
    CC: Create Value File
    Create a value data file.
    '''
    apdu = [0x90, 0xCC, 0x00, 0x00]
    lc = [0x11]
    apdu += lc
    apdu += fileno
    apdu += comms_setting_byte
    apdu += access_rights
    apdu += lower_limit
    apdu += upper_limit
    apdu += initial_value
    apdu += limited_credit_available
    le = [0x00]
    apdu += le
    return apdu


def command_create_linear_record_file() -> list:
    pass


def command_create_cyclic_record_file(fileno: list,
                                      comms_setting_byte: list,
                                      access_rights: list,
                                      record_size: list,
                                      number_of_records: list) -> list:
    '''
    C0: Create Cyclic Record File
    Create a cyclic record file. The number of records you can have is actually one less as the spare
    record is the one that is partly written before a commit.
    '''
    apdu = [0x90, 0xC0, 0x00, 0x00]
    lc = [0x0A]
    apdu += lc
    apdu += fileno
    apdu += comms_setting_byte
    apdu += access_rights
    apdu += record_size
    apdu += number_of_records
    le = [0x00]
    apdu += le
    return apdu


def command_delete_file(fileno: list) -> list:
    '''
    DF: Delete File
    Delete a file.
    '''
    apdu = [0x90, 0xDF, 0x00, 0x00]
    lc = [0x01]
    apdu += lc
    apdu += fileno
    le = [0x00]
    apdu += le
    return apdu
