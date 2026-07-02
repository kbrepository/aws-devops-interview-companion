from fastapi import FastAPI

app = FastAPI(
    title="AWS DevOps Interview Companion API",
    description="A simple FastAPI application used for AWS DevOps interview preparation.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "aws-devops-interview-companion",
        "version": "0.1.0",
    }


@app.get("/")
def root():
    return {
        "message": "Welcome to AWS DevOps Interview Companion API"
    }