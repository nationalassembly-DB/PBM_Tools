"""main"""


import os
import sys

from check_PBM.process_folder import process_folder
from create_PBM.process_folder import process_files
from modify_PBM.process_folder import modify_file


def main():
    """main"""
    print("="*60)
    print("\n>>>>>>PBM 생성 및 검토기<<<<<<\n")
    print("="*60)

    select = input("\n[1]PBM생성\n[2]PBM검토\n[3]PBM수정\n[0]종료\n-> ")

    if select == '1':
        input_path = input("\npdf 파일이 존재하는 폴더를 입력하세요\n-> ").strip()
        output_path = input("\n저장할 파일 폴더를 입력하세요\n-> ").strip()

        if not os.path.isdir(input_path):
            print("입력 폴더의 경로를 다시 한번 확인해주세요")
            return main()
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        process_files(input_path, output_path)
        print("모든 작업이 정상적으로 완료되었습니다.")
    elif select == '2':
        input_path = input("\nPBM파일이 위치한 폴더 경로를 입력해주세요\n-> ")
        output_path = input("\n엑셀 파일 경로를 입력하세요\n-> ")

        process_folder(input_path, output_path)
    elif select == '3':
        input_path = input("\nPBM파일이 위치한 폴더 경로를 입력해주세요\n-> ")
        output_path = input("\n새로운 PBM을 저장할 폴더 경로를 입력하세요\n-> ")
        modify_file(input_path, output_path)
    elif select == '0':
        sys.exit()
    else:
        print("올바른 숫자를 입력하세요")
        return main()

    return main()


if __name__ == "__main__":
    main()
