"""
A simple implementation of blockchain in Python.
"""
import time
import hashlib
import json

class Blockchain:
    """
    A Class to represent a simple blockchain.
    """
    def __init__(self, difficulty=4):
        """
        Initializes the blockchain with an empty chain, sets the mining difficulty, and creates the genesis block.
        """
        self.chain = []  # List to store the blocks of the blockchain
        self.difficulty = difficulty  # Difficulty level for proof-of-work
        self.create_block(proof=1, previous_hash='0')  # Creating the genesis block
    
    def create_block(self, proof, previous_hash):
        """
        Creates a new block and adds it to the blockchain.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block
    
    def print_previous_block(self):
        """
        Returns the last block in the blockchain.
        """
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        """
        Implements the Proof-of-Work algorithm to find a valid proof based on the difficulty level.
        """
        new_proof = 1
        check_proof = False
        
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:self.difficulty] == "0" * self.difficulty:
                check_proof = True
            else:
                new_proof += 1
        
        return new_proof
    
    def hash(self, block):
        """
        Hashes a block into a unique fingerprint.
        """
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def chain_valid(self, chain):
        """
        Validates the blockchain to ensure integrity.
        """
        previous_block = chain[0]
        current_index = 1
        
        while current_index < len(chain):
            block = chain[current_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            
            previous_proof = previous_block['proof']
            current_proof = block['proof']
            hash_operation = hashlib.sha256(str(current_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:self.difficulty] != "0" * self.difficulty:
                return False
            
            previous_block = block
            current_index += 1
        
        return True
