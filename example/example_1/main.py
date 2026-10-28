from discord import SyncWebhook, Embed, ui, Interaction,ButtonStyle
import json
import requests

response=requests.get("http://127.0.0.1:8000/vivinos/yt/post/0")
res=json.loads(response.content)

if res["images"][0]==None:
    images=None
else:
    images=res['images'][0]
link=res["postLink"]
name="VIVINOS"
authorPhoto=res['authorImage']
authorLink=res["authorLink"]
desc=res["description"]
color=0x6f03fc

embed=Embed(color=color,description=desc)
embed.set_author(name=name,icon_url=authorPhoto)
embed.set_image(url=images)
button=ui.Button(url=link,label="Post Link",style=ButtonStyle.gray)
channel=ui.Button(url=authorLink,label="Channel Link",style=ButtonStyle.gray)

view=ui.View(timeout=None)
view.add_item(button)
view.add_item(channel)

webhook=SyncWebhook.from_url("WEBHOOK_URL")
webhook.send(username="Sua",avatar_url="https://i.pinimg.com/736x/dc/06/80/dc06802337cc05c90fcacf9d52efefc2.jpg",embed=embed,view=view)
