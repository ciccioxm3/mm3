import urllib.parse

STATIC_CHANNELS_DATA = [
    {
        "id": "sky-sport-24",
        "title": "Sky Sport 24",
        "url": "https://linear303-it-dash1-prd.selector.skycdn.it/016a/31035/FHD/skysport24/master.mpd&key_id=003663ddf1acb25ea88a7cf973afc0d5&key=35ea91b4151d6975007998c328daee6c",
        "group": "MPD"
    },
    {
        "id": "sky-sport-uno",
        "title": "Sky Sport Uno",
        "url": "https://linear301-it-dash1-prd.selector.skycdn.it/016a/31023/FHD/skysportuno/master.mpd&key_id=0036aaa1d68c6b487e29a5cb080a8a28&key=a3e8db3ff3c876f7b43a961b64a63474",
        "group": "MPD"
    },
    {
        "id": "sky-sport-calcio",
        "title": "Sky Sport Calcio",
        "url": "https://linear302-it-dash1-prd.selector.skycdn.it/016a/31209/FHD/skysportseriea/master.mpd&key_id=00362f95db61eba0e6f14acee3f71e01&key=fb74cd84b53c7557e18424a3356c4665",
        "group": "MPD"
    },
    {
        "id": "sky-sport-f1",
        "title": "Sky Sport F1",
        "url": "https://linear307-it-dash1-prd.selector.skycdn.it/016a/31478/FHD/skysportf1/master.mpd&key_id=0036a96b6bbbf1828488f90e6b2ca1f4&key=d24e6ae926e88f8303b6926271ff8155",
        "group": "MPD"
    },
    {
        "id": "sky-sport-motogp",
        "title": "Sky Sport MotoGP",
        "url": "https://linear306-it-dash1-prd.selector.skycdn.it/016a/31483/FHD/skysportmotogp/master.mpd&key_id=00362e9181eaa0c5f91761ade3515eb8&key=52cf3c27885d58ad76aaf36d4217a984",
        "group": "MPD"
    },
    {
        "id": "sky-sport-arena",
        "title": "Sky Sport Arena",
        "url": "https://linear304-it-dash1-prd-akp2.cdn13.skycdp.com/016a/31024/FHD/skysportarena/master.mpd&key_id=00368f2bf10736c9c2c02ab0fa694d00&key=92eec9d841ac0c1ff16b90a0db82c792",
        "group": "MPD"
    },
    {
        "id": "sky-sport-tennis",
        "title": "Sky Sport Tennis",
        "url": "https://linear310-it-dash1-prd.selector.skycdn.it/016a/32559/FHD/skysporttennis/master.mpd&key_id=0036fb7c564c4eb99e310f5fa82ab2f2&key=647f07b6858a669456e73ca103b4c2c0",
        "group": "MPD"
    },
    {
        "id": "sky-sport-nba",
        "title": "Sky Sport NBA",
        "url": "https://linear308-it-dash1-prd-akp2.cdn13.skycdp.com/016a/31764/FHD/skysportnba/master.mpd&key_id=00364eac2ffee337640e39682439b540&key=0960172d9000c470ade0658bd36c1d53",
        "group": "MPD"
    },
    {
        "id": "sky-sport-max",
        "title": "Sky Sport Max",
        "url": "https://linear305-it-dash1-prd-akp2.cdn13.skycdp.com/016a/31248/FHD/skysportmax/master.mpd&key_id=0036f13bca1c5603b9f3bb28ec28fa80&key=f01403bcb5a02c61153d297fb0c4395f",
        "group": "MPD"
    },
    {
        "id": "sky-sport-golf",
        "title": "Sky Sport Golf",
        "url": "https://linear309-it-dash1-prd-akp2.cdn13.skycdp.com/016a/32768/FHD/skysportgolf/master.mpd&key_id=00360b7729f74bf56a0a4eb0eda15ec5&key=f8a5f4723c71ac84c2f1ff6f55939a63",
        "group": "MPD"
    },
    # Aggiungi qui tutti gli altri canali statici da STATIC_CHANNELS_DATA...
]

async def get_static_channel_streams(client, mfp_url=None, mfp_password=None):
    """
    Recupera i canali statici definiti localmente in STATIC_CHANNELS_DATA
    e applica la logica MFP se fornita.
    """
    streams = []
    for channel_data in STATIC_CHANNELS_DATA:
        original_channel_id = channel_data.get('id')
        original_channel_title = channel_data.get('title')
        original_channel_url = channel_data.get('url')
        original_channel_logo = channel_data.get('logo')
        group_name = channel_data.get('group',