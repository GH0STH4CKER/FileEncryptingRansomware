### Python Script That Encrypts All Files in Documents Folder

## File Encryption Tool Documentation

## Introduction
The File Encryption Tool is a Python script designed to encrypt files within a specified folder and its subfolders using the Fernet encryption method. This tool provides a secure way to protect the confidentiality of your files or for a malicious intent (Ransomware).

## Disclaimer ⚠️
**This tool is provided for educational and demonstration purposes only. Use it at your own risk!!**

## Table of Contents
1. [Introduction](#introduction)
2. [Usage](#usage)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running the Tool](#running-the-tool)
3. [Tool Explanation](#tool-explanation)
    - [Fernet Encryption](#fernet-encryption)
    - [File Replacement](#file-replacement)
4. [Security Considerations](#security-considerations)
5. [Contributing](#contributing)
6. [License](#license)
7. [Screenshots](#screenshot)

## Usage
### Prerequisites
- Python 3.x
- cryptography library (`pip install cryptography`)

### Installation
1. Clone or download the script from the repository.
2. Install the required `cryptography` library using the following command:


### Running the Tool
1. Open a terminal or command prompt.
2. Navigate to the folder containing the script.
3. Run the script using the command:

4. Follow the on-screen prompts to specify the folder path you want to encrypt.

## Tool Explanation
### Fernet Encryption
The File Encryption Tool uses the Fernet encryption method to secure your files. Fernet is a symmetric encryption algorithm, meaning the same key is used for both encryption and decryption. A secure Fernet key is generated for each run of the tool.

### File Replacement
- The original files within the specified folder and its subfolders are encrypted using the Fernet key.
- The encrypted files are saved with the same filename as the original file, but with "ENC" added to the filename (e.g., "example.txt" becomes "exampleENC.txt").
- The original files are removed from the folder to maintain security.

## Security Considerations
- Ensure that you have proper authorization to encrypt files.
- Store the generated Fernet key securely, as it is required for decryption.
- Backup important files before using this tool to prevent data loss.

## Contributing
If you'd like to contribute to the tool's development, feel free to submit pull requests.

## License
This tool is provided under the [MIT License](LICENSE).

## Screenshot
</br>
Before:<br>
<img src='https://github.com/GH0STH4CKER/FileEncryptingRansomware/assets/62290930/5014c6db-2b5a-442c-a7d7-2aed514210a7' alt='before_files' width='50%'>
</bR>After:<br>
<img src='https://github.com/GH0STH4CKER/FileEncryptingRansomware/assets/62290930/8d285c9d-c93a-4d5c-abcd-27fe49276148' alt ='after_files' width='50%'>

