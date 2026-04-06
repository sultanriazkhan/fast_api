from fastapi import FastAPI
app= FastAPI(
    title="Meri pehli app",
    description="Yeh meri pehli API hai",
    version="1.0"
)
@app.get("/")
def age():
    return {"app": "FastAPI Practice", "version": "1.0"}
@app.get("/about")
def about():   return {"name": "Sultan", "age": 30, "city": "New York"}
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "api"}