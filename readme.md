# Insighto Backend - AI-Powered Social Media Analytics API

The backend API for **Insighto** - an AI-automated social media analytics platform. This robust Python backend handles data collection, processing, AI analytics, and provides RESTful APIs for the frontend application.

## 🚀 Features

### 📊 Social Media Data Collection
- **Multi-Platform Integration**: Instagram, Twitter/X, YouTube, TikTok, LinkedIn APIs
- **Real-time Data Sync**: Automated data collection with configurable intervals
- **Rate Limiting**: Smart API rate limit management and queuing
- **Data Validation**: Comprehensive data validation and sanitization
- **Historical Data**: Efficient storage and retrieval of historical metrics

### 🤖 AI & Machine Learning
- **Content Performance Prediction**: ML models for engagement prediction
- **Sentiment Analysis**: AI-powered comment and mention sentiment analysis
- **Trend Detection**: Algorithm-based trend identification and forecasting
- **Audience Segmentation**: ML-driven audience analysis and categorization
- **Competitive Intelligence**: AI-powered competitor benchmarking
- **Recommendation Engine**: Personalized content and strategy recommendations

### 🔐 Security & Authentication
- **JWT Authentication**: Secure token-based authentication system
- **OAuth Integration**: Social media platform OAuth flows
- **API Key Management**: Secure API key generation and validation
- **Role-Based Access Control**: Granular permissions and user roles
- **Data Encryption**: End-to-end encryption for sensitive data

### 📈 Analytics & Processing
- **Real-time Metrics**: Live calculation of engagement metrics
- **Batch Processing**: Efficient bulk data processing with Celery
- **Custom Reports**: Dynamic report generation and export
- **Data Aggregation**: Advanced data aggregation and analytics
- **Performance Monitoring**: System performance tracking and alerts

## 🛠️ Tech Stack

### Core Framework
- **[FastAPI](https://fastapi.tiangolo.com/)**: Modern, fast web framework for building APIs
- **[Python 3.11+](https://python.org/)**: Latest Python with enhanced performance
- **[Pydantic](https://pydantic-docs.helpmanual.io/)**: Data validation using Python type annotations
- **[SQLAlchemy](https://sqlalchemy.org/)**: SQL toolkit and ORM
- **[Alembic](https://alembic.sqlalchemy.org/)**: Database migration tool

### Database & Caching
- **[PostgreSQL](https://postgresql.org/)**: Primary relational database
- **[Redis](https://redis.io/)**: Caching and session storage
- **[MongoDB](https://mongodb.com/)**: Document storage for unstructured data (optional)

### AI & Machine Learning
- **[OpenAI API](https://openai.com/api/)**: GPT models for content analysis
- **[scikit-learn](https://scikit-learn.org/)**: Machine learning library
- **[pandas](https://pandas.pydata.org/)**: Data manipulation and analysis
- **[numpy](https://numpy.org/)**: Numerical computing
- **[TensorFlow](https://tensorflow.org/)**: Deep learning framework
- **[NLTK](https://nltk.org/)**: Natural language processing

### Task Queue & Background Jobs
- **[Celery](https://celeryproject.org/)**: Distributed task queue
- **[Redis/RabbitMQ](https://rabbitmq.com/)**: Message broker for Celery
- **[Flower](https://flower.readthedocs.io/)**: Celery monitoring tool

### Monitoring & Logging
- **[Prometheus](https://prometheus.io/)**: Metrics collection
- **[Grafana](https://grafana.com/)**: Metrics visualization
- **[Sentry](https://sentry.io/)**: Error tracking and performance monitoring
- **[Structlog](https://structlog.org/)**: Structured logging

## 📋 Prerequisites

- **Python**: 3.11 or higher
- **PostgreSQL**: 15 or higher
- **Redis**: 7 or higher
- **Docker & Docker Compose**: Latest version (optional but recommended)

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/insighto-backend.git
cd insighto-backend
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the root directory:

```env
# Application Settings
APP_NAME=Insighto Backend
APP_VERSION=1.0.0
DEBUG=True
ENVIRONMENT=development
SECRET_KEY=your-super-secret-key-here
API_V1_PREFIX=/api/v1

# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/insighto
DATABASE_TEST_URL=postgresql://username:password@localhost:5432/insighto_test

# Redis Configuration
REDIS_URL=redis://localhost:6379/0
REDIS_CACHE_TTL=3600

# JWT Configuration
JWT_SECRET_KEY=your-jwt-secret-key
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
REFRESH_TOKEN_EXPIRATION_DAYS=30

# Social Media API Keys
INSTAGRAM_CLIENT_ID=your-instagram-client-id
INSTAGRAM_CLIENT_SECRET=your-instagram-client-secret
INSTAGRAM_REDIRECT_URI=http://localhost:3000/auth/instagram/callback

TWITTER_API_KEY=your-twitter-api-key
TWITTER_API_SECRET=your-twitter-api-secret
TWITTER_ACCESS_TOKEN=your-twitter-access-token
TWITTER_ACCESS_TOKEN_SECRET=your-twitter-access-token-secret
TWITTER_BEARER_TOKEN=your-twitter-bearer-token

YOUTUBE_API_KEY=your-youtube-api-key
YOUTUBE_CLIENT_ID=your-youtube-client-id
YOUTUBE_CLIENT_SECRET=your-youtube-client-secret

TIKTOK_CLIENT_ID=your-tiktok-client-id
TIKTOK_CLIENT_SECRET=your-tiktok-client-secret

LINKEDIN_CLIENT_ID=your-linkedin-client-id
LINKEDIN_CLIENT_SECRET=your-linkedin-client-secret

# AI Services
OPENAI_API_KEY=your-openai-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key
HUGGINGFACE_API_KEY=your-huggingface-api-key

# Email Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
FROM_EMAIL=noreply@insighto.com

# Celery Configuration
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/2

# Monitoring
SENTRY_DSN=your-sentry-dsn
PROMETHEUS_MULTIPROC_DIR=/tmp/prometheus_multiproc_dir

# File Storage
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=16777216  # 16MB
ALLOWED_EXTENSIONS=jpg,jpeg,png,gif,mp4,mov,avi

# Rate Limiting
RATE_LIMIT_PER_MINUTE=60
RATE_LIMIT_PER_HOUR=1000
RATE_LIMIT_PER_DAY=10000
```

### 5. Database Setup

```bash
# Start PostgreSQL and Redis (if not using Docker)
# PostgreSQL: brew services start postgresql (macOS) or sudo systemctl start postgresql (Linux)
# Redis: brew services start redis (macOS) or sudo systemctl start redis (Linux)

# Run database migrations
alembic upgrade head

# Seed database with initial data (optional)
python scripts/seed_database.py
```

### 6. Start the Development Server

```bash
# Start the main application
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# In another terminal, start Celery worker
celery -A app.core.celery worker --loglevel=info

# In another terminal, start Celery beat (for scheduled tasks)
celery -A app.core.celery beat --loglevel=info

# Optional: Start Flower for Celery monitoring
celery -A app.core.celery flower --port=5555
```

The API will be available at `http://localhost:8000`
API documentation will be available at `http://localhost:8000/docs`

## 🐳 Docker Setup

### Development with Docker Compose

```bash
# Build and start all services
docker-compose up --build

# Run in detached mode
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Production Docker

```bash
# Build production image
docker build -f Dockerfile.prod -t insighto-backend:latest .

# Run with environment variables
docker run -p 8000:8000 --env-file .env insighto-backend:latest
```

## 📁 Project Structure

```
insighto-backend/
├── app/
│   ├── api/                    # API route handlers
│   │   ├── v1/                # API version 1
│   │   │   ├── endpoints/     # API endpoints
│   │   │   │   ├── auth.py    # Authentication endpoints
│   │   │   │   ├── users.py   # User management
│   │   │   │   ├── analytics.py # Analytics endpoints
│   │   │   │   ├── social_accounts.py # Social media accounts
│   │   │   │   └── insights.py # AI insights endpoints
│   │   │   └── api.py         # API router
│   │   └── deps.py            # API dependencies
│   ├── core/                  # Core application logic
│   │   ├── config.py          # Application configuration
│   │   ├── security.py        # Security utilities
│   │   ├── database.py        # Database configuration
│   │   ├── redis.py           # Redis configuration
│   │   ├── celery.py          # Celery configuration
│   │   └── logging.py         # Logging configuration
│   ├── models/                # SQLAlchemy models
│   │   ├── user.py           # User model
│   │   ├── social_account.py # Social media account model
│   │   ├── analytics.py      # Analytics data models
│   │   └── insights.py       # AI insights models
│   ├── schemas/               # Pydantic schemas
│   │   ├── user.py           # User schemas
│   │   ├── auth.py           # Authentication schemas
│   │   ├── analytics.py      # Analytics schemas
│   │   └── social_media.py   # Social media schemas
│   ├── services/              # Business logic services
│   │   ├── auth_service.py   # Authentication service
│   │   ├── user_service.py   # User management service
│   │   ├── analytics_service.py # Analytics processing
│   │   ├── ai_service.py     # AI/ML services
│   │   └── social_media/     # Social media integrations
│   │       ├── instagram.py  # Instagram API integration
│   │       ├── twitter.py    # Twitter API integration
│   │       ├── youtube.py    # YouTube API integration
│   │       └── base.py       # Base social media class
│   ├── tasks/                 # Celery tasks
│   │   ├── data_collection.py # Social media data collection
│   │   ├── analytics.py      # Analytics processing tasks
│   │   ├── ai_processing.py  # AI/ML processing tasks
│   │   └── notifications.py  # Notification tasks
│   ├── utils/                 # Utility functions
│   │   ├── validators.py     # Data validation utilities
│   │   ├── helpers.py        # General helper functions
│   │   ├── decorators.py     # Custom decorators
│   │   └── exceptions.py     # Custom exceptions
│   ├── ml/                    # Machine learning models
│   │   ├── models/           # Trained ML models
│   │   ├── preprocessing.py  # Data preprocessing
│   │   ├── training.py       # Model training scripts
│   │   └── prediction.py     # Prediction utilities
│   └── main.py               # FastAPI application factory
├── alembic/                   # Database migrations
│   ├── versions/             # Migration versions
│   ├── env.py               # Alembic environment
│   └── alembic.ini          # Alembic configuration
├── tests/                     # Test suite
│   ├── api/                  # API tests
│   ├── services/             # Service tests
│   ├── models/               # Model tests
│   └── conftest.py          # Test configuration
├── scripts/                   # Utility scripts
│   ├── seed_database.py      # Database seeding
│   ├── train_models.py       # ML model training
│   └── backup_database.py    # Database backup
├── docker/                    # Docker configurations
│   ├── Dockerfile.dev        # Development Dockerfile
│   ├── Dockerfile.prod       # Production Dockerfile
│   └── docker-compose.yml    # Docker Compose configuration
├── requirements/              # Python dependencies
│   ├── base.txt             # Base requirements
│   ├── dev.txt              # Development requirements
│   └── prod.txt             # Production requirements
├── .env.example              # Environment variables example
├── requirements.txt          # All dependencies
├── pyproject.toml           # Project configuration
└── README.md                # This file
```

## 🔌 API Endpoints

### Authentication
```http
POST   /api/v1/auth/register          # User registration
POST   /api/v1/auth/login             # User login
POST   /api/v1/auth/refresh           # Refresh JWT token
POST   /api/v1/auth/logout            # User logout
POST   /api/v1/auth/forgot-password   # Password reset request
POST   /api/v1/auth/reset-password    # Password reset confirmation
```

### User Management
```http
GET    /api/v1/users/me               # Get current user profile
PUT    /api/v1/users/me               # Update user profile
DELETE /api/v1/users/me               # Delete user account
GET    /api/v1/users/me/settings      # Get user settings
PUT    /api/v1/users/me/settings      # Update user settings
```

### Social Media Accounts
```http
GET    /api/v1/social-accounts        # Get connected accounts
POST   /api/v1/social-accounts        # Connect new account
PUT    /api/v1/social-accounts/{id}   # Update account settings
DELETE /api/v1/social-accounts/{id}   # Disconnect account
POST   /api/v1/social-accounts/{id}/sync # Force sync account data
```

### Analytics
```http
GET    /api/v1/analytics/overview     # Dashboard overview
GET    /api/v1/analytics/metrics      # Detailed metrics
GET    /api/v1/analytics/performance  # Performance analytics
GET    /api/v1/analytics/audience     # Audience insights
GET    /api/v1/analytics/competitors  # Competitor analysis
GET    /api/v1/analytics/trends       # Trending content
POST   /api/v1/analytics/reports      # Generate custom reports
```

### AI Insights
```http
GET    /api/v1/insights               # Get AI insights
POST   /api/v1/insights/generate      # Generate new insights
GET    /api/v1/insights/recommendations # Get recommendations
POST   /api/v1/insights/predict       # Predict content performance
GET    /api/v1/insights/sentiment     # Sentiment analysis results
```

### Data Management
```http
POST   /api/v1/data/import            # Import data
POST   /api/v1/data/export            # Export data
GET    /api/v1/data/status            # Get sync status
POST   /api/v1/data/refresh           # Force data refresh
```

## 🤖 AI & Machine Learning

### Content Performance Prediction
```python
# Example usage in services/ai_service.py
from app.ml.prediction import ContentPerformancePredictor

predictor = ContentPerformancePredictor()
predicted_engagement = predictor.predict(
    content_text="Your social media post content",
    platform="instagram",
    user_id=user_id,
    posting_time=datetime.now()
)
```

### Sentiment Analysis
```python
from app.services.ai_service import SentimentAnalyzer

analyzer = SentimentAnalyzer()
sentiment_score = analyzer.analyze_sentiment(
    text="User comment or post content",
    context="comment"  # or "post", "mention"
)
```

### Trend Detection
```python
from app.ml.models.trend_detector import TrendDetector

detector = TrendDetector()
trending_topics = detector.detect_trends(
    platform="twitter",
    time_range="24h",
    user_industry="technology"
)
```

## 🔄 Background Tasks

### Celery Tasks

```python
# Data collection task
@celery.task(bind=True)
def sync_social_media_data(self, user_id: int, platform: str):
    """Sync social media data for a user"""
    # Implementation

# Analytics processing task  
@celery.task(bind=True)
def process_analytics(self, user_id: int, date_range: str):
    """Process analytics data"""
    # Implementation

# AI insights generation task
@celery.task(bind=True)
def generate_ai_insights(self, user_id: int):
    """Generate AI insights for user"""
    # Implementation
```

### Scheduled Tasks
```python
# Periodic tasks configuration
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'sync-all-accounts': {
        'task': 'app.tasks.data_collection.sync_all_accounts',
        'schedule': crontab(minute='*/30'),  # Every 30 minutes
    },
    'generate-daily-insights': {
        'task': 'app.tasks.ai_processing.generate_daily_insights',
        'schedule': crontab(hour=9, minute=0),  # Daily at 9 AM
    },
    'cleanup-old-data': {
        'task': 'app.tasks.maintenance.cleanup_old_data',
        'schedule': crontab(hour=2, minute=0),  # Daily at 2 AM
    },
}
```

## 📊 Database Schema

### Key Models

```python
# User Model
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    subscription_plan = Column(String, default="free")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

# Social Account Model
class SocialAccount(Base):
    __tablename__ = "social_accounts"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    platform = Column(String)  # instagram, twitter, youtube, etc.
    account_id = Column(String)
    username = Column(String)
    access_token = Column(String)
    refresh_token = Column(String)
    token_expires_at = Column(DateTime)
    is_active = Column(Boolean, default=True)
    last_sync_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

# Analytics Data Model
class AnalyticsData(Base):
    __tablename__ = "analytics_data"
    
    id = Column(Integer, primary_key=True)
    social_account_id = Column(Integer, ForeignKey("social_accounts.id"))
    metric_type = Column(String)  # followers, engagement, reach, etc.
    metric_value = Column(Float)
    date = Column(Date)
    metadata = Column(JSON)  # Additional platform-specific data
    created_at = Column(DateTime, default=datetime.utcnow)
```

## 🚀 Available Scripts

| Command | Description |
|---------|-------------|
| `python -m uvicorn app.main:app --reload` | Start development server |
| `alembic upgrade head` | Run database migrations |
| `alembic revision --autogenerate -m "message"` | Create new migration |
| `celery -A app.core.celery worker --loglevel=info` | Start Celery worker |
| `celery -A app.core.celery beat --loglevel=info` | Start Celery beat scheduler |
| `celery -A app.core.celery flower` | Start Flower monitoring |
| `python -m pytest` | Run test suite |
| `python -m pytest --cov=app` | Run tests with coverage |
| `python scripts/seed_database.py` | Seed database with test data |
| `python scripts/train_models.py` | Train ML models |
| `black app/` | Format code with Black |
| `isort app/` | Sort imports |
| `flake8 app/` | Lint code |
| `mypy app/` | Type checking |

## 🧪 Testing

```bash
# Install test dependencies
pip install -r requirements/dev.txt

# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=app --cov-report=html

# Run specific test file
python -m pytest tests/api/test_auth.py

# Run tests with verbose output
python -m pytest -v

# Run tests in parallel
python -m pytest -n auto
```

### Test Structure
```python
# Example test file: tests/api/test_auth.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "password": "testpass123",
            "full_name": "Test User"
        }
    )
    assert response.status_code == 201
    assert "access_token" in response.json()
```

## 🚢 Deployment

### Production Environment

```bash
# Install production dependencies
pip install -r requirements/prod.txt

# Set environment to production
export ENVIRONMENT=production
export DEBUG=False

# Start with Gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Docker Production

```dockerfile
# Dockerfile.prod
FROM python:3.11-slim

WORKDIR /app

COPY requirements/prod.txt .
RUN pip install --no-cache-dir -r prod.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "app.main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
```

### Database Migrations

```bash
# Create new migration
alembic revision --autogenerate -m "Add new table"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1

# Show current revision
alembic current

# Show migration history
alembic history
```

## 📈 Monitoring & Performance

### Metrics Collection
- **Request/Response metrics**: Automatically collected by FastAPI
- **Database query performance**: SQLAlchemy query logging
- **Celery task monitoring**: Task execution times and success rates
- **Cache hit/miss ratios**: Redis performance metrics
- **Custom business metrics**: User engagement, API usage, etc.

### Health Checks
```python
@app.get("/health")
async def health_check():
    """Health check endpoint for load balancers"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow(),
        "version": app.version,
        "database": await check_database_connection(),
        "redis": await check_redis_connection(),
        "celery": check_celery_worker_status()
    }
```

### Performance Optimization
- **Database connection pooling**: SQLAlchemy connection pool configuration
- **Query optimization**: Database indexing and query analysis
- **Caching strategy**: Redis caching for frequently accessed data
- **Async operations**: Async/await for I/O bound operations
- **Background processing**: Celery for heavy computational tasks

## 🔐 Security Best Practices

### Authentication & Authorization
- **JWT tokens**: Secure token-based authentication
- **Password hashing**: Bcrypt for password security
- **Rate limiting**: API rate limiting to prevent abuse
- **CORS configuration**: Proper cross-origin resource sharing setup
- **API key validation**: Secure API key management

### Data Protection
- **Input validation**: Pydantic schemas for request validation
- **SQL injection prevention**: SQLAlchemy ORM usage
- **XSS protection**: Input sanitization
- **Data encryption**: Sensitive data encryption at rest
- **Audit logging**: Comprehensive audit trail

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Development Workflow
1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Install development dependencies**: `pip install -r requirements/dev.txt`
4. **Write tests** for your changes
5. **Run the test suite**: `pytest`
6. **Format code**: `black app/` and `isort app/`
7. **Lint code**: `flake8 app/`
8. **Commit changes**: `git commit -m 'Add amazing feature'`
9. **Push to branch**: `git push origin feature/amazing-feature`
10. **Open a Pull Request**

### Code Style
- Follow **PEP 8** style guidelines
- Use **type hints** for all function parameters and return values
- Write **docstrings** for all public functions and classes
- Maintain **test coverage** above 85%
- Use **meaningful variable names**

### Pre-commit Hooks
```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support & Documentation

- **API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)
- **Alternative API Docs**: [http://localhost:8000/redoc](http://localhost:8000/redoc) (ReDoc)
- **Issues**: [GitHub Issues](https://github.com/your-username/insighto-backend/issues)
- **Wiki**: [GitHub Wiki](https://github.com/your-username/insighto-backend/wiki)
- **Email**: developers@insighto.com
- **Slack**: [Join our developer channel](https://insighto-dev.slack.com)

## 🎯 Roadmap

### Current Version (v1.0.0)
- [x] Core API endpoints
- [x] Social media integrations (Instagram, Twitter, YouTube)
- [x] Basic AI insights
- [x] User authentication
- [x] Real-time analytics

### Upcoming Features (v1.1.0)
- [ ] TikTok API integration
- [ ] LinkedIn Business API integration
- [ ] Advanced ML models for content optimization
- [ ] Webhook support for real-time updates
- [ ] GraphQL API support
- [ ] Advanced caching strategies

### Future Versions
- [ ] Microservices architecture
- [ ] Kubernetes deployment support
- [ ] Advanced AI content generation
- [ ] Multi-tenant support
- [ ] Real-time collaboration features
- [ ] Mobile SDK development

---

**Built with 🐍 Python and ❤️ by the Insighto Team**

For more information about the backend architecture and API usage, please refer to our [API documentation](http://localhost:8000/docs) and [developer wiki](https://github.com/your-username/insighto-backend/wiki).