from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest


async def join_channel_and_get_info(client: TelegramClient, link: str):
    try:
        if link.startswith("https://t.me/+"):
            invite_hash = link.split("+")[1]
            await client(ImportChatInviteRequest(invite_hash))
            entity = await client.get_entity(link)

            return link, entity.id, entity.title

        elif link.startswith("https://t.me/"):
            entity = await client.get_entity(link)
            await client(JoinChannelRequest(entity))

            return {'link': link, 'tg_id': int('-100' + str(entity.id)), 'name': entity.title}
    except Exception as e:
        print(e)