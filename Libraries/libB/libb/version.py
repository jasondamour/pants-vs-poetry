import pkg_resources
import flask

def print_flask_version():
    flask_version = pkg_resources.get_distribution(flask.__name__).version
    print(f"flask version: {flask_version}")
