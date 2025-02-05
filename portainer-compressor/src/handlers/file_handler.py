import os

class FileHandler:
    def __init__(self, compressor, output_directory):
        self.compressor = compressor
        self.output_directory = output_directory

    def on_file_uploaded(self, file_path):
        if file_path.endswith('.mkv'):
            self.process_mkv_file(file_path)

    def process_mkv_file(self, file_path):
        compressed_file_path = self.compressor.compress_file(file_path)
        movie_title = self.extract_movie_title(file_path)
        self.organize_files(movie_title, compressed_file_path)

    def extract_movie_title(self, file_path):
        return os.path.basename(file_path).replace('.mkv', '')

    def organize_files(self, movie_title, compressed_file_path):
        main_folder = os.path.join(self.output_directory, movie_title)
        behind_the_scenes_folder = os.path.join(main_folder, 'Behind the Scenes')
        
        os.makedirs(main_folder, exist_ok=True)
        os.makedirs(behind_the_scenes_folder, exist_ok=True)
        
        os.rename(compressed_file_path, os.path.join(main_folder, os.path.basename(compressed_file_path)))
        # Move additional files to the Behind the Scenes folder if needed