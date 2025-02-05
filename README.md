# Portainer Compressor

## Overview
Portainer Compressor is a Python application designed to listen for new MKV files uploaded to a specified folder, compress those files using HandBrake, and organize them into a Plex directory structure. Each movie will have its own folder named after the title, containing the main compressed movie file and a nested "Behind the Scenes" folder for additional files.

## Project Structure
```
portainer-compressor
├── src
│   ├── main.py                # Entry point of the application
│   ├── handlers
│   │   └── file_handler.py     # Handles new file uploads
│   ├── utils
│   │   └── handbrake_compressor.py # Compresses MKV files using HandBrake
│   └── config
│       └── settings.py        # Configuration settings
├── Dockerfile                  # Docker image instructions
├── docker-compose.yml          # Service definitions for Docker
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Setup Instructions
1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd portainer-compressor
   ```

2. **Install dependencies:**
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure settings:**
   Edit `src/config/settings.py` to set the input and output directory paths and any HandBrake settings.

4. **Build the Docker image:**
   ```
   docker build -t portainer-compressor .
   ```

5. **Run the application:**
   You can use Docker Compose to start the application:
   ```
   docker-compose up
   ```

## Usage
- Place MKV files in the designated input folder specified in the settings.
- The application will automatically detect new files, compress them, and organize them into the Plex directory structure.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.