# vidGen - Automated Video Generation and Upload

A Python-based tool for automating video generation from audio and video clips, and uploading them to YouTube.

## Features

*   Automated video creation from diverse audio and video sources.
*   Dynamic title, description, and tag generation.
*   Scheduled video generation and upload.
*   YouTube API integration for seamless uploads.

## Files

*   `captions.py`: Handles dynamic generation of video titles, descriptions, and tags.
*   `main.py`: Orchestrates the video generation process, including selecting media, concatenating clips, and scheduling tasks.
*   `upload.py`: Manages the authentication with YouTube API and the video upload process.
*   `desc_adder.txt`: Additional text to be appended to video descriptions.
*   `durration_base.txt`: Configures the desired duration for generated videos.
*   `paths.csv`: Defines paths for video and audio content, potentially with daily schedules and durations.
*   `requirements.txt`: Lists Python dependencies.
*   `Dockerfile`: For containerized deployment.

## Setup

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **YouTube API Credentials:**
    Obtain your `client_secret.json` file from the Google Cloud Console and place it in the project root directory.
3.  **Media Directories:**
    Create the following directory structure for your video and audio content:
    ```
    Mount/
    ├── Audio/
    │   └── [category_folder]/
    │       └── audio_file.mp3
    └── Video/
        └── [category_folder]/
            └── video_file.mp4
    ```
    Replace `[category_folder]` with your desired categories (e.g., "Gaming", "Study").

## Usage

To run the automated video generation and upload process, execute `main.py`:

```bash
python main.py
```

The `main.py` script is configured to run the `generate` function daily at 07:00:00.

### Configuration

*   **`durration_base.txt`**: This file should contain a single number representing the desired duration (in minutes) for the generated videos.
*   **`paths.csv`**: This CSV file allows you to define specific paths for video and audio content based on the day of the week, and override the default video duration. The format should be:
    ```csv
    day,path,durration
    0,Gaming,15
    1,Study,20
    ```
    Where `day` is an integer (0 for Monday, 6 for Sunday), `path` is the category folder name, and `durration` is the desired video duration in minutes for that day.
