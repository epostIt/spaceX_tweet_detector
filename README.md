# SpaceX Tweet Detector

This is a fun side project to get practice with the OpenAI API and hosting on a Raspberry Pi. The project analyzes Elon Musk's tweets to determine if they are related to SpaceX. If a tweet is identified as related by GPT3.5, it sends an SMS notification using Twilio. SpaceX related tweets only, please!

## Prerequisites

To run this project, you need to have accounts and API keys for the following services:

1. **OpenAI**: For analyzing the tweet content.
2. **Twilio**: For sending SMS notifications.

### Setting Up Accounts

1. **OpenAI**:
   - Sign up at [OpenAI](https://beta.openai.com/signup/).
   - Create an API key and set it as the `OPENAI_API_KEY` in the `.env` file.
   - Note: You do have to buy tokens, but I tried to make it as cheap as possible and have sent over 100 requests for less than a cent.

2. **Twilio**:
   - Sign up at [Twilio](https://www.twilio.com/try-twilio).
   - Get your Account SID and Auth Token from the Twilio Console and set them as `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` in the `.env` file.
   - Get your Twilio phone number and set it as `TWILIO_PHONE_NUMBER` in the `.env` file.
   - Set your personal phone number as `MY_PHONE_NUMBER` in the `.env` file to receive SMS notifications.
   - Note: Twilio gives you $15 free credit to play with when you sign up for a new account.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/epostIt/spaceX_tweet_detector.git
cd spacex-tweet-detector
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use .\venv\Scripts\activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your environment variables:

```bash
touch .env
# Add your environment variables here as shown below
```

### Environment Variables

You need to set up the following environment variables in a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
MY_PHONE_NUMBER=your_phone_number
```

## Running the Application

To run the application:

```bash
python main.py
```

## Running Tests

To run the tests, you can use `unittest`. Note: These tests were generated with the help of AI and might not be fully robust. Please review and modify them as necessary.

```bash
python -m unittest discover -s test
```

Alternatively, if you have `pytest` installed, you can run:

```bash
pytest
```

## Disclaimer

The tests included in this project were written by an AI assistant. While efforts have been made to ensure their accuracy, they might not cover all edge cases or scenarios. It's recommended to review and enhance the tests for robustness as needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
