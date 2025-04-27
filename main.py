from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "مرحبًا بك في وكالة دايناميكا الإخبارية!"}

@app.get("/news")
async def get_news():
    # هذه نقطة النهاية التي يمكن استخدامها لإرجاع الأخبار
    return {"news": "خبر مثال"}
