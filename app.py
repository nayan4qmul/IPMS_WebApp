from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data - in a real app, this would be a database
policies = [
    {
        'id': 1,
        'policy_number': 'POL001',
        'customer_name': 'John Doe',
        'policy_type': 'Auto',
        'premium': 1200.00,
        'status': 'Active',
        'coverage_amount': 50000.00
    },
    {
        'id': 2,
        'policy_number': 'POL002',
        'customer_name': 'Jane Smith',
        'policy_type': 'Home',
        'premium': 800.00,
        'status': 'Active',
        'coverage_amount': 250000.00
    },
    {
        'id': 3,
        'policy_number': 'POL003',
        'customer_name': 'Bob Johnson',
        'policy_type': 'Life',
        'premium': 1500.00,
        'status': 'Pending',
        'coverage_amount': 1000000.00
    }
]

claims = [
    {
        'id': 1,
        'claim_number': 'CLM001',
        'policy_number': 'POL001',
        'customer_name': 'John Doe',
        'claim_type': 'Collision',
        'amount': 5000.00,
        'status': 'Under Review',
        'date_filed': '2024-01-15'
    },
    {
        'id': 2,
        'claim_number': 'CLM002',
        'policy_number': 'POL002',
        'customer_name': 'Jane Smith',
        'claim_type': 'Theft',
        'amount': 15000.00,
        'status': 'Approved',
        'date_filed': '2024-01-10'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/policies')
def show_policies():
    return render_template('policies.html', policies=policies)

@app.route('/claims')
def show_claims():
    return render_template('claims.html', claims=claims)

@app.route('/api/policies', methods=['GET'])
def get_policies():
    return jsonify(policies)

@app.route('/api/policies/<int:policy_id>', methods=['GET'])
def get_policy(policy_id):
    policy = next((p for p in policies if p['id'] == policy_id), None)
    if policy:
        return jsonify(policy)
    return jsonify({'error': 'Policy not found'}), 404

@app.route('/api/claims', methods=['GET'])
def get_claims():
    return jsonify(claims)

@app.route('/api/policies', methods=['POST'])
def create_policy():
    new_policy = {
        'id': len(policies) + 1,
        'policy_number': request.json.get('policy_number'),
        'customer_name': request.json.get('customer_name'),
        'policy_type': request.json.get('policy_type'),
        'premium': request.json.get('premium'),
        'status': 'Active',
        'coverage_amount': request.json.get('coverage_amount')
    }
    policies.append(new_policy)
    return jsonify(new_policy), 201

@app.route('/api/claims', methods=['POST'])
def create_claim():
    new_claim = {
        'id': len(claims) + 1,
        'claim_number': request.json.get('claim_number'),
        'policy_number': request.json.get('policy_number'),
        'customer_name': request.json.get('customer_name'),
        'claim_type': request.json.get('claim_type'),
        'amount': request.json.get('amount'),
        'status': 'Under Review',
        'date_filed': request.json.get('date_filed')
    }
    claims.append(new_claim)
    return jsonify(new_claim), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)