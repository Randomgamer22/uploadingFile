import os
import dropbox

class TransferData:
	def __init__(self, token):
		self.token = token

	def upload_file(self, file_from, file_to):
		dbx = dropbox.Dropbox(self.token)

		for root, folders, files in os.walk(file_from):
			print("done")
			for f in files:
				local_path = os.path.join(root, f)
				relative_path = os.path.relpath(local_path, file_from)
				dropbox_path = os.path.join(file_to, relative_path)

				with open(local_path, 'rb') as f:
					dbx.files_upload(f.read(), dropbox_path)



def main():
	token = 'sl.Av0h0sokMdiQeiXP-BiMhTOKRSLy3jFtWM_8FSwFsSu486G3dT7XcsCLUnRdMKYmbVwQ1h_ImyNNeBE9kWs4gRQ81gzF81ySdGPW8VVeoGZGaCb0X0QlaRGpUbiaciZHpaFa1OmC72Y'
	transfer_data = TransferData(token)

	file_from = input("Enter which folder you want to upload from: ")
	file_to = input("What should the folder be named: ")

	transfer_data.upload_file(file_from, file_to)
	print("Upload successful!")

main()