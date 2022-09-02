from src_acs import nfc

reader = nfc.Reader()
reader.print_data(reader.get_uid())
reader.info()
