import argparse
import toml
import json
# Make sure to update these dependancies in poetry group:
# tool.poetry.group.gh_read_pyproject

description ="""
This is a quick script used by GithubWorkflows 
when interpreting important values from pyproject.toml.

For instance if github workspaces wanted python versions to test,
instead of interpreting the file itself, it will call this script:

interpret_pyproject -py_versions

If only one argument was inputed, only the corresponding value will be output,
but will be encoded into json. If multiple arguments were inputted, a dictionary
will be created with those values, encoded into json, and be outputed.

This is done so someone unfimiliar with github workflows can fix
errors that occour from refactoring pyproject.toml without
having to look through github workflows to figure it out. 
It should also mean that the github workflows would be more clear.

We also must ensure that the interface to github (the arguments)
doen't change meaning even if pyproject.toml changes syntax.
"""

# interpret_pyproject -py_versions

parser = argparse.ArgumentParser(
    prog= "interpret pyproject.toml for Github Workflows",
    description=description
)
def create_value_identifier(parser:argparse.ArgumentParser, argument_name:str,description:str)-> None:
    "creates the commandline arguments that identify the value to extract from pyproject.toml."
    parser.add_argument("--"+argument_name,dest=argument_name,action="store_true",default=False,help=description)

create_value_identifier(parser,"python_versions","The python versions we test, all of which our code should work when using.")
create_value_identifier(parser,"homepage","The homepage URL for the repository.")
create_value_identifier(parser,"repository","The github repository URL.")
create_value_identifier(parser,"documentation","The documentation URL for the repository.")

args = parser.parse_args()
output = {}
py_project_toml = "pyproject.toml"
py_project_data = toml.load(py_project_toml)

if args.python_versions:
    #The versions of python that must pass all tests in github workflows
    output["python_versions"] = \
        py_project_data["tests"]["workflows"]["python-versions"]
    
if args.homepage:
    #URL of repository homepage
    output["homepage"] = \
        py_project_data["tool"]["poetry"]["homepage"]

if args.repository:
    #URL of github repository 
    output["repository"] = \
        py_project_data["tool"]["poetry"]["repository"]
    
if args.documentation:
    #URL of repository documentation
    output["documentation"] = \
        py_project_data["tool"]["poetry"]["documentation"]

json_encoder = json.JSONEncoder()

if len(output) == 1:
    print(json_encoder.encode(list(output.values())[0]))
else:
    print(json_encoder.encode(output))

exit(0)