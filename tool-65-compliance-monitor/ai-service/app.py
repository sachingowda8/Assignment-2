import re
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from services.groq_client import GroqClient

app = Flask(__name__)

# Day 3: Security - Rate Limiting (30 requests per minute)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"],
    storage_uri="memory://"
)

client = GroqClient()

def sanitize_input(text):
    """Clean input to prevent basic prompt injection."""
    # Remove common injection characters
    return re.sub(r'[<>{}\[\]]', '', text)

@app.route('/api/analyze', methods=['POST'])
@limiter.limit("5 per minute") # Extra strict for the heavy AI route
def analyze_compliance():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
        
    user_input = data.get('query', '')
    
    # Security Check: Input Sanitization
    clean_input = sanitize_input(user_input)
    
    if not clean_input:
        return jsonify({"error": "Invalid or empty input"}), 400

    try:
        # Prompt Tuning for Sustainability Compliance
        system_prompt = "You are a Sustainability Compliance Expert. Analyze the following query for ESG compliance rules."
        response = client.get_completion(clean_input, system_prompt=system_prompt)
        
        return jsonify({
            "status": "success",
            "analysis": response
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Using 5001 to avoid potential conflicts with other services
    app.run(port=5001, debug=True)
