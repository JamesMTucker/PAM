from configparser import ConfigParser

def pam_dir(filename='directories.ini', section='PAM'):
    """
    Return Directory to the PAM images
    """

    parser = ConfigParser()
    parser.read(filename)
    pam = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            pams[param[0]] = param[1]
        else:
            raise Exception(f'Section {section} is not found in {filename}')
        return pam