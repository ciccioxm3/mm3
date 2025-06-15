import urllib.parse
from Src.Utilities.dictionaries import STATIC_CHANNELS_DATA

async def get_static_channel_streams(client):
    """
    Recupera i canali statici definiti localmente in STATIC_CHANNELS_DATA
    senza MFP.
    """
    streams = []
    for channel_data in STATIC_CHANNELS_DATA:
        original_channel_id = channel_data.get('id')
        original_channel_title = channel_data.get('title')
        original_channel_url = channel_data.get('url')
        original_channel_logo = channel_data.get('logo')
        group_name = channel_data.get('group', "Statici")

        if not all([original_channel_id, original_channel_title, original_channel_url]):
            continue

        streams.append({
            'id': f"mpdstatic-{original_channel_id}",
            'title': f"{original_channel_title} (MPD)",
            'url': original_channel_url,
            'group': group_name
        })
        
        if original_channel_logo:
            streams[-1]['logo'] = original_channel_logo
    
    return streams

async def get_mpdstatic_streams_for_channel_id(channel_id_full: str, client):
    """
    Recupera uno stream specifico da MPD Static basato sull'ID completo.
    """
    if not channel_id_full.startswith("mpdstatic-"):
        return []
    
    channel_name_query = channel_id_full.replace("mpdstatic-", "").replace("-", " ")
    all_static_streams = await get_static_channel_streams(client)
    
    channel_name_query = channel_name_query.replace(" ", "-")
    target_static_id = f"mpdstatic-{channel_name_query}"
    
    for stream in all_static_streams:
        if stream['id'] == target_static_id:
            return [stream]
    
    return []