from setuptools import setup
from distutils import sysconfig
import re
#from setuptools.dist import Distribution

site_packages_path = sysconfig.get_python_lib()
sprem = re.match(
    r'.*(lib[\\/](python\d\.\d[\\/])?site-packages)', site_packages_path, re.I)
rel_site_packages = sprem.group(1)

#class PureDistribution(Distribution):
#    def is_pure(self):
#        return True
    
setup(
    name = 'coverage_pth',
    version = '0.0.1',
    description = 'Coverage PTH file to enable coverage at the virtualenv level',
    #packages = '..',
    #include_pacakage_date=True,
    data_files=[
        (rel_site_packages, ['coverage_pth.pth',]),
    ],
    install_requires=[
        'coverage',
    ],
    #distclass=PureDistribution,
    zip_safe=False,
)