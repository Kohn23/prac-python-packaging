from setuptools import setup, Extension
from Cython.Build import cythonize
from distutils.command.build_ext import build_ext
import sys
import os


if sys.platform == "win32":
    class BuildExt(build_ext):
        def build_extensions(self):
            self.compiler.set_executable('compiler_so', 'gcc -O2 -Wall -shared')
            self.compiler.set_executable('compiler_cxx', 'g++ -O2 -Wall -shared')
            self.compiler.set_executable('linker_so', 'gcc -shared')
            self.compiler.set_executable('linker_exe', 'gcc')
            # Cancel MSVC Macro
            self.define_macros = [('MS_WIN64', '1')]
            self.undef_macros = ['_DEBUG']
            build_ext.build_extensions(self)

    cmdclass = {'build_ext': BuildExt}
else:
    cmdclass = {}
    
    
base_dir = os.path.dirname(os.path.abspath(__file__))

pyx_file = os.path.join(base_dir, 'src', 'pkg', 'harmonic_mean.pyx')

ext_modules = cythonize([
    Extension("mypkg._Charm", [pyx_file])
])

setup(
    ext_modules=ext_modules,
    cmdclass = cmdclass,
)
