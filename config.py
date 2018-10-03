import os

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = 'secret'

# There are three different ways to store the data in the application.
# You can choose 'datastore', 'cloudsql', or 'mongodb'. Be sure to
# configure the respective settings for the one you choose below.
# You do not have to configure the other data backends. If unsure, choose
# 'datastore' as it does not require any additional configuration.
DATA_BACKEND = 'datastore'

# Google Cloud Project ID. This can be found on the 'Overview' page at
# https://console.developers.google.com
PROJECT_ID = 'atyrcloud'
EMAIL_SENDER_ADDRESS = 'reminders@atyrcloud.appspotmail.com'


# cloud storage stuff for file uploading
CLOUD_STORAGE_BUCKET = 'atyrcloud.appspot.com'
MAX_CONTENT_LENGTH = 8 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'pdf', 'xls', 'xlsx',
                          'doc', 'docx', 'csv'])
