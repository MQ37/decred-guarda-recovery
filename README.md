This repo will help you recover your [Decred](https://decred.org/) funds from [Guarda](https://guarda.co/) wallet private key export using [Exodus](https://www.exodus.io/) wallet and simple Python script to convert the Guarda base58 encoded private key to WIF key.

# Steps

1. Export your private key from Guarda wallet
- Go to your wallet
- Click on your Decred wallet
- Click on the three dots on the top right corner
- Click on "Export Private Key"
- See [Guarda support article](https://support.guarda.com/article/68-how-to-save-your-private-keys) for more details
2. Clone this repo and run the Python script
- Create Python virtual environment
```
# Linux / MacOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```
- Install the required packages
```
pip install -r requirements.txt
```
- Run the script
```
python convert.py
```
3. Input the Guarda private key and it should output WIF key that can be used to move funds to Decred Exodus wallet
4. Install Exodus desktop wallet
5. Select Decred wallet, click on the three dots on the top right corner and click on "Move Funds"
- See [Exodus video tutorial](https://youtu.be/12f9SxnXRaQ?feature=shared&t=115) or [Exodus support article](https://www.exodus.com/support/en/articles/8598622-how-do-i-import-a-private-key) for more details

Now that you have your funds in Exodus wallet, you can move them to any other wallet or exchange.

# Sources
- [https://www.reddit.com/r/decred/comments/18s54fm/help_importing_a_private_key/](https://www.reddit.com/r/decred/comments/18s54fm/help_importing_a_private_key/)

