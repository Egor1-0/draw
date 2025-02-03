from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors import UserAlreadyParticipantError

async def join_channel_and_get_info(client: TelegramClient, link: str):
    if link.startswith("https://t.me/+"):
        invite_hash = link.split("+")[1]
        try:
            await client(ImportChatInviteRequest(invite_hash))
        except UserAlreadyParticipantError:
            pass
        entity = await client.get_entity(link)

        return {'link': link, 'tg_id': int(str(entity.id)), 'name': entity.title}

    else: # link.startswith("https://t.me/"):
        entity = await client.get_entity(link)
        try:
            await client(JoinChannelRequest(entity))
        except UserAlreadyParticipantError:
            pass

        return {'link': link, 'tg_id': int(str(entity.id)), 'name': entity.title}