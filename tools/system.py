import imp
import os

MODULE_EXTENSIONS = ('.py')
def package_contents(package_name):
    file, pathname, description = imp.find_module(package_name)
    if file:
        raise ImportError('Not a package: %r', package_name)
    # Use a set because some may be both source and compiled.
    return set([os.path.splitext(module)[0]
        for module in os.listdir(pathname)
        if module.endswith(MODULE_EXTENSIONS)])

def get_dynamic_class(module_path, class_name):
	m = __import__(
		module_path,
		fromlist=[class_name]
	)
	c = getattr(m, class_name)
	return c