import subprocess

def pbpaste():

    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)

    retcode = p.wait()

    data = p.stdout.read()

    return data


def pbcopy(data):

    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)

    try:

        p.stdin.write(data)

    except TypeError:

        p.stdin.write(repr(data))

    p.stdin.close()
