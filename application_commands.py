def command_create_application(aid: list,
                               key_setting_byte: list,
                               app_setting_byte: list) -> list:
    '''
    CA: Create Application
    Create a new application. Depending on settings this may be possible without authenticating
    as the card master key. The key settings depend if you are setting the master key for AID 0 (the card level), 
    or for an application. (Refer to the table on page 7 of RevK's DESFire manual).
    '''
    apdu = apdu = [0x90, 0xCA, 0x00, 0x00]
    lc = [0x05]
    apdu += lc
    apdu += aid
    apdu += key_setting_byte
    apdu += app_setting_byte
    le = [0x00]
    apdu += le
    return apdu


def command_delete_application(aid: list) -> list:
    '''
    DA: Delete Application
    This allows an application to be deleted. The permission to allow deletion depends on settings,
    but it always requires authentication.
    '''
    apdu = [0x90, 0xDA, 0x00, 0x00]
    lc = [0x03]
    apdu += lc
    apdu += aid
    le = [0x00]
    apdu += le
    return apdu


def command_get_application_ids() -> list:
    '''
    6A: Get Application IDs
    This one byte command gets a list of application IDs, each 3 bytes.
    '''
    apdu = [0x90, 0x6A, 0x00, 0x00]
    le = [0x00]
    apdu += le
    return apdu


def command_free_memory() -> list:
    '''
    6E: Free Memory
    This gets the free memory, the response is 3 bytes (low byte first).
    '''
    apdu = [0x90, 0x6E, 0x00, 0x00]
    return apdu


def command_get_df_names() -> list:
    pass


def command_get_key_settings() -> list:
    '''
    45: Get Key Settings
    Returns the settings for the current application - the response is the settings, 
    and number of keys.
    '''
    apdu = [0x90, 0x45, 0x00, 0x00]
    le = [0x00]
    apdu += le
    return apdu


def command_select_application(aid: list) -> list:
    '''
    5A: Select Application
    Selects an application with the Application ID (AID) Privided
    '''
    apdu = [0x90, 0x5A, 0x00, 0x00]
    lc = [0x03]
    apdu += lc
    apdu += aid
    le = [0x00]
    apdu += le
    return apdu


def command_format_picc() -> list:
    '''
    FC: FormatPICC
    This formats (wipes) the card - you need to be authenticated with the card master key for this.
    Formatting does not change the key type or zap the master key in the process.

    NOTE: When you delete an application or a file, that memory isn't actually freed. In order to reclaim
    used memory, you ultimately need to reformat the PICC. Typically you'd overwrite a file as opposed to 
    nuking it, recreating it and writing to it again. But, if you need to completely wipe a card, this is 
    the APDU to use.
    '''
    apdu = [0x90, 0xFC, 0x00, 0x00]
    le = [0x00]
    apdu += le
    return apdu


def command_get_version() -> list:
    '''
    60 : Get Version
    This gets the card version details, including manufacturing info and its uid.
    '''
    apdu = [0x90, 0x60, 0x00, 0x00]
    le = [0x00]
    apdu += le
    return apdu


def command_get_card_uid() -> list:
    pass


def command_select_root_application() -> list:
    '''
    A4 Select (ISO/IEC 7816)
    Selects the root application
    '''
    apdu = [0x00, 0xA4, 0x00, 0x00]
    return apdu


def command_additional_frame(data: list = None) -> list:
    '''
    AF: Additional Frame
    This sends data pertaining to a previous command as an additional frame.
    Must be sent in a response to a status code of AF.
    '''
    apdu = [0x90, 0xAF, 0x00, 0x00]

    if data:
        lc = [len(data)]
        apdu += lc
        apdu += data

    le = [0x00]
    apdu += le
    return apdu
