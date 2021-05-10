#!/usr/bin/env python3

import analyzemft

if __name__ == "__main__":
    session = analyzemft.mftsession.MftSession()
    session.mft_options()
    session.open_files()
    session.process_mft_file()
