from fastapi import FastAPI
app= FastAPI(
    title="Meri pehli app",
    description="Yeh meri pehli API hai",
    version="1.0"
)
@app.get("/")
def age():
    return {"message": "Hello World" , "status": "Running"}
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "api"}