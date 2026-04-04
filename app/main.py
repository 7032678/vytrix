from flask import Flask, render_template, request, jsonify
import os
import uuid
from datetime import datetime
import random

app = Flask(__name__)

# Mock data storage (in production, this would be a database)
users = {}
policies = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy", "service": "vytrix-flask"})

@app.route('/api/users/register', methods=['POST'])
def register_user():
    data = request.get_json()

    # Generate user ID
    user_id = f"user_{uuid.uuid4().hex[:8]}"

    # Store user data
    user_data = {
        "user_id": user_id,
        "name": data.get("name"),
        "phone_number": data.get("phone"),
        "delivery_platform": data.get("platform"),
        "vehicle_type": data.get("vehicle"),
        "primary_work_area": data.get("zone"),
        "average_daily_earnings": float(data.get("earnings", 0)),
        "shift": data.get("shift"),
        "risk_score": random.uniform(0.1, 0.9),
        "verification_status": "VERIFIED",
        "created_at": datetime.now().isoformat()
    }

    users[user_id] = user_data

    return jsonify({
        "user_id": user_id,
        "message": "User registered successfully",
        "user": user_data
    })

@app.route('/api/policies/calculate-premium', methods=['POST'])
def calculate_premium():
    data = request.get_json()
    user_id = data.get("user_id")

    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    user = users[user_id]

    # Mock premium calculation
    base_premium = 200.0
    zone_risk = {"urban": 1.2, "suburban": 1.0, "rural": 0.8}.get(user["primary_work_area"], 1.0)
    vehicle_risk = {"bike": 1.0, "scooter": 0.9, "car": 1.3}.get(user["vehicle_type"], 1.0)
    earnings_factor = min(user["average_daily_earnings"] / 1000, 2.0)

    final_premium = base_premium * zone_risk * vehicle_risk * earnings_factor
    coverage_amount = final_premium * 10

    premium_data = {
        "base_premium": round(base_premium, 2),
        "zone_risk_adjustment": round(base_premium * (zone_risk - 1), 2),
        "weather_risk_adjustment": round(base_premium * 0.05, 2),
        "final_premium": round(final_premium, 2),
        "coverage_amount": round(coverage_amount, 2),
        "coverage_type": "parametric",
        "risk_factors": {
            "zone_risk": round(zone_risk - 1, 2),
            "vehicle_risk": round(vehicle_risk - 1, 2),
            "earnings_risk": round(earnings_factor - 1, 2),
            "weather_risk": 0.05
        }
    }

    policies[user_id] = premium_data

    return jsonify(premium_data)

@app.route('/api/simulations/rain', methods=['POST'])
def simulate_rain():
    data = request.get_json()
    user_id = data.get("user_id")

    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    session_id = f"session_{uuid.uuid4().hex[:8]}"

    # Mock rain simulation
    opportunity_score = random.uniform(0.7, 0.95)
    fraud_score = random.uniform(0.05, 0.2)
    threshold = 0.7

    status = "APPROVED" if opportunity_score > threshold and fraud_score < 0.3 else "REJECTED"

    result = {
        "session_id": session_id,
        "opportunity_score": round(opportunity_score, 2),
        "fraud_score": round(fraud_score, 2),
        "status": status,
        "threshold": threshold,
        "reasons": [
            "Heavy rain detected in work area",
            "Activity drop of 65% during rain period",
            "Peer activity correlation confirmed rain impact"
        ] if status == "APPROVED" else [
            "Rain intensity below threshold",
            "Activity drop insufficient for claim"
        ],
        "score_breakdown": {
            "weather": {"score": round(opportunity_score, 2), "weight": 0.4, "contribution": round(opportunity_score * 0.4, 2)},
            "activity_drop": {"score": 0.9, "weight": 0.4, "contribution": 0.36},
            "peer_correlation": {"score": 0.8, "weight": 0.2, "contribution": 0.16}
        },
        "claim_amount": round(policies.get(user_id, {}).get("coverage_amount", 0) * 0.6, 2) if status == "APPROVED" else None,
        "processed_at": datetime.now().isoformat()
    }

    return jsonify(result)

@app.route('/api/simulations/fraud', methods=['POST'])
def simulate_fraud():
    data = request.get_json()
    user_id = data.get("user_id")

    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    session_id = f"session_{uuid.uuid4().hex[:8]}"

    # Mock fraud simulation
    opportunity_score = random.uniform(0.3, 0.6)
    fraud_score = random.uniform(0.8, 0.95)
    threshold = 0.7

    status = "REJECTED"

    result = {
        "session_id": session_id,
        "opportunity_score": round(opportunity_score, 2),
        "fraud_score": round(fraud_score, 2),
        "status": status,
        "threshold": threshold,
        "reasons": [
            "GPS location mismatch detected",
            "Activity pattern inconsistent with weather data",
            "High fraud risk indicators present"
        ],
        "score_breakdown": {
            "location_anomaly": {"score": 0.9, "weight": 0.3, "contribution": 0.27},
            "pattern_inconsistency": {"score": 0.85, "weight": 0.4, "contribution": 0.34},
            "historical_risk": {"score": 0.8, "weight": 0.3, "contribution": 0.24}
        },
        "claim_amount": None,
        "processed_at": datetime.now().isoformat()
    }

    return jsonify(result)

@app.route('/api/simulations/no-activity', methods=['POST'])
def simulate_no_activity():
    data = request.get_json()
    user_id = data.get("user_id")

    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    session_id = f"session_{uuid.uuid4().hex[:8]}"

    # Mock no-activity simulation
    opportunity_score = random.uniform(0.4, 0.7)
    fraud_score = random.uniform(0.1, 0.4)
    threshold = 0.7

    status = "UNDER_REVIEW" if opportunity_score > 0.5 else "REJECTED"

    result = {
        "session_id": session_id,
        "opportunity_score": round(opportunity_score, 2),
        "fraud_score": round(fraud_score, 2),
        "status": status,
        "threshold": threshold,
        "reasons": [
            "No delivery activity recorded during shift",
            "Weather conditions may have impacted operations",
            "Under review for manual verification"
        ] if status == "UNDER_REVIEW" else [
            "Activity level insufficient for claim",
            "No verifiable opportunity loss"
        ],
        "score_breakdown": {
            "activity_level": {"score": round(opportunity_score, 2), "weight": 0.5, "contribution": round(opportunity_score * 0.5, 2)},
            "weather_impact": {"score": 0.6, "weight": 0.3, "contribution": 0.18},
            "platform_data": {"score": 0.7, "weight": 0.2, "contribution": 0.14}
        },
        "claim_amount": None,
        "processed_at": datetime.now().isoformat()
    }

    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)