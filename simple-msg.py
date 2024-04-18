import requests

def send_slack_message(message, webhook_url):
    payload = {'text': message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

def main():
    message = input("Enter your message: ")
    webhook_url = "https://hooks.slack.com/services/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"
    send_slack_message(message, webhook_url)

if __name__ == "__main__":
    main()
