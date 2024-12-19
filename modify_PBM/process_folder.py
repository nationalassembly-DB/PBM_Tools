"""PBM문서 내 개행문자가 발견되면 이를 제거하고 새로 저장합니다"""


import os
import re
from natsort import natsorted


def modify_file(input_path, output_path):
    """개행문자 제거후 새로 저장"""
    for root, _, files in os.walk(input_path):
        for file in natsorted(files):
            if not file.lower().endswith('.pbm'):
                continue

            input_file = os.path.join(root, file)
            output_file = os.path.join(output_path, file)

            with open(input_file, 'r', encoding='utf-8') as pbm:
                html = pbm.read()

                cleaned_html = re.sub(r'(<Level[^>]*>)([^<]+)(</Level>)', lambda m: m.group(
                    1) + m.group(2).replace('\r', '').replace('\n', ' ').strip() + m.group(3), html)

            with open(output_file, 'w', encoding='utf-8') as savepbm:
                savepbm.write(cleaned_html)
