# __all__ = ["import_submodules"]
# import os
# for module in os.listdir(os.path.dirname(__file__)):
#     if module == '__init__.py' or module[-3:] != '.py':
#         continue
#     __all__.append(module[:-3])
# del module

# import importlib
# import pkgutil


# def import_submodules(package, recursive=True):
#     """ Import all submodules of a module, recursively, including subpackages

#     :param package: package (name or actual module)
#     :type package: str | module
#     :rtype: dict[str, types.ModuleType]
#     """
#     if isinstance(package, str):
#         package = importlib.import_module(package)
#     results = {}
#     for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
#         full_name = package.__name__ + '.' + name
#         try:
#             results[full_name] = importlib.import_module(full_name)
#         except ModuleNotFoundError:
#             continue
#         if recursive and is_pkg:
#             results.update(import_submodules(full_name))
#     return results

__all__ = ["I will get rewritten"]
# Don't modify the line above, or this line!
import automodinit
automodinit.automodinit(__name__, __file__, globals())
del automodinit
# Anything else you want can go after here, it won't get modified.
