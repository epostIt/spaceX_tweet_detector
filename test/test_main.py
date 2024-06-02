import sys
import os
import unittest
from unittest.mock import patch, MagicMock
from main import (
    get_GPT_determination,
    format_response,
    is_affirmative,
    is_about_spacex,
    get_most_recent_tweet,
    get_elon_musk_tweets,
    send_sms
)
from setup_clients import setup_clients

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.twilio_client = MagicMock()
        self.twilio_phone_number = "your_twilio_number"
        self.my_phone_number = "your_phone_number"
        
    @patch('main.get_GPT_determination')
    @patch('main.openAI_client', new_callable=MagicMock)
    def test_is_about_spacex_yes(self, mock_openAI_client, mock_get_GPT_determination):
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "yes"
        mock_get_GPT_determination.return_value = mock_response
        self.assertTrue(is_about_spacex("This is a test tweet"))

    @patch('main.get_GPT_determination')
    @patch('main.openAI_client', new_callable=MagicMock)
    def test_is_about_spacex_no(self, mock_openAI_client, mock_get_GPT_determination):
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "no"
        mock_get_GPT_determination.return_value = mock_response
        self.assertFalse(is_about_spacex("This is a test tweet"))

    def test_format_response(self):
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Yes"
        self.assertEqual(format_response(mock_response), "yes")

    def test_is_affirmative(self):
        self.assertTrue(is_affirmative("yes"))
        self.assertTrue(is_affirmative("yes."))
        self.assertFalse(is_affirmative("no"))
        self.assertFalse(is_affirmative("no"))

    def test_get_most_recent_tweet(self):
        mock_feed = MagicMock()
        mock_feed.entries = ["entry"]
        self.assertEqual(get_most_recent_tweet(mock_feed), "entry")

        mock_feed.entries = []
        self.assertIsNone(get_most_recent_tweet(mock_feed))

    @patch('main.feedparser.parse')
    def test_get_elon_musk_tweets(self, mock_parse):
        mock_feed = MagicMock()
        mock_feed.entries = ["entry"]
        mock_parse.return_value = mock_feed
        self.assertEqual(get_elon_musk_tweets(), "entry")
        
    def test_send_sms(self):
        message = "Test message"
        send_sms(self.twilio_client, self.twilio_phone_number, self.my_phone_number, message)
        self.twilio_client.messages.create.assert_called_once_with(
            body=message,
            from_=self.twilio_phone_number,
            to=self.my_phone_number
        )
        
    @patch('main.setup_clients')
    def test_get_GPT_determination_exception(self, mock_setup_clients):
        mock_openai_client = MagicMock()
        mock_openai_client = Exception("API Error")
        mock_setup_clients.return_value = (mock_openai_client, None, None, None)
        response = get_GPT_determination(mock_setup_clients.return_value, "Is this a test?")
        self.assertIsNone(response)


if __name__ == '__main__':
    unittest.main()
