#!/usr/bin/python3

import os
import os.path
import time
import csv

from logger import info_logger, warning_logger, error_logger
import config.new_string as NEW
import config.old_string as OLD
import config.start_path as START
import config.list_path as LIST

# Global variables
_start_time = 'TIME'

_old_string = OLD.string
_new_string = NEW.string

_target_list_path = LIST.target

def main():
    target_list = load_csv()
    num_target = len(target_list)

    target_count = 0
    warning_count = 0
    for target in target_list:
        target_count += 1
        Found = False
        for root, _, files in os.walk(START.dir_name):
            if target in files:
                Found = True
                target_path = os.path.join(root, target)
                info_logger.info(f"filename: '{target_path}'")
                try:
                    # Read the file content
                    with open(target_path, 'r', encoding="utf-8-sig") as file:
                        file_content = file.read()
                        result = file_content.find(_old_string)
                        if result != -1:
                            #Replace the string
                            modified_content = file_content.replace(_old_string, _new_string)
                            # Write the file content
                            with open(target_path, 'w', encoding="utf-8-sig") as file:
                                file.write(modified_content)
                            info_logger.info(f"[PASSED] Successfully replaced '{_old_string}' with '{_new_string}' in '{target}'.")
                        else:
                            warning_count += 1
                            info_logger.info(f"[FAILED] The '{_old_string}' is not in the file '{target};'")
                            warning_logger.warning(f"{warning_count}. The '{_old_string}' is not in the file '{target}'")

                except FileNotFoundError:
                    info_logger.info(f"Error: The file '{target}' was not found.")
                    error_logger.error(f"Error: The file '{target}' was not found.")
                except PermissionError:
                    info_logger.info("Error: Permission denied to access '{target}'.")
                    error_logger.error("Error: Permission denied to access '{target}'.")
                except Exception as e:
                    info_logger.info(f"An error occurred: {e}")
                    error_logger.error(f"An error occurred: {e}")
        if not Found:
            warning_count += 1
            info_logger.info(f"[FAILED] The '{target}' is not in the '{START.dir_name}'")
            warning_logger.warning(f"{warning_count}. The '{target}' is not in the '{START.dir_name}'")                

        motion = {0:'-', 1:'\\', 2:'|', 3:'/'}

        if not (target_count == num_target):
            print(f'{motion[target_count % 4]} Processing.. [{target_count}/{num_target}] ', end = '\r')
        else:
            print(f'Processing Completed. [{target_count}/{num_target}]')
            if(warning_count > 49):
                print(f'\'Warning\' count is {warning_count}, Please check \'WARNING.log\' and \'config\' again.')

def load_csv():
    data = []

    try:
        with open(f'{_target_list_path}', 'r', newline='', encoding="utf-8-sig") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:
                    data.append(row[0])
                else:
                    continue

    except FileNotFoundError:
        info_logger.info(f"Error: The file '{_target_list_path}' was not found.")
        error_logger.error(f"Error: The file '{_target_list_path}' was not found.")
    except Exception as e:
        info_logger.info(f"An error occurred: {e}")
        error_logger.error(f"An error occurred: {e}")

    return data

# Init
if __name__ == '__main__':

    _start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    print(f'<< [{_start_time}] Start >>')
    info_logger.info(f'<< [{_start_time}] Start >>')
    
    main()