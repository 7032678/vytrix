# Vytrix Insurance Platform (Flask)

AI-powered parametric insurance for gig workers - now built with Flask for easy deployment.

## Quick Start

1. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python run.py
   ```

4. Open http://localhost:5000 in your browser.

## Deploy to Render

1. Connect your GitHub repo to Render.
2. Create a new Web Service.
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python run.py`
5. Render will automatically detect Flask and set the PORT environment variable.

## Features

- **Multi-page Interface**: Complete user flow with registration, premium display, simulation testing, and results
- **User Registration**: Collect gig worker details (name, phone, zone, shift, platform, vehicle, earnings)
- **Premium Calculation**: AI-powered premium calculation based on risk factors
- **Simulation Scenarios**: Test different claim scenarios (rain, fraud, no-activity)
- **Results Display**: Detailed claim assessment with scores and status
- **Responsive Design**: Mobile-friendly interface matching the original React app
- **REST API**: Clean API endpoints for all functionality

## User Flow

1. **Registration Page**: User enters personal and work details
2. **Premium Page**: Displays calculated monthly premium and coverage amount
3. **Trigger Page**: Choose from simulation scenarios to test claims
4. **Results Page**: View AI assessment results with opportunity loss and fraud scores

## API Endpoints

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
