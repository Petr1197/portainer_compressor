import os

input_directory = os.getenv('INPUT_DIRECTORY', '/path/to/input/directory')
output_directory = os.getenv('OUTPUT_DIRECTORY', '/path/to/output/directory')
handbrake_path = os.getenv('HANDBRAKE_PATH', '/usr/bin/HandBrakeCLI')
video_extensions = os.getenv('VIDEO_EXTENSIONS', '.mkv').split(',')
compression_settings = {
    "preset": os.getenv('COMPRESSION_PRESET', 'H.264 MKV 1080p30'),
    "quality": os.getenv('COMPRESSION_QUALITY', '22'),
    "audio": os.getenv('COMPRESSION_AUDIO', 'all'),
    "subtitle": os.getenv('COMPRESSION_SUBTITLE', 'all')
}