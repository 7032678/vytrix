# Vytrix Insurance Platform

AI-powered parametric insurance for gig workers.

## Project Structure

This project contains:
- **Frontend**: React application (`frontend/` directory)
- **Backend**: FastAPI application (database models, services, and schemas)
- **Deployment**: Configuration files for Render, Docker, and other platforms

## Frontend (React)

The React frontend provides a complete user interface for:
- User registration and profile management
- Premium calculation and policy management
- Claim simulation scenarios (rain, fraud, no-activity)
- Results display with AI-powered assessments

### Running the Frontend

```bash
cd frontend
npm install
npm start
```

## Backend (FastAPI)

The backend includes:
- User management and authentication
- Policy and premium calculation services
- Fraud detection and opportunity loss analysis
- Simulation engines for different scenarios

### Database

The project uses SQLite with Alembic for migrations:
- Database file: `vytrix.db`
- Migrations: `alembic/` directory
- Models: User, Policy, Claim, etc.

## Deployment

### Render Deployment

1. Connect your GitHub repo to Render
2. Deploy the frontend as a Static Site
3. Deploy the backend as a Web Service

### Docker

Use `docker-compose.yml` for local development with all services.

## Development

1. **Frontend**: `cd frontend && npm install && npm start`
2. **Backend**: Set up Python environment and run FastAPI server
3. **Database**: Run `alembic upgrade head` to apply migrations

## Features

- **AI-Powered Risk Assessment**: Machine learning models for fraud detection
- **Parametric Insurance**: Weather-based and activity-based claim triggers
- **Real-time Simulations**: Test different claim scenarios
- **Gig Worker Focus**: Specialized for delivery platform workers
- **Multi-platform Support**: Swiggy, Zomato, Uber Eats, DoorDash

## API Documentation

FastAPI provides automatic API documentation at `/docs` when running the backend server.

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
