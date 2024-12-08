import os
import platform

class OsManager:

    def __init__(self):
        self.__sorted_files_path = None
        self.__unsorted_files_path = None
        self.__filenames = None
        self.__extension_folders = None


    @staticmethod
    def print_os_name():
        print(platform.system())

    @staticmethod
    def return_dir():
        print(os.getcwd())


    def __move_files_to_unsorted(self):
        self.__unsorted_files_path = os.path.join(os.getcwd(), 'unsorted files')

        if not os.path.exists(self.__unsorted_files_path):
            os.mkdir(self.__unsorted_files_path)

        current_directory_files = os.listdir(os.getcwd())

        for item in current_directory_files:
            item_path = os.path.join(os.getcwd(), item)

            if os.path.isfile(item_path):
                destination = os.path.join(self.__unsorted_files_path, item)
                os.replace(item_path, destination)

    def sort_by_extension(self):
        self.__move_files_to_unsorted()
        self.__unsorted_files_path = os.path.join(os.getcwd(), 'unsorted files')
        self.__sorted_files_path = os.path.join(os.getcwd(), 'sorted files')
        if not os.path.exists(self.__sorted_files_path):
            os.mkdir(self.__sorted_files_path)
        self.__filenames = os.listdir(self.__unsorted_files_path)
        self.__extension_folders = {}
        for filename in self.__filenames:
            file_extension = os.path.splitext(filename)[1][1:]
            destination_path = os.path.join(self.__sorted_files_path, file_extension)

            if file_extension not in self.__extension_folders:
                self.__extension_folders[file_extension] = []
                if not os.path.exists(destination_path):
                    os.mkdir(destination_path)

            self.__extension_folders[file_extension].append(filename)

            os.replace(
                os.path.join(self.__unsorted_files_path, filename),
                os.path.join(destination_path, filename)
            )

            if self.__filenames.index(filename) == 0:
                os.replace(
                    os.path.join(destination_path, filename),
                    os.path.join(destination_path, f'some_{filename}')
                )
                print(f'{filename} was renamed into some_{filename}')

        for extension, files in self.__extension_folders.items():
            total_size = sum(
                os.path.getsize(os.path.join(self.__sorted_files_path, extension, f))
                for f in files
            )
            size_in_mb = total_size / (1024 * 1024)  # Конвертируем байты в мегабайты
            print(
                f"В папку '{extension}' было перемещено {len(files)} файлов объемом {size_in_mb:.2f} MB"
            )


OsManager.print_os_name()
OsManager.return_dir()
osmanager = OsManager()

osmanager.sort_by_extension()