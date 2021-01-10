import os
import sys
import traceback

import uuid

from pymongo import MongoClient # import mongo client to connect  
import pprint  

def get_environ(key=None):
    if (isinstance(key, str)):
        for k,v in os.environ.items():
            if (k.lower().find(key.lower()) > -1):
                print('{} -> {}'.format(k,v))


def get_keys_from(collection):
    keylist = []
    for item in collection:
        for key in item.keys():
            if key not in keylist:
                keylist.append(key)
            if isinstance(item[key], dict):
                for subkey in item[key]:
                    subkey_annotated = key + "." + subkey
                    if subkey_annotated not in keylist:
                        keylist.append(subkey_annotated)
                        if isinstance(item[key][subkey], dict):
                            try:
                                for subkey2 in item[subkey]:
                                    subkey2_annotated = subkey_annotated + "." + subkey2
                                    if subkey2_annotated not in keylist:
                                        keylist.append(subkey2_annotated)
                            except:
                                pass
            if isinstance(item[key], list):
                for l in item[key]:
                    if isinstance(l, dict):
                        for lkey in l.keys():
                            lkey_annotated = key + ".[" + lkey + "]"
                            if lkey_annotated not in keylist:
                                keylist.append(lkey_annotated)
    return keylist


def get_collections_from_db_by_name(db_name, client=None):
    return client[db_name].list_collection_names()


def remove_all_admins_not_matching_this(u, user_type=None, collection=None):
    '''
    takes uuid for record of type key and returns None if not found else the doc if found.
    '''
    __doc__ = None
    if (collection):
        try:
            docs = collection.find()
            for doc in docs:
                uu = doc.get(user_type) if (user_type) else None
                if (str(uu) == u):
                    __doc__ = doc
                else:
                    d = {'_id':doc.get('_id')}
                    print('(-) Removed: {}'.format(d))
                    collection.remove(d)
        except:
            pass
    return __doc__


def auto_config_admin(mongouri=os.environ.get('MONGO_URI'), db_name=os.environ.get('MONGO_INITDB_DATABASE'), app_dbName=None, app_colName=None, user_type='admin', admin_id=None, username=os.environ.get('MONGO_INITDB_ROOT_USERNAME'), password=os.environ.get('MONGO_INITDB_ROOT_PASSWORD'), authMechanism=os.environ.get('MONGO_AUTH_MECHANISM'), verbose=False, debug=False, report_except=True):
    doc = None
    try:
        is_not_none = lambda s:(s) and (isinstance(s, str)) and (len(s) > 0)
        assert is_not_none(password), 'Cannot continue without a password ({}).'.format(password)
        if (not is_not_none(admin_id)):
            admin_id = str(uuid.uuid4()) # assign a uuid if none was given.
        assert is_not_none(admin_id), 'Cannot continue without an admin_id ({}).'.format(admin_id)
        client = MongoClient(mongouri, username=username, password=password, authSource=db_name, authMechanism=authMechanism)
        if (verbose):
            print('client -> ',)
            pprint.pprint(client)
        db = client[db_name]
        if (verbose):
            print('db -> ',)
            pprint.pprint(db)

        assert is_not_none(app_dbName), 'Cannot continue without an app_dbName ({}).'.format(app_dbName)
        db2 = client[app_dbName]
        if (verbose):
            print('db2 -> ',)
            pprint.pprint(db2)
            
        assert is_not_none(app_colName), 'Cannot continue without an app_colName ({}).'.format(app_colName)
        col2 = db2[app_colName]
        if (verbose):
            print('col2 -> ',)
            pprint.pprint(col2)
        
        assert is_not_none(user_type), 'Cannot continue without an user_type ({}).'.format(user_type)
        doc = col2.find_one({user_type: admin_id})
        if (doc):
            if (verbose):
                print('*** (1) doc len -> {}'.format(len(doc)))
        else:
            if (verbose):
                print('Removing all from {} !.format(col2.name)')
            remove_all_admins_not_matching_this(admin_id, collection=col2, user_type=user_type)
            if (verbose):
                print('Adding ADMIN_ID !')
            col2.insert_one({user_type: admin_id})
        doc = col2.find_one({user_type: admin_id})
        if (doc):
            if (verbose):
                print('*** (2) doc len -> {}'.format(len(doc)))
                print('*** doc -> {}'.format(doc))
        
        if (verbose and debug):
            __system_dbs = ['config', 'admin', 'local']
            print('BEGIN: databases')
            dbs = [n for n in client.database_names() if (n not in __system_dbs)]
            for n in dbs:
                print('\t{}'.format(n))
                for col in get_collections_from_db_by_name(n, client=client):
                    print('\t\t{}'.format(col))
                    __col = client[n][col]
                    keys = get_keys_from(__col.find())
                    for k in keys:
                        print('\t\t\t{}'.format(k))
                    print('-'*30)
                    __k = {k for k in keys}
                    print('*** {}'.format(__k))
                    for doc in __col.find():
                        print('\t\t\t{}'.format(doc))
            print('END: databases')
            print('='*30)
            print()
    except:
        if (report_except):
            exc_info = sys.exc_info()
            print('\n'.join(traceback.format_exception(*exc_info)))
    return doc
