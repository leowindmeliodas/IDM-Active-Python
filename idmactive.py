import requests
import subprocess
import os

# Enable TLSv1.2 for compatibility with older clients
try:
    from requests.packages.urllib3.util.ssl_ import create_urllib3_context
    context = create_urllib3_context()
    context.options |= getattr(requests.packages.urllib3.contrib, "pyopenssl", None).openssl.SSL.OP_NO_TLSv1 | \
                       getattr(requests.packages.urllib3.contrib, "pyopenssl", None).openssl.SSL.OP_NO_TLSv1_1
    requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST = 'DEFAULT@SECLEVEL=1'
except (ImportError, AttributeError):
    pass

# Download script
download_url = 'https://raw.githubusercontent.com/leowindmeliodas/IDM-Active/main/IAS_0.8.cmd'
file_path = os.path.join(os.environ['TEMP'], 'IAS.cmd')

try:
    with open(file_path, 'wb') as file:
        response = requests.get(download_url)
        file.write(response.content)
except Exception as e:
    print(f"Error: {e}")
    exit()

# Run script
try:
    subprocess.run(file_path, check=True, shell=True)
finally:
    # Delete the file after execution
    os.remove(file_path)