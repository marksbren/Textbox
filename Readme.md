This is a simple app I used to make a fun Christmas present opening game. It is a simple inbox for texting into. When someone texts into the Twilio number, Textbox replies with the first unread message in their message queue.

The app consists of two pages (main & user). The main page displays all users (unique phone numbers) and has a form for adding users. The user page shows the messages, whether they have been read, and has a form for adding new messages to their queue.

##Entering a User
- The phone number must be of the form "+1xxxxxxxxxx"

##Entering Messages
- Messages are delivered in the order they are entered (FIFO). Enter the first message you want a user to receive first.
- Make sure each message is under 160 characters (text message limit)

#Setup
1. Change the first line of app.yaml to be your Google Appengine domain (APPENGINENAME)
2. Setup Twilio - Put your Twilio SID & KEY into helpers.py
3. Point the Twilio number to {your appengine domain}.appspot.com/twilio 