import requests 

def add_paragraph(token, page_id, text):
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
        }
    data = {
            "children": [{
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{
                        "type": "text",
                        "text": {"content": text}
                    }

                    ]
                }
            }

            ]
        }
    res = requests.patch(url, headers=headers,  json=data)
    print("Holy SHIT IT WORKED" if res.status_code == 200 else f"Error: {res.text}")