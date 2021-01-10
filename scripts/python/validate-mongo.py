import os
import sys
import traceback

import urllib

import uuid

if (0):
    for f in sys.path:
        print(f)

from pymongo import MongoClient # import mongo client to connect  
import pprint  

from vyperlogix.mongo import vyperapi

if (__name__ == '__main__'):
    ADMIN_ID = '4a1bf01e-0693-48c5-a52b-fc275205c1d8'
    #ADMIN_ID = '49ac426b-cbc7-444e-9d00-49716bc0ac5c'
    vyperapi.get_environ(key='mongo')
    # Creating instance of mongoclient  
    try:
        if (0):
            db_name = os.environ.get('MONGO_INITDB_DATABASE')
            password = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
            if (len(password) == 0):
                password = input("password? ")
            client = MongoClient(os.environ.get('MONGO_URI'), username=os.environ.get('MONGO_INITDB_ROOT_USERNAME'), password=password, authSource=db_name, authMechanism=os.environ.get('MONGO_AUTH_MECHANISM'))
            print('client -> {}'.format(client))
            db_name = os.environ.get('MONGO_INITDB_DATABASE')
            db = client['{}'.format(db_name)]
            print('db -> {}'.format(db))


            vyper_admin_name = 'VYPERADMIN'
            db2 = client[vyper_admin_name]
            print('db2 -> {}'.format(db2))
            
            col2 = db2['ADMIN']
            print('col2 -> {}'.format(col2))
            
            doc = col2.find_one({'admin':ADMIN_ID})
            if (doc):
                print('*** (1) doc len -> {}'.format(len(doc)))
            else:
                print('Removing all from {} !.format(col2.name)')
                vyperapi.remove_all_admins_not_matching_this(ADMIN_ID, collection=col2, user_type='admin')
                print('Adding ADMIN_ID !')
                col2.insert_one({'admin': ADMIN_ID})
            doc = col2.find_one({'admin':ADMIN_ID})
            if (doc):
                print('*** (2) doc len -> {}'.format(len(doc)))
                print('*** doc -> {}'.format(doc))

            if (0):
                docs = col2.find()
                for doc in docs:
                    uuid = doc.get('admin')
                    if (str(uuid) == ADMIN_ID):
                        print('*** Found -> {}'.format(doc))
                    else:
                        d = {'_id':doc.get('_id')}
                        print('(-) Removed: {}'.format(d))
                        col2.remove(d)
                docs = col2.find()
                for doc in docs:
                    uuid = doc.get('admin')
                    if (str(uuid) == ADMIN_ID):
                        print('*** Found -> {}'.format(doc))
                        d = {'_id':doc.get('_id')}
                        print('*** Removed: {}'.format(d))
                        col2.remove(d)
            if (0):
                new_uuid = uuid.uuid4()
                col2.insert_one({'admin': new_uuid})

        db_name = os.environ.get('MONGO_INITDB_DATABASE')
        password = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
        if (len(password) == 0):
            password = input("password? ")

        print()
        print('BEGIN: auto_config_admin()')
        doc = vyperapi.auto_config_admin(password=password, admin_id=ADMIN_ID, app_dbName=os.environ.get('ADMIN_TABLE'), app_colName=os.environ.get('ADMIN_COL'), verbose=False, debug=False)
        assert doc and doc.get('admin'), 'Cannot verify the existence of the admin user.'
        print(doc)
        print('END!!! auto_config_admin()')
        print('\n')

        client = MongoClient(os.environ.get('MONGO_URI'), username=os.environ.get('MONGO_INITDB_ROOT_USERNAME'), password=password, authSource=db_name, authMechanism=os.environ.get('MONGO_AUTH_MECHANISM'))
        print('client -> {}'.format(client))
        db_name = os.environ.get('MONGO_INITDB_DATABASE')
        db = client['{}'.format(db_name)]
        print('db -> {}'.format(db))

        print('BEGIN: users')
        listing = db.command('usersInfo')
        for document in listing['users']:
            print('{}'.format(document))
            print('-'*30)
            print()
        print('END: users')
        print('='*30)
        print()
        
        __system_dbs = ['config', 'admin', 'local']
        print('BEGIN: databases')
        dbs = [n for n in client.database_names() if (n not in __system_dbs)]
        for n in dbs:
            print('\t{}'.format(n))
            for col in vyperapi.get_collections_from_db_by_name(n, client=client):
                print('\t\t{}'.format(col))
                __col = client[n][col]
                keys = vyperapi.get_keys_from(__col.find())
                print('\t\t\tkeys -> {}'.format(keys))
                for doc in __col.find():
                    print('\t\t\t{}'.format(doc))
                print('-'*30)
        print('END: databases')
        print('='*30)
        print()

    except Exception as ex:
        exc_info = sys.exc_info()
        print('\n'.join(traceback.format_exception(*exc_info)))
