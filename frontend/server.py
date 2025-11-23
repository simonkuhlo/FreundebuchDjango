import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="192.168.178.38", port=6969, reload=True)