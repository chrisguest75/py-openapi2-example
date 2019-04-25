#!/usr/bin/env python3

import connexion

app = connexion.FlaskApp(__name__, specification_dir='openapi/')
app.add_api('service_api.yaml')

if __name__ == '__main__':
    app.run(port=8080)
