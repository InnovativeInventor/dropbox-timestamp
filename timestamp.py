import dropbox
import requests

class Timestamp:
    def __init__(self, token = None):
        if not token:
            assert ValueError("You need to pass the token argument")
        else:
            self.dbx = dropbox.Dropbox(token)

    def check_user(self):
        return self.dbx.users_get_current_account()

    def timestamp(self):
        for entry in self.dbx.files_list_folder('', recursive = True).entries:
            if isinstance(entry, dropbox.files.FileMetadata):
                self.send_timestamp(entry.content_hash)
                print(entry.content_hash)

        self.upgrade()

    def send_timestamp(self, sha256):
        requests.post("https://stamp.homelabs.space/stamp/" + str(sha256).rstrip())

    def upgrade(self):
        requests.get("https://stamp.homelabs.space/upgrade")
