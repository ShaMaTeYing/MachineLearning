import requests

file_url = "https://github-production-release-asset-2e65be.s3.amazonaws.com/23216272/503f5ade-bd6d-11e7-91ab-b3405ddf16bf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20171105%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20171105T124908Z&X-Amz-Expires=300&X-Amz-Signature=4a4fa87d8727b089780124628856646ab28952ff79034129592488e941296318&X-Amz-SignedHeaders=host&actor_id=22962540&response-content-disposition=attachment%3B%20filename%3DGit-2.15.0-64-bit.exe&response-content-type=application%2Foctet-stream"

r = requests.get(file_url, stream=True)

with open("git.exe", "wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            pdf.write(chunk)
