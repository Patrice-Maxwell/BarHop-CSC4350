from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file("credentials.json", scopes=scopes)
credentials = flow.run_local_server(port=8080)

