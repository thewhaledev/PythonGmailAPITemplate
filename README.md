# Quick Start Template for Gmail's API - With Python

This easy-to-use template extends Google's Quickstart authentication template for Gmail, allowing you to create and send messages.

##Guide:

Firstly, go to [Gmail Quickstart](https://developers.google.com/gmail/api/quickstart/python) template for Python, and follow the
steps to receive your credentials.json file, store it in a blank directory of your choosing.

Now, install the Google client library as follows:

```
$ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

Then, fill in the following variables with the message you want to send, the subject of your email, the sender (the account you used
to get the authentication credentials), and the recipient of your email.

```python3
message_text="#"
subject = "#"
sender = "#"
to = "#"
```

All you have to do now is fill in the user_id, with the same email you used for the sender variable.

```python3
user_id = "#"
```

When you run the file, you'll create an automatic "token.pickle" file. You'll have to delete this if you ever want to change the scope.

Finally, running the program will also prompt you to authorize access to your account. If you are not signed in, or you are logged
into more than one account, you will be prompted to choose which one you want to give access.
