# OnKeyPress

OnKeyPress is a Keylogging program that tracks a person's keyboard input and sends the recorded keys to another person via remote connection.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages ,namely, socket(to create a remote connection) and pynput(to get the keypresses).

```bash
pip install socket
```
```bash
pip install pynput
```

## Usage
Firstly ,start the **server.py** file on your terminal using the command 
```
python3 server.py
```
Simultaneously ,run the **keylogger.py** on another instance of your terminal using the command :
```
python3 keylogger.py
```
## Output

<img src="https://github.com/CosmosElement77/KeyLogger/blob/c1fda6cdf8c5d855ddfcdc42904ecce65a80cbb6/first.png" width="200" height="200">
<img src="https://github.com/CosmosElement77/KeyLogger/blob/c1fda6cdf8c5d855ddfcdc42904ecce65a80cbb6/second.png" width="200" height="200">






