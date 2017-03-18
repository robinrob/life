import subprocess
import os
import csv
import sys
from termcolor import colored
import subprocess

from fabric.decorators import task

DEFAULT_BRANCH = "master"


@task
def commit(message="Auto-update."):
    add()
    status()
    subprocess.call("git commit -m '" + message + "'", shell=True)


@task
def status():
    subprocess.call("git status", shell=True)


@task
def install(destination=None):
    # install_python()
    install_requirements()
    if not os.path.exists(LOGS):
        os.mkdir(LOGS)


def install_python():
    subprocess.call("pythonbrew install " + PYTHON, shell=True)


def use_python(version):
    subprocess.call("pythonbrew use " + version, shell=True)


def install_requirements():
    # use_python(PYTHON)
    subprocess.call("pip install -r requirements.txt", shell=True)

@task
def clean():
    subprocess.call("find . -name '*.pyc' -delete", shell=True)
    subprocess.call("find . -name '__pycache__' -delete", shell=True)
    subprocess.call("find . -name '*~' -delete", shell=True)
    subprocess.call("find . -name '*.orig' -delete", shell=True)
    subprocess.call("find logs -name '*.log' -delete", shell=True)


@task
def test():
    subprocess.call("nosetests", shell=True)


@task
def count():
    clean()
    subprocess.call("find . -name '*.py' | xargs wc -l", shell=True)


@task
def commit(message="Auto-update."):
    add()
    status()
    subprocess.call("git commit -m '" + message + "'", shell=True)


@task
def add():
    clean()
    subprocess.call("git add .", shell=True)
    subprocess.call("git add .gitignore", shell=True)
    subprocess.call("git add -u", shell=True)
    subprocess.call("git add README.md --ignore-errors", shell=True)
    subprocess.call("git add requirements.txt --ignore-errors", shell=True)


@task
def push(branch=DEFAULT_BRANCH):
    subprocess.call("git push origin " + branch, shell=True)


@task
def pull(branch=DEFAULT_BRANCH):
    subprocess.call("git pull origin " + branch, shell=True)


@task
def status():
    subprocess.call("git status", shell=True)


@task
def log():
    subprocess.call("git log", shell=True)


@task
def save(message="Auto-update", branch=DEFAULT_BRANCH):
    commit(message)
    pull(branch)
    push(branch)


def wrap_quotes(s):
    return "'" + s + "'"


@task
def test():
    subprocess.call("nosetests", shell=True)


@task
def count():
    clean()
    subprocess.call("find . -name '*.py' | xargs wc -l", shell=True)


@task
def checkout(branch):
    subprocess.call("git checkout " + branch, shell=True)


@task
def publish(message="Auto-update", from_branch="develop", to_branch=DEFAULT_BRANCH):
    commit(message)
    pull(from_branch)
    push(from_branch)
    checkout(to_branch)
    pull(from_branch)
    push(to_branch)


@task
def log():
    # Git formats
    git_log_medium_format = "%C(bold)commit:%C(reset) %C(green)%H%C(red)%d%n%C(bold)Author:%C(reset) %C(cyan)%an <%ae>%n%C(bold)Date:%C(reset)   %C(blue)%ai (%ar)%C(reset)%n%+B"
    #git_log_oneline_format = "%C(green)%h%C(reset) %s%C(red)%d%C(reset)%n"
    #git_log_brief_format = "%C(green)%h%C(reset) %s%n%C(blue)(%ar by %an)%C(red)%d%C(reset)%n"


    # Git aliases
    #gl="git log --topo-order --pretty=format:${_git_log_medium_format}" + wrap_quotes(git_log_medium_format)
    gls="git log --topo-order --stat --pretty=format:" + wrap_quotes(git_log_medium_format)
    #gld="git log --topo-order --stat --patch --full-diff --pretty=format:" + wrap_quotes(git_log_medium_format)
    #glo="git log --topo-order --pretty=format:" + wrap_quotes(git_log_oneline_format)
    #glg="git log --topo-order --all --graph --pretty=format:" + wrap_quotes(git_log_oneline_format)
    #glb="git log --topo-order --pretty=format:" + wrap_quotes(git_log_brief_format)
    #glc="git shortlog --summary --numbered"


    subprocess.call(gls, shell=True)


def wrap_quotes(s):
    return "'" + s + "'"

@task
def readme():
    subprocess.call("less README.md", shell=True)


@task
def sub_deinit(submodule):
  if submodule is "all":
    deinit_all()

  else:
    deinit(submodule)


def deinit_all():
    with open('submodules.csv', 'rt') as file:
        reader = csv.reader(file, delimiter=',', quotechar='|')
        reader.readLine()
        [deinit(row) for row in reader]


def deinit(submodule):
    repo = colored(submodule, 'green')
    prefix=colored("Deinit repo:", 'red')
    print("{} {}".format(prefix, repo))

    cmd = "rm -rf {}".format(submodule)
    do(cmd)
    cmd = "git rm -rf --ignore-unmatch --cached {}".format(submodule)
    do(cmd)
    cmd = "git submodule deinit {} 2> /dev/null".format(submodule)
    do(cmd)


def show(cmd):
    print(cmd)


def do(cmd):
    show(cmd)
    subprocess.call(cmd, shell=True)