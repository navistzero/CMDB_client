import importlib

def get_class(path):
    module_str,cls_str=path.rsplit(".",maxsplit=1)
    module=importlib.import_module(module_str)
    return getattr(module,cls_str)



