### Python Slack Playground
## Requirements
Before you begin, generate the following:
```
export SLACK_BOT_TOKEN="xoxb-xxxxxxxxx"
export SLACK_APP_TOKEN="xapp-xxxxxxxx"
export SLACK_WEBHOOK="https://hooks.slack.com/services/xxxxxxxxxxx/xxxxxxxxxxxxxxx/xxxxxxxxxxxxxxx"
```

## Test Button Reponse
This code snippet tests response to button clicks
```
python3 app-slash.py
```
Message Paylod
```
{
    "text": "Test Button",
    "username":"admin",
    "channel" : "#general",
    "icon_emoji": ":star:",
    "attachments": [
        {
            "fallback": "Test Comic Book?",
            "title": "Test Comic Book?",
            "callback_id": "comic_1234_xyz",
            "color": "#3AA3E3",
            "attachment_type": "default",
            "actions": [
                {
                    "name": "yes",
                    "text": "Yes",
                    "type": "button",
                    "style": "danger",
                    "action_id": "yes_deploy",
                    "value": "yes"
                },
                {
                    "name": "no",
                    "text": "No",
                    "type": "button",
                    "style": "primary",
                    "action_id": "no_deploy",
                    "value": "no"
                }
            ]
        }
    ],
    "blocks": [
    	{
    		"type": "section",
    		"text": {
    			"type": "mrkdwn",
    			"text": "Test Completed"
    		}
    	}
    ]
}
```
curl -XPUT "${SLACK_WEBHOOK}" --data-binary "@message.json" -H "Content-type:application/json"
