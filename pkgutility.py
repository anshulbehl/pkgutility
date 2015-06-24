import github3
import getpass
import os
import sys
import tempfile


def get_password():
    """
    Get the password of github user
    """
    passwd = getpass.getpass(prompt='Enter the Github Password: ')

    return passwd


def get_all_requirements(user, ghuser, file):
    """
    Get all the requirements from all the public repos of a github user
    """
    github = github3.GitHub(user, get_password())

    # Get all the public repos of a github user
    public_repo = [repo.name for repo in github.repositories_by(ghuser)]

    # Get contents of a file from all the public repo
    reqr = {}
    for repo in public_repo:
        robj = github.repository(ghuser, repo)

        if file in robj.directory_contents('.', return_as=dict).keys():
            file_content = robj.file_contents(file)

            repo_pkg = []
            for data in file_content.decoded.split('\n'):
                if not data.startswith('#') and not (data == ''):
                    if not data.startswith('http') and not data.startswith('-e'):
                        repo_pkg.append(split_string(data))

            reqr.update({repo:repo_pkg})

    return reqr

# TODO Find a better way to split a package having version number

def split_string(string):
    """
    Remove version number from a package
    """
    if '>=' in string:
        return string.split('>=')[0]
    elif '!=' in string:
        return string.split('!=')[0]
    elif '<=' in string:
        return string.split('<=')[0]
    elif '~=' in string:
        return string.split('~=')[0]
    elif '==' in string:
        return string.split('==')[0]
    elif '>' in string:
        return string.split('>')[0]
    elif '<' in string:
        return string.split('<')[0]
    elif '===' in string:
        return string.split('===')[0]
    elif '#' in string:
        return string.split('#')[0]
    else:
        return string

def generate_requirements(reqr_dict, ghuser):
    """
    Generate a final requirements file
    """
    pkgs = []
    for pkg in reqr_dict.values():
        pkgs.extend(pkg)

    final_pkg = list(set(pkgs))

    dirpath = tempfile.mkdtemp()
    filename = ghuser + '.txt'
    with open(os.path.join(dirpath, filename), 'w') as fobj:
        for item in final_pkg:
            fobj.write('%s\n' % item)

    print '%s file is created at %s' % (filename, dirpath)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        reqr_dict = get_all_requirements(sys.argv[1], sys.argv[2], sys.argv[3])
        generate_requirements(reqr_dict, sys.argv[2])
    else:
        print "Usage: python pkgutility.py <github username> openstack test-requirements.txt"



