import sys
import inspect
from menu.getMenu import getMenu
from menu.newMenu import newMenu
from tag.getTags import getTags
from tag.newTag import newTag
from tag.updateTag import updateTag
from tag.getTagUserlist import getTagUserlist
from user.getUserlist import getUserlist
if __name__ == '__main__':
    module = sys.argv[1]
    assert module in vars(), 'Method is not accessable.'
    module = vars()[module]
    arguments = sys.argv[2:]
    argSpec = inspect.getfullargspec(module)
    assert len(arguments) == len(argSpec.args), \
        'Need {} arguments but {} arguments provided.'.format(len(argSpec.args), len(arguments))
    result = module(*arguments)
    print(result)
