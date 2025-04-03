# Google Slides to PNG Exporter

A secure Docker container that exports Google Slides presentations to high-quality PNG files, with proper slide numbering. Perfect for creating presentation archives or generating slide images for web use.

## Quick Start (Using Docker)

1. **Set up Google Cloud Project**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Google Slides API for your project
   - Create credentials (OAuth 2.0 Client ID)
   - Download the credentials and save them as `credentials.json`

2. **Run the Container**:
   ```bash
   # Create a directory for exported slides
   mkdir exported_slides

   # Run the container
   docker compose up

   # Or with custom paths:
   CREDENTIALS_PATH=/path/to/credentials.json \
   TOKEN_PATH=/path/to/token.pickle \
   EXPORT_PATH=/path/to/exports \
   docker compose up
   ```

3. **Use the Exporter**:
   - On first run, follow the OAuth authentication prompt in your browser
   - Enter the Google Slides URL when prompted (formats supported):
     - `https://docs.google.com/presentation/d/[PRESENTATION_ID]/edit`
     - `https://docs.google.com/presentation/d/[PRESENTATION_ID]/view`
   - Slides will be exported to the `exported_slides` directory (or your custom `EXPORT_PATH`)

## Environment Variables

- `CREDENTIALS_PATH`: Path to your Google OAuth credentials file (default: `./credentials.json`)
- `TOKEN_PATH`: Path to store the OAuth token (default: `./token.pickle`)
- `EXPORT_PATH`: Directory where slides will be exported (default: `./exported_slides`)

## Development

For development purposes, use the development compose file:

```bash
docker compose -f docker-compose.dev.yml up
```

This will build the container from source instead of using the pre-built image.

## Security Features

This container runs with several security enhancements:
- Read-only filesystem
- Dropped capabilities
- No privilege escalation
- Temporary filesystem for volatile data

## Notes

- Requires an active internet connection
- The Google Slides presentation must be accessible to your Google account
- Exported PNG files maintain the original slide resolution
- Authentication tokens are saved in `token.pickle` for future use
- The container automatically handles Google OAuth authentication 