import os
import re
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pickle
from urllib.parse import urlparse, parse_qs
import requests
from dotenv import load_dotenv

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/presentations.readonly']

def get_credentials():
    """Gets valid user credentials from storage or initiates OAuth2 flow."""
    creds = None
    
    # The file token.pickle stores the user's access and refresh tokens
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def extract_presentation_id(url):
    """Extract the presentation ID from a Google Slides URL."""
    # Handle both presentation/d/ and presentation/edit style URLs
    match = re.search(r'/d/([a-zA-Z0-9-_]+)', url)
    if not match:
        match = re.search(r'/presentation/([a-zA-Z0-9-_]+)', url)
    
    if not match:
        raise ValueError("Could not extract presentation ID from URL")
    
    return match.group(1)

def download_slide_as_png(export_url, filename):
    """Download a slide as PNG."""
    response = requests.get(export_url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Successfully downloaded {filename}")
    else:
        print(f"Failed to download {filename}")

def export_slides_to_png(presentation_url):
    """Export all slides from a presentation to PNG files."""
    try:
        # Get credentials and build service
        creds = get_credentials()
        service = build('slides', 'v1', credentials=creds)
        
        # Get presentation ID from URL
        presentation_id = extract_presentation_id(presentation_url)
        
        # Create output directory if it doesn't exist
        output_dir = 'exported_slides'
        os.makedirs(output_dir, exist_ok=True)
        
        # Get presentation details
        presentation = service.presentations().get(
            presentationId=presentation_id).execute()
        slides = presentation.get('slides', [])
        
        print(f"Found {len(slides)} slides in the presentation")
        
        # Export each slide
        for i, slide in enumerate(slides, 1):
            # Construct the export URL
            export_url = f"https://docs.google.com/presentation/d/{presentation_id}/export/png?id={presentation_id}&pageid={slide['objectId']}"
            
            # Download the slide
            filename = os.path.join(output_dir, f"slide_{i:03d}.png")
            download_slide_as_png(export_url, filename)
            
        print("\nExport completed!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Get the presentation URL from user input
    presentation_url = input("Please enter the Google Slides URL: ")
    export_slides_to_png(presentation_url) 