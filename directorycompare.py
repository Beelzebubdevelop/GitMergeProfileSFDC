import platform
import pathlib
import filecmp

# def filedirectorycmp(path1, path2):
#     result = filecmp.dircmp(adjustPathname(path1), adjustPathname(path2))
#     return result.common

# def isWindows():
#     return (platform.system() == 'Windows')

# def adjustPathname(path):
#     if isWindows():
#         return pathlib.Path('r'+path)
#     else:
#         return pathlib.Path(path)

def filedirectorycmp(path1, path2):
    result = filecmp.dircmp(path1, path2)
    return result.common