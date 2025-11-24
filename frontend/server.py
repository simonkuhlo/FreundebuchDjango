import uvicorn
import settings

def run_server_blocking(app_path: str = "app:app", host: str = settings.server_host, port: int = settings.server_port):
    uvicorn.run(app_path, host=host, port=port)

if __name__ == "__main__":
    run_server_blocking()