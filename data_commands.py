def command_read_data(fileno: list, offset: list, length: list) -> list:
    """
    BD: Read Data
    Read data from a file.
    The response will have MAC or be encrypted depending on file comms mode.

    NOTE: This function expects the byte order for both `length` and `offset` to be reversed.
    """
    apdu = [0x90, 0xBD, 0x00, 0x00]
    lc = [0x07]
    apdu += lc
    apdu += fileno
    apdu += offset
    apdu += length
    le = [0x00]
    apdu += le
    return apdu


def command_write_data(fileno: list, offset: list, length: list, data: list) -> list:
    """
    3D: Write Data
    Write data to a file.
    This needs to be sent using plain, CMAC or encrypted (with CRC) depending on file comms
    mode.

    NOTE: Details in RevK's manual, page 14.
    NOTE: currently this command only supports writing plain data.
    NOTE: This function expects the byte order for both `length` and `offset` to be reversed.
    """
    apdu = [0x90, 0x3D, 0x00, 0x00]
    lc = [len(fileno) + len(offset) + len(length) + len(data)]
    apdu += lc
    apdu += fileno
    apdu += offset
    apdu += length
    apdu += data
    le = [0x00]
    apdu += le
    return apdu


def command_get_value(fileno: list) -> list:
    """
    6C: Get Value
    Get value from a value file.
    """
    apdu = [0x90, 0x6C, 0x00, 0x00]
    lc = [0x01]
    apdu += lc
    apdu += fileno
    le = [0x00]
    apdu += le
    return apdu


def command_credit(fileno: list, amount: list) -> list:
    """
    OC: Credit
    Credit value in a value file. You need to commit the changes.
    amount is 4 bytes
    """
    apdu = [0x90, 0x0C, 0x00, 0x00]
    lc = [0x05]
    apdu += lc
    apdu += fileno
    apdu += amount
    le = [0x00]
    apdu += le
    return apdu


def command_debit(fileno: list, amount: list) -> list:
    """
    DC: Debit
    Debit the value in a file. You need to commit the changes.
    amount is 4 bytes
    """
    apdu = [0x90, 0xDC, 0x00, 0x00]
    lc = [0x05]
    apdu += lc
    apdu += fileno
    apdu += amount
    le = [0x00]
    apdu += le
    return apdu


def command_limited_credit() -> list:
    pass


def command_write_record(fileno: list, offset: list, length: list, data: list) -> list:
    """
    3B: Write Record
    Write to a record. The offset/length are within the record.
    A new record is created with 00 bytes where not written.
    You need to commit the changes.

    NOTE: This version of the command does not support data encryption
    """
    apdu = [0x90, 0x3B, 0x00, 0x00]
    lc = [len(fileno) + len(offset) + len(length) + len(data)]
    apdu += lc
    apdu += fileno
    apdu += offset
    apdu += length
    apdu += data
    le = [0x00]
    apdu += le
    return apdu


def command_read_record(
    fileno: list, record_number: list, number_of_records: list
) -> list:
    """
    BB: Read Records
    Read records - record 0 is the oldest/first.
    """
    apdu = [0x90, 0xBB, 0x00, 0x00]
    lc = [0x07]
    apdu += lc
    apdu += fileno
    apdu += record_number
    apdu += number_of_records
    le = [0x00]
    apdu += le
    return apdu


def command_clear_record_file(fileno: list) -> list:
    apdu = [0x90, 0xEB, 0x00, 0x00]
    lc = [0x01]
    apdu += lc
    apdu += fileno
    le = [0x00]
    apdu += le
    return apdu


def command_commit_transaction() -> list:
    """
    C7: Commit Transaction
    Commit updates to value and record files.
    """
    apdu = [0x90, 0xC7, 0x00, 0x00]
    le = [0x00]
    apdu += le
    return apdu


def command_abort_transaction() -> list:
    pass
