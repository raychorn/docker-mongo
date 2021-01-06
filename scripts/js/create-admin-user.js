/*
use admin
db.createUser(
    {
        user: "admin",
        pwd: passwordPrompt(),
        roles: [{ role: 'root', db: "admin" }, "readWriteAnyDatabase"], 
        mechanisms: ["SCRAM-SHA-256"]
    }
)

use angularappgenerator
db.angularappgenerator.insert({ name: "sample name", value: 205 })
db.createUser(
    {
        user: "appuser",
        pwd: passwordPrompt(),
        roles: [{ role: "dbOwner", db: "angularappgenerator" }],
        mechanisms: ["SCRAM-SHA-256"]
    }
)

use angularappgenerator
db.updateUser("appuser",
    {
        pwd: passwordPrompt(),
        roles: [
            { role: "dbOwner", db: "angularappgenerator" }
        ]
    }
)
*/