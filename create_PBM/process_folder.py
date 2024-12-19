"""PBM 파일을 생성합니다"""


import os
import fitz


def extract_bookmarks(pdf_path):
    """Bookmark Dictionary를 반환"""
    doc = fitz.open(pdf_path)
    toc = doc.get_toc(simple=False)
    return toc


def convert_to_html(bookmarks):
    """PBM 생성"""
    html_content = '<HTML><HEAD>\n<META NAME="PBM Ver 1.0", CONTENT="Bookmark exported by muhayu">\n</HEAD>\n'  # pylint: disable=C0301

    for item in bookmarks:
        level, title, page, _ = item
        blank = "\t"*(level-1)
        str_title = str(title).replace("\n", " ").replace("\r", "")
        html_content += f'{blank}<Level ID="{
            level}", Page="{page}">{str_title}</Level>\n'
    html_content += '</HTML>'
    return html_content


def save_pbm(html_content, output_path):
    """PBM 저장"""
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(html_content)


def process_files(src_dir, dst_dir):
    """PBM 저장을 위한 폴더 순회"""
    try:
        for root, _, files in os.walk(src_dir):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, src_dir)
                new_file_path = os.path.join(dst_dir, relative_path)

                os.makedirs(os.path.dirname(new_file_path), exist_ok=True)

                if file.lower().endswith('.pdf'):
                    pdf_file_path = new_file_path.rsplit('.', 1)[0] + '.PBM'
                    save_pbm(convert_to_html(
                        extract_bookmarks(file_path)), pdf_file_path)
                else:
                    continue
    except Exception:  # pylint: disable=W0718
        log_missing_file(file, dst_dir)


def log_missing_file(file_name, output_path):
    """Exception 처리"""
    log_file_path = os.path.join(output_path, 'log.txt')
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        log_file.write('[PBM 변환 실패] ' + file_name + '\n')
