from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app instance
app = FastAPI(
    title="Social Media Analytics API",
    description="Backend API for social media analytics tool",
    version="1.0.0"
)

# Configure CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your Next.js frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint for testing
@app.get("/")
async def root():
    return {"message": "Social Media Analytics API is running!"}

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
