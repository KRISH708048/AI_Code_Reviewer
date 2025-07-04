from fastapi import FastAPI
from routes import analyze
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Code Review Backend",
    description="Backend API for analyzing and reviewing code using LLMs.",
    version="1.0.0"
)

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      
    allow_methods=["*"],        
    allow_headers=["*"],        
)
app.include_router(analyze.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Code Review API"}


# https://ai-code-reviewer-d2j2.onrender.com