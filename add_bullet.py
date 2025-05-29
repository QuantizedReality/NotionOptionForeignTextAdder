import requests

def add_bullet(token, page_id, text):
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"

    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    data = {
        "children": [
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": text
                            }
                        }
                    ]
                }
            }
        ]
    }

    response = requests.patch(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Bullet item ADDED!")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)