from setuptools import setup, find_packages
setup(
    name = 'L4-2_omop531-etl-synthea',
    version = '1.0',
    packages = find_packages(include = ('l42_omop531etlsynthea*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.8.13'],
    entry_points = {
'console_scripts' : [
'main = l42_omop531etlsynthea.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
