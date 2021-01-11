/*
use admin
db.createUser(
    {
        user: "root",
        pwd: passwordPrompt(),
        roles: [{ role: 'root', db: "admin" }, "readWriteAnyDatabase", "dbAdminAnyDatabase"], 
        mechanisms: ["SCRAM-SHA-256"]
    }
)
*/