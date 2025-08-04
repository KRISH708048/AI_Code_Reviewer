from fastapi import FastAPI
from routes import analyze, users, history # Import new routers
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Code Review Backend",
    description="Backend API for analyzing and reviewing code using LLMs.",
    version="1.0.0"
)

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "https://ai-code-reviewer-nine-nu.vercel.app",
    "https://ai-code-reviewer-git-main-krishs-projects-d8c81696.vercel.app",
    "https://ai-code-reviewer-krishs-projects-d8c81696.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      
    allow_methods=["*"],        
    allow_headers=["*"],        
)

app.include_router(users.router, tags=["Users & Auth"])
app.include_router(analyze.router, tags=["Code Analysis"])
app.include_router(history.router, tags=["History"])

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Code Review API"}
