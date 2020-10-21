

__author__ = "ariannagbasha and got Pete's help and got Tracy's help as well"


import sys
import signal
import time
import argparse
import os
import logging
# Level(#'val)           When it’s used
# DEBUG(10)          Detailed information, typically of interest only when
#                    diagnosing problems.
# INFO(20)           Confirmation that things are working as expected.
# WARNING(30)        An indication that something unexpected happened, or
#                    indicative of some problem in the near future
#                    (e.g. ‘disk space low’).
#                    The software is still working as expected.
# ERROR(40)          Due to a more serious problem, the software has not been
#                    able to perform some function.
# CRITICAL(50)       A serious error, indicating that the program itself may be 
#                    unable to continue running.


exit_flag = False
global_dict = {}
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('file.log')
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def search_for_magic(filename, start_line, magic_string):
    """ Searches for magic string by opening the file, iterating through the file
    And looking for the magic string with the special nature of find"""
    with open(filename) as f:
        for line_num, line_string in enumerate(f):
            if line_string.find(magic_string) != -1:
                print(filename, line_num + 1)


def scan_single_file(dirname):
    """"""


def detect_added_files(dirname):
    """This will"""
    pass


def detect_removed_files(dirname):
    """"""
    pass



def watch_directory(path, magic_string, extension, interval):
    """ """
    file_ls = os.listdir(path)
    for file_name in file_ls:
        search_for_magic(path + '/' + file_name, 0, magic_string)


def create_parser():
    """ """
    parser = argparse.ArgumentParser(
        description="Looking for changing files in directory.")
    parser.add_argument('directory', help='directory to watch')
    parser.add_argument('txt', help="find magic")
    parser.add_argument(
        '-e', '--ext', default='.txt', help='extension input')
    parser.add_argument(
        '-i', '--int', default=1.0, type=int, help='polling interval period of time\
                        between the end of the timeout period')
    return parser


def signal_handler(sig_num, frame):
    """
    This is a handler for SIGTERM and SIGINT. Other signals can be mapped here as well (SIGHUP?)
    Basically, it just sets a global flag, and main() will exit its loop if the signal is trapped.
    :param sig_num: The integer signal number that was trapped from the OS.
    :param frame: Not used
    :return None
    """
    # log the associated signal name
    global exit_flag
    logger.warning('Received ' + signal.Signals(sig_num).name)
    exit_flag = True
    return None


def main(args):
    parser = create_parser()
    ns = parser.parse_args(args)
    # Hook into these two signals from the OS
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Now my signal_handler will get called if OS sends
    # either of these to my process.
    while not exit_flag:
        try:
            # call my directory watching function
            watch_directory(ns.directory, ns.txt, ns.ext, ns.int)
            time.sleep(ns.int)
            pass
        except Exception as e:
            print(e)
            # This is an UNHANDLED exception
            # Log an ERROR level message here
            pass
        # put a sleep inside my while loop so I don't peg the cpu usage at 100%
        # time.sleep(args.int)
    # final exit point happens here
    # Log a message that we are shutting down
    # Include the overall uptime since program start


if __name__ == '__main__':
    main(sys.argv[1:])