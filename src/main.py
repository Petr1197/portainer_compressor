import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from handlers.file_handler import FileHandler
from utils.handbrake_compressor import HandBrakeCompressor
from config.settings import input_directory, output_directory, handbrake_path

class FileWatcher(FileSystemEventHandler):
    def __init__(self, handler):
        self.handler = handler

    def on_created(self, event):
        if not event.is_directory:
            self.handler.on_file_uploaded(event.src_path)

if __name__ == "__main__":
    compressor = HandBrakeCompressor(handbrake_path)
    handler = FileHandler(compressor, output_directory)
    event_handler = FileWatcher(handler)
    observer = Observer()
    observer.schedule(event_handler, input_directory, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()