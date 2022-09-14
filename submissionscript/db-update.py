import argparse
from src.databaseoperations.connect import DatabaseConnect
from src.db_updates.execute_db_update import DbUpdateEngine
from src.fileoperations.directorycheck import DirectoryCheck


def main():
    args = argument_parser()
    directory = DirectoryCheck(args.db_scripts_folder)
    if not directory.check_if_exists():
        print('Specified directory doesn''t exist')
    try:
        db_conn = DatabaseConnect(args.db_host, args.db_user, args.db_password, args.db_name)
        file_executor = DbUpdateEngine(args.db_scripts_folder + '/seed_data', args.db_scripts_folder, db_conn)
        file_executor.execute_seed_data()
        file_executor.execute_scripts_data()
    except StopIteration:
        return


def argument_parser():
    parser = argparse.ArgumentParser(description='DB Update')
    parser.add_argument('db_scripts_folder', type=str, help='DB Scripts folder path')
    parser.add_argument('db_user', type=str, help='DB User')
    parser.add_argument('db_host', type=str, help='DB host')
    parser.add_argument('db_name', type=str, help='DB Name')
    parser.add_argument('db_password', type=str, help='DB Password')
    return parser.parse_args()


if __name__ == '__main__':
    main()
