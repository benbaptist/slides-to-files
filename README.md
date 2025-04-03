# Google Slides to PNG Exporter

This script allows you to export all slides from a Google Slides presentation as individual PNG files, with proper numbering.

## Setup

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up Google Cloud Project and enable the Google Slides API:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Google Slides API for your project
   - Create credentials (OAuth 2.0 Client ID)
   - Download the credentials and save them as `credentials.json` in the same directory as the script

## Usage

1. Run the script:
   ```bash
   python export_slides.py
   ```

2. When prompted, enter the Google Slides URL. The URL should be in one of these formats:
   - `https://docs.google.com/presentation/d/[PRESENTATION_ID]/edit`
   - `https://docs.google.com/presentation/d/[PRESENTATION_ID]/view`

3. On first run, the script will open your browser for Google OAuth authentication. Follow the prompts to authorize the application.

4. The slides will be exported as PNG files in the `exported_slides` directory, named as `slide_001.png`, `slide_002.png`, etc.

## Notes

- The script requires an active internet connection
- Make sure the Google Slides presentation is accessible to your Google account
- The exported PNG files will be in the same resolution as they appear in Google Slides
- Your authentication tokens will be saved in `token.pickle` for future use 