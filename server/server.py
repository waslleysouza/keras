import os
import connexion

PORT = int(os.environ.get('PORT', 5000))

application = connexion.App(__name__, port=PORT, specification_dir='')
application.add_api('models.yaml')


if __name__ == '__main__':
    application.run(server='tornado', debug=True)
