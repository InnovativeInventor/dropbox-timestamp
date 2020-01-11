## Dropbox-timestamp

This tool is intended to timestamp an entire user's Dropbox and publish the associated attestation on the Bitcoin blockchain using OpenTimestamps. Currently it is *very slow* for large Dropbox accounts.

## Design
This uses the API provided by (myself) at https://stamp.homelabs.space/stamp/$HASH. To fetch a file's proof (which is not stored locally by default, go to https://stamp.homelabs.space/hash/$HASH.ots . Since Dropbox uses a special way to rapidly hash files, this *will not* match up with shasum or any other standard hashing utility.

To verify the proof, use their implementation:
https://github.com/dropbox/dropbox-api-content-hasher

Source: https://www.dropbox.com/developers/reference/content-hash

## Usage
Simply edit `conf-sample.py` to contain the proper api/secrets/tokens and then rename it to `conf.py`.

Note: The tokens in `conf-sample.py` were generated randomly.
