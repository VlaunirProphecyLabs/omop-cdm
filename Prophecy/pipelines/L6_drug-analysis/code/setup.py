from setuptools import setup, find_packages
setup(
    name = 'L6-1_drug-analysis_UsageofOxycodonestratifiedbygender',
    version = '1.0',
    packages = find_packages(include = ('l6_druganalysis*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.8.13'],
    entry_points = {
'console_scripts' : [
'main = l6_druganalysis.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
