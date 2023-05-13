def command_aes_auth(key_id: list) -> list:
    '''
    AA: Authenticate (AES)
    This allows you to authenticate for a specified key number using AES. 
    If the key is not AES you get an AE error back. The key number is the key in the current application. 
    If top level (AID 0) selected or no application selected yet then this is the master key for the card (key 0).
    '''
    apdu = [0x90, 0xAA, 0x00, 0x00]
    lc = [0x01]
    apdu += lc
    apdu += key_id
    le = [0x00]
    apdu += le
    return apdu


def command_des_auth(key_id: list) -> list:
    '''
    1A: Authenticate (3DES/ 3K3DES)
    '''
    apdu = [0x90, 0x1A, 0x00, 0x00]
    lc = [0x01]
    apdu += lc
    apdu += key_id
    le = [0x00]
    apdu += le
    return apdu


def command_legacy_auth(key_id: list) -> list:
    '''
    0A: Authenticate (Legacy DES)
    '''
    apdu = [0x90, 0x0A, 0x00, 0x00]
    lc = [0x01]
    apdu += lc
    apdu += key_id
    le = [0x00]
    apdu += le
    return apdu


def command_change_key_settings(key_id: list, encrypted_data: list) -> list:
    apdu = [0x90, 0x54, 0x00, 0x00]
    lc = [len(encrypted_data)]
    apdu += lc
    le = [0x00]
    apdu += le
    return apdu


def command_set_configuration(encrypted_data: list) -> list:
    '''
    5C 00: Set Configuration (card config)
    This sets top level card settings.
    
    NOTE: Details in RevK's manual, page 7.
    '''
    apdu = [0x90, 0x5C, 0x00, 0x00]
    lc = [0x01]
    apdu += lc
    apdu += [0x00]
    le = [0x00]
    apdu += le
    return apdu


def command_change_key(key_id: list, encrypted_data: list) -> list:
    '''
    C4: Change Key
    This allows a key to be changed.
    If setting the master key for the card level, the key no has bit 7 set to indicate AES.
    If changing a different key to the current key, the new key data is the new XOR'd with the old
    key. A CRC of the new key is included at the end of the message.
    This message format is slightly different if not using AES.
    '''
    apdu = [0x90, 0xC4, 0x00, 0x00]
    lc = [len(encrypted_data) + 1]
    apdu += lc
    apdu += key_id
    apdu += encrypted_data
    le = [0x00]
    apdu += le
    return apdu


def command_get_key_version(key_id: list) -> list:
    '''
    64: Get Key Version
    This gets the version of the key, for AES this is a version byte which can be set when setting the
    key. This allows you to then know which key to use if there have been different versions of keys in use.
    '''
    apdu = [0x90, 0x64, 0x00, 0x00]
    lc = [0x01]
    apdu += lc
    apdu += key_id
    le = [0x00]
    apdu += le
    return apdu
