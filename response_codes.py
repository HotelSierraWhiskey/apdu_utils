apdu_response_codes = {
    (0x62, 0x00): "62 00: No information given (NV-Ram not changed)",
    (0x62, 0x01): "62 01: NV-Ram not changed 1.",
    (0x62, 0x81): "62 81: Part of returned data may be corrupted",
    (0x62, 0x82): "62 82: End of file/record reached before reading Le bytes",
    (0x62, 0x83): "62 83: Selected file invalidated",
    (0x62, 0x84): "62 84: Selected file is not valid. FCI not formated according to ISO",
    (0x62, 0x85): "62 85: No input data available from a sensor on the card. No Purse Engine enslaved for R3bc",
    (0x62, 0xA2): "62 A2: Wrong R-MAC",
    (0x62, 0xA4): "62 A4: Card locked (during reset( ))",
    (0x62, 0xF1): "62 F1: Wrong C-MAC",
    (0x62, 0xF3): "62 F3: Internal reset",
    (0x62, 0xF5): "62 F5: Default agent locked",
    (0x62, 0xF7): "62 F7: Cardholder locked",
    (0x62, 0xF8): "62 F8: Basement is current agent",
    (0x62, 0xF9): "62 F9: CALC Key Set not unblocked",
    (0x63, 0x00): "63 00: No information given (NV-Ram changed)",
    (0x63, 0x81): "63 81: File filled up by the last write. Loading/updating is not allowed.",
    (0x63, 0x82): "63 82: Card key not supported.",
    (0x63, 0x83): "63 83: Reader key not supported.",
    (0x63, 0x84): "63 84: Plaintext transmission not supported.",
    (0x63, 0x85): "63 85: Secured transmission not supported.",
    (0x63, 0x86): "63 86: Volatile memory is not available.",
    (0x63, 0x87): "63 87: Non-volatile memory is not available.",
    (0x63, 0x88): "63 88: Key number not valid.",
    (0x63, 0x89): "63 89: Key length is not correct.",
    (0x63, 0xC0): "63 C0: Verify fail, no try left.",
    (0x63, 0xC1): "63 C1: Verify fail, 1 try left.",
    (0x63, 0xC2): "63 C2: Verify fail, 2 tries left.",
    (0x63, 0xC3): "63 C3: Verify fail, 3 tries left.",
    (0x63, 0xF1): "63 F1: More data expected.",
    (0x63, 0xF2): "63 F2: More data expected and proactive command pending.",
    (0x64, 0x00): "64 00: No information given (NV-Ram not changed)",
    (0x64, 0x01): "64 01: Command timeout. Immediate response required by the card.",
    (0x65, 0x00): "65 00: No information given",
    (0x65, 0x01): "65 01: Write error. Memory failure. There have been problems in writing or reading the EEPROM. Other hardware problems may also bring this error.",
    (0x65, 0x81): "65 81: Memory failure",
    (0x66, 0x00): "66 00: Error while receiving (timeout)",
    (0x66, 0x01): "66 01: Error while receiving (character parity error)",
    (0x66, 0x02): "66 02: Wrong checksum",
    (0x66, 0x03): "66 03: The current DF file without FCI",
    (0x66, 0x04): "66 04: No SF or KF under the current DF",
    (0x66, 0x69): "66 69: Incorrect Encryption/Decryption Padding",
    (0x67, 0x00): "67 00: Wrong length",
    (0x68, 0x00): "68 00: No information given (The request function is not supported by the card)",
    (0x68, 0x81): "68 81: Logical channel not supported",
    (0x68, 0x82): "68 82: Secure messaging not supported",
    (0x68, 0x83): "68 83: Last command of the chain expected",
    (0x68, 0x84): "68 84: Command chaining not supported",
    (0x69, 0x00): "69 00: No information given (Command not allowed)",
    (0x69, 0x01): "69 01: Command not accepted (inactive state)",
    (0x69, 0x81): "69 81: Command incompatible with file structure",
    (0x69, 0x82): "69 82: Security condition not satisfied.",
    (0x69, 0x83): "69 83: Authentication method blocked",
    (0x69, 0x84): "69 84: Referenced data reversibly blocked (invalidated)",
    (0x69, 0x85): "69 85: Conditions of use not satisfied.",
    (0x69, 0x86): "69 86: Command not allowed (no current EF)",
    (0x69, 0x87): "69 87: Expected secure messaging (SM) object missing",
    (0x69, 0x88): "69 88: Incorrect secure messaging (SM) data object",
    (0x69, 0x8D): "69 8D: Reserved",
    (0x69, 0x96): "69 96: Data must be updated again",
    (0x69, 0xE1): "69 E1: POL1 of the currently Enabled Profile prevents this action.",
    (0x69, 0xF0): "69 F0: Permission Denied",
    (0x69, 0xF1): "69 F1: Permission Denied - Missing Privilege",
    (0x6A, 0x00): "6A 00: No information given (Bytes P1 and/or P2 are incorrect)",
    (0x6A, 0x80): "6A 80: The parameters in the data field are incorrect.",
    (0x6A, 0x81): "6A 81: Function not supported",
    (0x6A, 0x82): "6A 82: File not found",
    (0x6A, 0x83): "6A 83: Record not found",
    (0x6A, 0x84): "6A 84: There is insufficient memory space in record or file",
    (0x6A, 0x85): "6A 85: Lc inconsistent with TLV structure",
    (0x6A, 0x86): "6A 86: Incorrect P1 or P2 parameter.",
    (0x6A, 0x87): "6A 87: Lc inconsistent with P1-P2",
    (0x6A, 0x88): "6A 88: Referenced data not found",
    (0x6A, 0x89): "6A 89: File already exists",
    (0x6A, 0x8A): "6A 8A: DF name already exists.",
    (0x6A, 0xF0): "6A F0: Wrong parameter value",
    (0x6B, 0x00): "6B 00: Wrong parameter(s) P1-P2",
    (0x6C, 0x00): "6C 00: Incorrect P3 length.",
    (0x6D, 0x00): "6D 00: Instruction code not supported or invalid",
    (0x6E, 0x00): "6E 00: Class not supported",
    (0x6F, 0x00): "6F 00: Command aborted - more exact diagnosis not possible (e.g., operating system error).",
    (0x6F, 0xFF): "6F FF: Card dead (overuse, …)",
    (0x90, 0x00): "90 00: Command successfully executed (OK).",
    (0x90, 0x04): "90 04: PIN not succesfully verified, 3 or more PIN tries left",
    (0x90, 0x08): "90 08: Key/file not found",
    (0x90, 0x80): "90 80: Unblock Try Counter has reached zero",
    (0x91, 0x00): "91 00: OK",
    (0x91, 0x01): "91 01: States.activity, States.lock Status or States.lockable has wrong value",
    (0x91, 0x02): "91 02: Transaction number reached its limit",
    (0x91, 0x0C): "91 0C: No changes",
    (0x91, 0x0E): "91 0E: Insufficient NV-Memory to complete command",
    (0x91, 0x1C): "91 1C: Command code not supported",
    (0x91, 0x1E): "91 1E: CRC or MAC does not match data",
    (0x91, 0x40): "91 40: Invalid key number specified",
    (0x91, 0x7E): "91 7E: Length of command string invalid",
    (0x91, 0x9D): "91 9D: Not allow the requested command",
    (0x91, 0x9E): "91 9E: Value of the parameter invalid",
    (0x91, 0xA0): "91 A0: Requested AID not present on PICC",
    (0x91, 0xA1): "91 A1: Unrecoverable error within application",
    (0x91, 0xAE): "91 AE: Authentication status does not allow the requested command",
    (0x91, 0xAF): "91 AF: Additional data frame is expected to be sent",
    (0x91, 0xBE): "91 BE: Out of boundary",
    (0x91, 0xC1): "91 C1: Unrecoverable error within PICC",
    (0x91, 0xCA): "91 CA: Previous Command was not fully completed",
    (0x91, 0xCD): "91 CD: PICC was disabled by an unrecoverable error",
    (0x91, 0xCE): "91 CE: Number of Applications limited to 28",
    (0x91, 0xDE): "91 DE: File or application already exists",
    (0x91, 0xEE): "91 EE: Could not complete NV-write operation due to loss of power",
    (0x91, 0xF0): "91 F0: Specified file number does not exist",
    (0x91, 0xF1): "91 F1: Unrecoverable error within file",
    (0x92, 0x10): "92 10: Insufficient memory. No more storage available.",
    (0x92, 0x40): "92 40: Writing to EEPROM not successful.",
    (0x93, 0x01): "93 01: Integrity error",
    (0x93, 0x02): "93 02: Candidate S2 invalid",
    (0x93, 0x03): "93 03: Application is permanently locked",
    (0x94, 0x00): "94 00: No EF selected.",
    (0x94, 0x01): "94 01: Candidate currency code does not match purse currency",
    (0x94, 0x02): "94 02: Candidate amount too high",
    (0x94, 0x02): "94 02: Address range exceeded.",
    (0x94, 0x03): "94 03: Candidate amount too low",
    (0x94, 0x04): "94 04: FID not found, record not found or comparison pattern not found.",
    (0x94, 0x05): "94 05: Problems in the data field",
    (0x94, 0x06): "94 06: Required MAC unavailable",
    (0x94, 0x07): "94 07: Bad currency : purse engine has no slot with R3bc currency",
    (0x94, 0x08): "94 08: R3bc currency not supported in purse engine",
    (0x94, 0x08): "94 08: Selected file type does not match command.",
    (0x95, 0x80): "95 80: Bad sequence",
    (0x96, 0x81): "96 81: Slave not found",
    (0x97, 0x00): "97 00: PIN blocked and Unblock Try Counter is 1 or 2",
    (0x97, 0x02): "97 02: Main keys are blocked",
    (0x97, 0x04): "97 04: PIN not succesfully verified, 3 or more PIN tries left",
    (0x97, 0x84): "97 84: Base key",
    (0x97, 0x85): "97 85: Limit exceeded - C-MAC key",
    (0x97, 0x86): "97 86: SM error - Limit exceeded - R-MAC key",
    (0x97, 0x87): "97 87: Limit exceeded - sequence counter",
    (0x97, 0x88): "97 88: Limit exceeded - R-MAC length",
    (0x97, 0x89): "97 89: Service not available",
    (0x98, 0x02): "98 02: No PIN defined.",
    (0x98, 0x04): "98 04: Access conditions not satisfied, authentication failed.",
    (0x98, 0x35): "98 35: ASK RANDOM or GIVE RANDOM not executed.",
    (0x98, 0x40): "98 40: PIN verification not successful.",
    (0x98, 0x50): "98 50: INCREASE or DECREASE could not be executed because a limit has been reached.",
    (0x98, 0x62): "98 62: Authentication Error, application specific (incorrect MAC)",
    (0x99, 0x00): "99 00: 1 PIN try left",
    (0x99, 0x04): "99 04: PIN not succesfully verified, 1 PIN try left",
    (0x99, 0x85): "99 85: Wrong status - Cardholder lock",
    (0x99, 0x86): "99 86: Missing privilege",
    (0x99, 0x87): "99 87: PIN is not installed",
    (0x99, 0x88): "99 88: Wrong status - R-MAC state",
    (0x9A, 0x00): "9A 00: 2 PIN try left",
    (0x9A, 0x04): "9A 04: PIN not succesfully verified, 2 PIN try left",
    (0x9A, 0x71): "9A 71: Wrong parameter value - Double agent AID",
    (0x9A, 0x72): "9A 72: Wrong parameter value - Double agent Type",
    (0x9D, 0x05): "9D 05: Incorrect certificate type",
    (0x9D, 0x07): "9D 07: Incorrect session data size",
    (0x9D, 0x08): "9D 08: Incorrect DIR file record size",
    (0x9D, 0x09): "9D 09: Incorrect FCI record size",
    (0x9D, 0x0A): "9D 0A: Incorrect code size",
    (0x9D, 0x10): "9D 10: Insufficient memory to load application",
    (0x9D, 0x11): "9D 11: Invalid AID",
    (0x9D, 0x12): "9D 12: Duplicate AID",
    (0x9D, 0x13): "9D 13: Application previously loaded",
    (0x9D, 0x14): "9D 14: Application history list full",
    (0x9D, 0x15): "9D 15: Application not open",
    (0x9D, 0x17): "9D 17: Invalid offset",
    (0x9D, 0x18): "9D 18: Application already loaded",
    (0x9D, 0x19): "9D 19: Invalid certificate",
    (0x9D, 0x1A): "9D 1A: Invalid signature",
    (0x9D, 0x1B): "9D 1B: Invalid KTU",
    (0x9D, 0x1D): "9D 1D: MSM controls not set",
    (0x9D, 0x1E): "9D 1E: Application signature does not exist",
    (0x9D, 0x1F): "9D 1F: KTU does not exist",
    (0x9D, 0x20): "9D 20: Application not loaded",
    (0x9D, 0x21): "9D 21: Invalid Open command data length",
    (0x9D, 0x30): "9D 30: Check data parameter is incorrect (invalid start address)",
    (0x9D, 0x31): "9D 31: Check data parameter is incorrect (invalid length)",
    (0x9D, 0x32): "9D 32: Check data parameter is incorrect (illegal memory check area)",
    (0x9D, 0x40): "9D 40: Invalid MSM Controls ciphertext",
    (0x9D, 0x41): "9D 41: MSM controls already set",
    (0x9D, 0x42): "9D 42: Set MSM Controls data length less than 2 bytes",
    (0x9D, 0x43): "9D 43: Invalid MSM Controls data length",
    (0x9D, 0x44): "9D 44: Excess MSM Controls ciphertext",
    (0x9D, 0x45): "9D 45: Verification of MSM Controls data failed",
    (0x9D, 0x50): "9D 50: Invalid MCD Issuer production ID",
    (0x9D, 0x51): "9D 51: Invalid MCD Issuer ID",
    (0x9D, 0x52): "9D 52: Invalid set MSM controls data date",
    (0x9D, 0x53): "9D 53: Invalid MCD number",
    (0x9D, 0x54): "9D 54: Reserved field error",
    (0x9D, 0x55): "9D 55: Reserved field error",
    (0x9D, 0x56): "9D 56: Reserved field error",
    (0x9D, 0x57): "9D 57: Reserved field error",
    (0x9D, 0x60): "9D 60: MAC verification failed",
    (0x9D, 0x61): "9D 61: Maximum number of unblocks reached",
    (0x9D, 0x62): "9D 62: Card was not blocked",
    (0x9D, 0x63): "9D 63: Crypto functions not available",
    (0x9D, 0x64): "9D 64: No application loaded",
    (0x9E, 0x00): "9E 00: PIN not installed",
    (0x9E, 0x04): "9E 04: PIN not succesfully verified, PIN not installed",
    (0x9F, 0x00): "9F 00: PIN blocked and Unblock Try Counter is 3",
    (0x9F, 0x04): "9F 04: PIN not succesfully verified, PIN blocked and Unblock Try Counter is 3",
}


####################################################################################################
#                                                                                                  #
#   NOTE:   Variable Length APDU Responses, some of which are ISO 7816.                            #
#           Left here for reference.                                                               #
#                                                                                                  #
####################################################################################################

# 6			        Class not supported.
# 61	—		    Response bytes still available
# [0x61, 0xXX]		Command successfully executed; ‘XX’ bytes of data are available and can be requested using GET RESPONSE.
# [0x62, 0x—]	    State of non-volatile memory unchanged
# [0x62, 0xCX]		Counter with value x (command dependent)
# [0x62, 0xFX]		-
# [0x62, 0xXX]		RFU
# [0x63, 0x—]	    State of non-volatile memory changed
# [0x63, 0xCX]		The counter has reached the value ‘x’ (0 = x = 15) (command dependent).
# [0x63, 0xFX]		-
# [0x63, 0xXX]		RFU
# [0x64, 0x—]	    State of non-volatile memory unchanged
# [0x64, 0xXX]		RFU
# [0x65, 0x—]	    State of non-volatile memory changed
# [0x65, 0xFX]		-
# [0x65, 0xXX]		RFU
# [0x66, 0x—]
# [0x66, 0xXX]		-
# [0x67, 0x—]
# [0x67, 0xXX]		length incorrect (procedure)(ISO 7816-3)
# [0x68, 0x—]	    Functions in CLA not supported
# [0x68, 0xFX]		-
# [0x68, 0xXX]		RFU
# [0x69, 0x—]	    Command not allowed
# [0x69, 0xFX]		-
# [0x69, 0xXX]		RFU
# [0x6A, 0x—]	    Wrong parameter(s) P1-P2
# [0x6A, 0xFX]		-
# [0x6A, 0xXX]		RFU
# [0x6B, 0x—]
# [0x6B, 0xXX]		"Reference incorrect (procedure byte), (ISO 7816-3)"
# [0x6C, 0x—]	    Wrong length Le
# [0x6C, 0xXX]		"Bad length value in Le; ‘xx’ is the correct exact Le"
# [0x6D, 0xXX]		"Instruction code not programmed or invalid (procedure byte), (ISO 7816-3)"
# [0x6E, 0xXX]		"Instruction class not supported (procedure byte), (ISO 7816-3)"
# [0x6F, 0x—]	    Internal exception
# [0x6F, 0xXX]		No precise diagnosis (procedure byte), (ISO 7816-3)
# [0x9-, 0x—]
# [0x92, 0x0x]		"Writing to EEPROM successful after ‘x’ attempts."
# [0x9F, 0xXX]		"Command successfully executed; ‘xx’ bytes of data are available and can be requested using GET RESPONSE."
# [0x9x, 0xXX]		"Application related status, (ISO 7816-3)"
