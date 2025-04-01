import os

from flask_api import create_app

app = create_app(os.getenv('FLASK_CONFIG', 'default'))

if __name__ == '__main__':
    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.methods} {rule}")
    app.run()
