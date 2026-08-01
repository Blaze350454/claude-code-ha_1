"""Import this BEFORE cadquery. CadQuery hard-imports VTK at load, but the
build/STEP-export path only uses OCP. This machine's VTK native DLLs are blocked
by Application Control policy, so satisfy `import vtkmodules.*` with harmless
stubs (never actually called). Same shim as flood_table_filter."""
import sys, types, importlib.abc, importlib.machinery


class _VtkStub(types.ModuleType):
    def __getattr__(self, name):
        return type(name, (), {})


class _VtkFinder(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def find_spec(self, fullname, path, target=None):
        if fullname == "vtkmodules" or fullname.startswith("vtkmodules."):
            return importlib.machinery.ModuleSpec(fullname, self)
        return None

    def create_module(self, spec):
        return _VtkStub(spec.name)

    def exec_module(self, module):
        pass


sys.meta_path.insert(0, _VtkFinder())
