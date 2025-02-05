import subprocess
from config.settings import compression_settings

class HandBrakeCompressor:
    def __init__(self, handbrake_path):
        self.handbrake_path = handbrake_path

    def compress_file(self, input_file):
        output_file = input_file.replace('.mkv', '_compressed.mkv')
        command = [
            self.handbrake_path,
            '-i', input_file,
            '-o', output_file,
            '--preset', compression_settings['preset'],
            '-q', compression_settings['quality']
        ]

        if compression_settings['audio'] == 'all':
            command.append('--all-audio')
        if compression_settings['subtitle'] == 'all':
            command.append('--all-subtitles')

        try:
            subprocess.run(command, check=True)
            return output_file
        except subprocess.CalledProcessError as e:
            print(f"Error compressing file: {e}")
            return None