""" TODO(O.Z.): add comments, unit tests and auto code review.
"""

_SCRIPT_VERSION_MAJOR = 0
_SCRIPT_VERSION_MINOR = 0
_SCRIPT_BUILD_NUMBER = 1

def get_script_name():
    return "Solution Generation Tools"

def get_script_version():
    return str(_SCRIPT_VERSION_MAJOR) + "." + \
           str(_SCRIPT_VERSION_MINOR) + "." + \
           str(_SCRIPT_BUILD_NUMBER)

def get_script_description():
    return "Tool for generation/building/testing C++ projects."




def main():
    pass


if __name__ == "__main__":
    main()
