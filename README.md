# Flask Encryption and IP Tracker

**Flask Encryption and IP Tracker** is a web application that provides various utilities, including generating random passwords, encrypting and decrypting messages, and tracking IP addresses. It is built using Flask, SQLAlchemy, and other libraries.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Password Generator**: Generate strong and random passwords of specified lengths.
- **Message Encryption**: Encrypt and securely store messages with a unique key.
- **Message Decryption**: Retrieve and decrypt messages using their corresponding keys.
- **IP Address Tracker**: Track IP addresses and fetch location information using the IP-API service.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed.
- `pip` package manager installed.
- Basic knowledge of Flask web applications.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/flask-encryption-ip-tracker.git
   
Install the project dependencies:
        pip install -r requirements.txt



### Configuration

**Open the app.py file and locate the following line:**
        app.secret_key = 'ghjklkjhgcvbn678"?|>KB'

        Replace the secret key with your own secret key. A strong secret key is essential for session security.


### Usage

1. Start the Flask application:**
        python app.py

    The application will be accessible in your web browser at http://localhost:5000.

2. Explore the following features:

    - Generate Password: Create random passwords with custom lengths.
    - Encrypt Message: Securely store messages with a unique key.
    - Decrypt Message: Retrieve and decrypt messages using their corresponding keys.
    - IP Tracker: Track IP addresses and fetch location information using the IP-API service.


### Contributing

**Contributions to this project are welcome! If you'd like to contribute**


### License

**This project is licensed under the MIT License. See the LICENSE file for details.**









