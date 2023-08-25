import sqlite3
import uvicorn
import yaml
from fastapi import FastAPI

configuration = yaml.safe_load(open('config.yml', 'r'))

class SQL_DB:
    def __init__(self):
        self.sql_connection = sqlite3.connect(configuration['database_file_name'])
        self.sql_cursor = self.sql_connection.cursor()
        for table_name in ["prom_servers", "prom_targets"]:
            table_check_output = self.sql_cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(table_name)).fetchone()
            if table_check_output == None:
                print("table is missing. Rebuilding DB")
                self.sql_cursor.execute("CREATE TABLE {} (ci_id CHAR(36) NOT NULL)".format(table_name))
                self.sql_connection.commit()

    def get_prom_servers(self):
        return self.sql_cursor.execute("select ci_id from prom_servers").fetchall()
        #self.sql_connection.commit()

    def add_prom_servers(self, ipmi_host):
        self.sql_cursor.execute("insert into prom_servers (ci_id) VALUES ('{}')".format(ipmi_host))
        self.sql_connection.commit()
        return {"total_changes": self.sql_connection.total_changes}

sql_db = SQL_DB()

tags_metadata = [
        {
            "name": "Prometheus Servers",
            "description": "Manage Prometeus Servers.",
        },
        {
            "name": "Targets",
            "description": "Manage Targets.",
        },
        {
            "name": "Target Labels",
            "description": "Manage Target Labels.",
        },
        {
            "name": "Labels",
            "description": "Manage Labels.",
        },
        {
            "name": "HTTP Service Discovery",
            "description": "Service Discovery for Prometeus servers.",
        }
    ]

app = FastAPI(
    title="HTTP Service Discovery API",
    description="Target Manager",
    summary="Contains dummy hosts and data.",
    version="0.0.1",
    contact={
        "name": "David Romero",
        "url": "https://dromero.dev",
        "email": "dl_romero@outlook.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
    )

#SERVERS
@app.get("/get_prom_servers/", tags=["Prometheus Servers"])
async def get_prom_servers():
    prometheus_servers = sql_db.get_prom_servers()
    return_data = {}
    for prometheus_server in prometheus_servers:
        return_data[prometheus_server[0]] = ""
    return (return_data)

@app.post("/add_prom_server/", tags=["Prometheus Servers"])
async def post_prom_servers(ipmi_host: str):
    return (sql_db.add_prom_servers(ipmi_host))

@app.post("/update_prom_server/{ci_id}", tags=["Prometheus Servers"])
async def post_prom_servers(ci_id: str):
    return ({"": ""})

@app.post("/remove_prom_server/{ci_id}", tags=["Prometheus Servers"])
async def post_prom_servers(ci_id: str):
    return ({"": ""})

# TARGETS
@app.get("/get_prom_targets/", tags=["Targets"])
async def get_prom_servers():
    return ({"": ""})

@app.post("/add_prom_target/", tags=["Targets"])
async def post_prom_servers():
    return ({"": ""})

@app.post("/update_prom_target/{ci_id}", tags=["Targets"])
async def post_prom_servers(ci_id: str):
    return ({"": ""})

@app.post("/remove_prom_target/{ci_id}", tags=["Targets"])
async def post_prom_servers(ci_id: str):
    return ({"": ""})

# TARGET LABELS
@app.get("/get_target_labels/", tags=["Target Labels"])
async def get_prom_servers():
    return ({"": ""})

@app.post("/add_target_label/", tags=["Target Labels"])
async def post_prom_servers():
    return ({"": ""})

@app.post("/update_target_label/{ci_id}", tags=["Target Labels"])
async def post_prom_servers(ci_id: str):
    return ({"": ""})

@app.post("/remove_target_label/{ci_id}", tags=["Target Labels"])
async def post_prom_servers(ci_id: str):
    return ({"": ""})

# LABELS
@app.get("/get_labels/", tags=["Labels"])
async def get_prom_servers():
    return ({"": ""})

@app.post("/add_label/", tags=["Labels"])
async def post_prom_servers():
    return ({"": ""})

@app.post("/update_label/{ci_id}", tags=["Labels"])
async def post_prom_servers(ci_id: str):
    return ({"": ""})

@app.post("/remove_label/{ci_id}", tags=["Labels"])
async def post_prom_servers(ci_id: str):
    return ({"": ""})

@app.post("/http_sd/{ci_id}", tags=["HTTP Service Discovery"])
async def service_discovery(ci_id: str):
    return ({"": ""})

if __name__ == "__main__":
    
    uvicorn.run("http_sd:app", host="localhost", port=5000, log_level="info")