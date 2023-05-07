import os
import shutil
import re
import zipfile

EXTENSIONS = {
    'images': ('JPEG', 'PNG', 'JPG', 'SVG'),
    'videos': ('AVI', 'MP4', 'MOV', 'MKV'),
    'documents': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
    'audio': ('MP3', 'OGG', 'WAV', 'AMR'),
    'archives': ('ZIP', 'GZ', 'TAR', 'RAR', '7z'),
}


def process_directory(directory, extensions):
    """Обробляє директорію та повертає словник зі списками файлів за типами"""
    # Створюємо пустий словник для зберігання файлів за типами
    files_by_type = {}

    # Обходимо всі файли в директорії
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Якщо файл є директорією, то рекурсивно оброблюємо його
        if os.path.isdir(file_path):
            sub_files_by_type = process_directory(file_path, extensions)
            # Додаємо файли з вкладеної директорії до загального словника
            for group_name, file_list in sub_files_by_type.items():
                if group_name not in files_by_type:
                    files_by_type[group_name] = []
                files_by_type[group_name].extend(file_list)
    # Якщо файл не є директорією, то додаємо його до словника за типами
    else:
        # Отримуємо розширення файлу
        _, file_ext = os.path.splitext(file_name)
        # Якщо розширення є в списку дозволених, то додаємо файл до словника
        if file_ext.lower() in extensions:
            group_name = get_group_name(file_ext)
            if group_name not in files_by_type:
                files_by_type[group_name] = []
            files_by_type[group_name].append(file_path)

    return files_by_type
