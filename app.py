from flask import Flask, jsonify
from blockchain import *

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def home():
    """
    Flask route to display a welcome message.
    """
    return jsonify({'message': 'Welcome to the Blockchain API'}), 200

@app.route('/mine_block', methods=['GET'])
def mine_block():
    """
    Flask route to mine a new block.
    """
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    
    response = {
        'message': 'A new block has been mined!',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200

@app.route('/get_chain', methods=['GET'])
def display_chain():
    """
    Flask route to display the entire blockchain.
    """
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

@app.route('/valid', methods=['GET'])
def valid():
    """
    Flask route to validate the blockchain.
    """
    is_valid = blockchain.chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'The blockchain is valid.'}
    else:
        response = {'message': 'The blockchain is not valid.'}
    
    return jsonify(response), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request'}), 400

if __name__ == "__main__":
    app.run()
        
