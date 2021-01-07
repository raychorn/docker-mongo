import os
import sys
import traceback

def get_environ(key=None):
    if (isinstance(key, str)):
        for k,v in os.environ.items():
            if (k.lower().find(key.lower()) > -1):
                print('{} -> {}'.format(k,v))

if (__name__ == '__main__'):
    get_environ(key='mongo')
    from pymongo import MongoClient # import mongo client to connect  
    import pprint  
    # Creating instance of mongoclient  
    try:
        db_name = os.environ.get('MONGO_INITDB_DATABASE')
        client = MongoClient(os.environ.get('MONGO_URI'), username=os.environ.get('MONGO_INITDB_ROOT_USERNAME'), password=os.environ.get('MONGO_INITDB_ROOT_PASSWORD'), authSource=db_name, authMechanism=os.environ.get('MONGO_AUTH_MECHANISM'))
        print('client -> {}'.format(client))
        db_name = os.environ.get('MONGO_INITDB_DATABASE')
        db = client['{}'.format(db_name)]
        print('db -> {}'.format(db))
        
        listing = db.command('usersInfo')
        for document in listing['users']:
            print('{}'.format(document))
            print('='*30)
            print()
        
    except Exception as ex:
        exc_info = sys.exc_info()
        print('\n'.join(traceback.format_exception(*exc_info)))
