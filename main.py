import uvicorn
from fastapi import FastAPI

from routers import tweet

app = FastAPI()
app.include_router(router=tweet.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0')
