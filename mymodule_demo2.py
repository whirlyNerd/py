# This method of importing modules is not preferred since it 
# makes naming conflicts more likely, e.g. every module uses __version__

from mymodule import say_hi, __version__

say_hi()
print 'Version', __version__