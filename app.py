from flask import Flask
from myproject.app import MyFlaskApp
from myproject import config as config_module


if __name__ == '__main__':
    app = MyFlaskApp(Flask(__name__), 
                    config_module=config_module,
                    blueprint_dirname="blueprint")
    """
    app.app_context().push()
    app.db.drop_all()
    app.db.create_all()
    """
    app.run()

