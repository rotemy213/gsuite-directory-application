# Functions to get data from Gsuite through the GSuite Admin SDK's Directory API
# Find sections with ${YOUR_CONFIG_HERE} and replace with your configs

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

# Scopes necessary to access Gsuite user directory
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user',
          'https://www.googleapis.com/auth/admin.directory.userschema'] # necessary for custom user attrs

SERVICE_ACCOUNT_EMAIL = ${YOUR_CONFIG_HERE}
SERVICE_ACCOUNT_PKCS12_FILE_PATH = ${YOUR_CONFIG_HERE}


def create_directory_service(user_email):
	"""
	Creates and returns an Admin SDK service object.
	:param user_email: user account that the service account will act on behalf of
	:return: Admin SDK service object
	"""

	credentials = ServiceAccountCredentials.from_p12_keyfile(
		SERVICE_ACCOUNT_EMAIL,
		SERVICE_ACCOUNT_PKCS12_FILE_PATH,
		'notasecret',   # insert secret that was generated when .p12 file was created
		scopes=SCOPES)

	credentials = credentials.create_delegated(user_email)

	return build('admin', 'directory_v1', credentials=credentials)


def get_users():
	"""
	Gets all users in the organization
	:rtype: list
	:return: List of current users
	"""

	service = create_directory_service('it_admin@atyrpharma.com')

	# Call the Admin SDK Directory API
	results = service.users().list(domain='atyrpharma.com', query="isSuspended=false orgUnitPath='/Current Users'",
	                               orderBy='familyName', projection='full').execute()

	users = results.get('users', [])
	current_users = []

	if not users:
		print('No users in the domain.')
	else:
		current_users.append(user)
				
	return current_users


def get_user(id):
	"""
	Gets user object from service and returns it
	:param id: user id in gsuite
	:return: user object
	"""
	service = create_directory_service('it_admin@atyrpharma.com')
	result = service.users().get(userKey=id, projection='full').execute()

	return result
