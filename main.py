#!/usr/bin/python3

import subprocess
import time
from rich import print, box
from rich.console import Console
from rich.panel import Panel

# /// contoh code nodejs ...
examjs = """const http = require('node:http');
const hostname = '127.0.0.1';
const port = 3000;
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World\n');
});
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
"""

# /// form package.json ....
package_json = """{
  "name": "%s",
  "version": "%s",
  "description": "%s",
  "main": "%s",
  "scripts": {
    "test": "%s"
  },
  "repository": {
    "type": "git",
    "url": "%s"
  },
  "keywords": [
    "%s"
  ],
  "author": "%s",
  "license": "%s",
  "bugs": {
    "url": "%s/issues"
  },
  "homepage": "%s#readme"
}
"""

# /// class project ...
class CreateProject():
    def __init__(self, name_file: str):
        self.name_file = name_file
        self.requires = ["baso_kontol_real"] # contoh repository npm
        self.directory = subprocess.getoutput("pwd -P")

    def create_file(self, in_file: str):
        # //// buat isi file ....
        try:
            dengan_file = open("{}.js".format(self.name_file),"w")
            dengan_file.write("{}".format(in_file))
        except Exception as file: return file

    def create_file_package_json(self, name_: str, version: int, description: str, entery_point: str, test_command: str, git_repo: str, keyword: str, author: str, lisense: str):
        # /// buat file package_json
        try: dengan_file_json = open("package.json","w")
        except Exception as file: return file
        
        # /// simpan file package_json
        dengan_file_json.write(package_json%(name_,version,description,entery_point,test_command,git_repo,keyword,author,license,git_repo,git_repo))

    def create_packages(self, name_packages: list):
        # /// Mengintall Dependets ....
        console = Console()
        with console.status(
                Panel("* Tunggu Sedang Mengintall Dependets...",title="[green bold]INFO",border_style="green bold"
                      )
                ) as status:
            rr = subprocess.getoutput("npm i {}".format(self.requires))
            for count, package in enumerate(name_packages,1):
                status.console.print(
                        "[red bold]{} [white]: [green underline bold]{}[reset] ".format(count,package)
                        )
                result = subprocess.getoutput("npm i {}".format(package))
            return result

    def create_push_Github(self, url_github: str,  username_github: str, email_github: str):
        # /// list push github
        console = Console()
        github = [
                "git init",
                "git add .",
                "git add *",
                'git config --global user.name "{}"'.format(username_github),
                'git config --global user.email "{}"'.format(email_github),
                'git commit -m "files"',
                "git remote add origin {}".format(url_github),
                ]

        with console.status(
                Panel("* Tunggu Sedang MengUpload repository ke Github...",title="[green bold]INFO",border_style="green bold")
                ) as status:

        # /// parsing ....
            for count, __git__ in enumerate(github,1):
                time.sleep(1)
                result = subprocess.getoutput("{}".format(__git__))
                status.console.print("{}: {}".format(count, __git__))
                status.console.log(Panel(result,border_style="blue bold",highlight=True))

        # /// execute ....
        result = subprocess.getoutput("git push origin master")
        print(result)


abc = CreateProject(name_file="kontol")
#abc.create_file(in_file=examjs)
#abc.create_file_package_json(name_="%s"%(abc.directory.replace("/data/data/com.termux/files/home/","")),version="1.1.1",description="hello",entery_point="%s"%(abc.name_file),test_command="hello",git_repo="https://github.com",keyword="hello",author="irfanDect",lisense="MIT")
abc.create_packages(name_packages=["axios","yarn"])
abc.create_push_Github(url_github="https://github.com/IrfanDect/tester_upload.git",username_github="irfanDect",email_github="bsbdrack@gmail.com")
