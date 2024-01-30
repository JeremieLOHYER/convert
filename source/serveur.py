import uvicorn


if __name__ == "__main__":
    uvicorn.run("API:app", host="10.126.3.172", port=8000, log_level="info")