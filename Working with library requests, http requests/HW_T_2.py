import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                params={'path': file_path.split('\\')[-1]},
                                headers={'Authorization': uploader.token})

        with open(os.path.basename(file_path), 'rb') as f:
            upload_file = requests.put(response.json()['href'], files={'file': f})

        return print(upload_file.status_code)


if __name__ == '__main__':
    uploader = YaUploader('<Your Yandex Disk token>')
    uploader.upload(r'С:\1900_0.jpg')  # Absolute path to file

