from paver.tasks import task, BuildFailure
from paver.easy import *

@task
def run_doc_tests():
    sh('nosetests --with-doctest --rednose ./src/app --verbose')

@task
def run_unit_tests():
    sh('nosetests --with-coverage --rednose ./src/test/unit')

@task
def run_mock_tests():
    sh('nosetests --with-coverage --rednose ./src/test/mock')

@task
def run_integration_tests():
    sh('nosetests --with-coverage --rednose ./src/test/integration')

@task
def run_acceptance_tests():
    sh('cd ./src; behave ./test/acceptance --verbose')

@task
def run_pylint():
    try:
        sh('pylint ./src/app/*')
    except BuildFailure:
        pass

@task 
def generate_docs():
    sh("cd ./src/doc; sphinx-apidoc --force -o ./source './../app'")
    sh("cd ./src/doc; make html")


@task
def create_zip_package():
    sh('cd ./pack/zip; zip app ./../../src/app/* -r')


@needs('run_doc_tests', 'run_unit_tests', 'run_mock_tests',
       'run_integration_tests', 'run_acceptance_tests',
       'run_pylint', 'generate_docs', 'create_zip_package')
@task
def default():
    pass
