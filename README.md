# Simple BlockChain

## Overview

This project is a simple blockchain implementation in Python, featuring proof-of-work, block creation, validation, and a Flask API for interaction. It includes a mining difficulty parameter to control block mining complexity.

## Features

- Blockchain creation and management
- Proof-of-Work for mining blocks
- Blockchain validation
- Flask API for interaction

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/lokk798/Simple-BlockChain.git
   cd simple-blockchain
   ```
2. Install dependencies:
   ```sh
   pip install flask
   ```
3. Run the application:
   ```sh
   python app.py
   ```

## API Endpoints

- **`GET /`** → Welcome message
- **`GET /mine_block`** → Mines a new block
- **`GET /get_chain`** → Retrieves the full blockchain
- **`GET /valid`** → Checks if the blockchain is valid
