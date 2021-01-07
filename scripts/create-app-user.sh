#!/bin/bash
# https://www.stuartellis.name/articles/shell-scripting/#enabling-better-error-handling-with-set
set -Eeuo pipefail
 
# Based on mongo/docker-entrypoint.sh
# https://github.com/docker-library/mongo/blob/master/docker-entrypoint.sh#L303
if [ "$MONGO_INITDB_USERNAME" ] && [ "$MONGO_INITDB_PASSWORD" ]; then   # -u "$MONGO_INITDB_ROOT_USERNAME" -p "$MONGO_INITDB_ROOT_PASSWORD" --authenticationDatabase "$MONGO_INITDB_DATABASE"
    mongo --shell <<'EOJS'
        db.createUser({
            user: $(_js_escape "$MONGO_INITDB_USERNAME"),
            pwd: $(_js_escape "$MONGO_INITDB_PASSWORD"),
            roles: [ { role: 'readWrite', db: $(_js_escape "$MONGO_INITDB_DATABASE") } ]
        })
        use admin
        db.createUser(
            {
                user: $(_js_escape "$MONGO_INITDB_ROOT_USERNAME"),
                pwd: $(_js_escape "$MONGO_INITDB_ROOT_PASSWORD"),
                roles: [{ role: 'root', db: "admin" }, "readWriteAnyDatabase"], 
                mechanisms: [$(_js_escape "$MONGO_AUTH_MECHANISM")]
            }
        )

        use $(_js_escape "$MONGO_INITDB_DATABASE")
        db.createUser(
            {
                user: $(_js_escape "$MONGO_INITDB_USERNAME"),
                pwd: $(_js_escape "$MONGO_INITDB_PASSWORD"),
                roles: [{ role: "dbOwner", db: $(_js_escape "$MONGO_INITDB_DATABASE") }],
                mechanisms: [$(_js_escape "$MONGO_AUTH_MECHANISM")]
            }
        )
EOJS
fi