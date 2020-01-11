from dropbox import DropboxOAuth2FlowNoRedirect
import dropbox
from conf import api_token, secret_key

auth_flow = DropboxOAuth2FlowNoRedirect(api_token, secret_key)

authorize_url = auth_flow.start()
print("1. Go to: " + authorize_url)
print("2. Click \"Allow\" (you might have to log in first).")
print("3. Copy the authorization code.")
auth_code = input("Enter the authorization code here: ").strip()

try:
    oauth_result = auth_flow.finish(auth_code)
except Exception as e:
    print('Error: %s' % (e,))

dbx = dropbox.Dropbox(oauth_result.access_token)
print("Token", oauth_result.access_token)
