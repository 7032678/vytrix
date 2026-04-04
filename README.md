# Vytrix Insurance Platform

AI-powered parametric insurance for gig workers.

## ⚠️ Current Status

**Flask application has been completely removed.** The project now contains:
- ✅ **Frontend**: React application (`frontend/` directory)
- ✅ **Database**: SQLite with Alembic migrations (`alembic/`, `vytrix.db`)
- ❌ **Backend**: Needs to be rebuilt (FastAPI or other framework)

## Quick Start

### Frontend Only (Current State)

```bash
cd frontend
npm install
npm start
```

### Full Stack (When Backend is Rebuilt)

1. **Frontend**: `cd frontend && npm install && npm start`
2. **Backend**: Implement FastAPI/Flask server with the existing database models
3. **Database**: Run `alembic upgrade head` to apply migrations

## Project Structure

```
vytrix/
├── frontend/          # React application
├── alembic/           # Database migrations
├── vytrix.db          # SQLite database
├── DEPLOYMENT.md      # Deployment guide
├── docker-compose.yml # Docker setup
├── render.yaml        # Render deployment config
└── test_scenarios.md  # Test cases
```

## Database Models (Available for Backend)

The database contains models for:
- **Users**: Gig worker profiles and risk scores
- **Policies**: Insurance policies and coverage details
- **Claims**: Claim records and assessment results
- **Opportunity Loss**: Activity-based loss calculations
- **Fraud Detection**: ML-powered fraud risk analysis

## Deployment

### Render (Recommended)

1. **Frontend**: Deploy as Static Site from `frontend/` directory
2. **Backend**: Deploy as Web Service (needs to be rebuilt first)

### Docker

Use `docker-compose.yml` for local development once backend is implemented.

## Next Steps

To complete the application:

1. **Rebuild Backend**: Create FastAPI/Flask server using existing database models
2. **Implement APIs**: User registration, premium calculation, simulation endpoints
3. **Connect Frontend**: Update React app to connect to new backend APIs
4. **Test Integration**: Run full-stack tests with simulation scenarios

## Features (When Complete)

- **AI-Powered Risk Assessment**: Machine learning for fraud detection
- **Parametric Insurance**: Weather and activity-based triggers
- **Real-time Simulations**: Rain, fraud, and no-activity scenarios
- **Gig Worker Focus**: Specialized for delivery platforms
- **Multi-platform Support**: Swiggy, Zomato, Uber Eats, DoorDash

- `GET /` - Main application interface
- `GET /api/health` - Health check
- `POST /api/users/register` - Register new user
- `POST /api/policies/calculate-premium` - Calculate insurance premium
- `POST /api/simulations/rain` - Simulate rain scenario claim
- `POST /api/simulations/fraud` - Simulate fraud scenario claim
- `POST /api/simulations/no-activity` - Simulate no-activity scenario claim

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with gradients and animations
- **API**: RESTful JSON API
- **Data Storage**: In-memory (for demo - easily replaceable with database)

## Development

The app replicates the exact UI and functionality of the original React application but uses pure HTML/CSS/JS for simpler deployment. All form validations, state management, and API calls are handled client-side.
