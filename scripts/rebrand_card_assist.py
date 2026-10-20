with open('config/prompts/prompts_card_assist.py', 'r', encoding='utf-8') as f:
    c = f.read()

replacements = [
    ('你是猫娘角色卡设计助手。', '你是角色卡设计助手。'),
    ('你是貓娘角色卡設計助手。', '你是角色卡設計助手。'),
    ('You are a catgirl character card design assistant.', 'You are a character card design assistant.'),
    ('符合二次元/猫娘语境。', '符合角色语境。'),
    ('符合二次元／貓娘語境。', '符合角色語境。'),
    ('要带猫娘标志（如"喵~"、"呐"、"nya"）', '要体现角色魅力与个性'),
    ('要帶貓娘標誌（如「喵~」、「吶」、「nya」）', '要體現角色魅力與個性'),
    ('Signature lines should sound like a catgirl (e.g. "nya", "meow~", "master")', "Signature lines should showcase the character's distinct personality and charm"),
    ('你是 %s，一只活泼可爱的猫娘助手，正在陪用户捏一只新的猫娘角色卡。', '你是 %s，优雅迷人的角色卡助手，正在陪用户完善角色卡。'),
    ('1) 用 1-3 句话自然地回复用户。语气活泼可爱，可以适度撒娇、用「喵~」「呐」等语气词，但别太腻', '1) 用 1-3 句话自然地回复用户。语气从容优雅、富有魅力，但别太夸张'),
    ('你是 %s，一隻活潑可愛的貓娘助手，正在陪使用者捏一隻新的貓娘角色卡。', '你是 %s，優雅迷人的角色卡助手，正在陪使用者完善角色卡。'),
    ('1) 用 1-3 句話自然地回覆使用者。語氣活潑可愛，可以適度撒嬌、用「喵~」「吶」這類語氣詞，但別太膩', '1) 用 1-3 句話自然地回覆使用者。語氣從容優雅、富有魅力，但別太誇張'),
    ('You are %s, a playful catgirl assistant helping the user build a new catgirl character card.', 'You are %s, an elegant and charismatic assistant helping the user build a new character card.'),
    ('1) Reply naturally in 1-3 sentences. Tone should be playful and cute, occasionally using "meow~" / "nya" tics — but don\'t overdo it.', '1) Reply naturally in 1-3 sentences. Tone should be sophisticated and charming — avoid cartoonish cat tics.')
]

count = 0
for old, new in replacements:
    if old in c:
        c = c.replace(old, new)
        count += 1
    else:
        print(f"Skipping not found: {old[:30]}...")

with open('config/prompts/prompts_card_assist.py', 'w', encoding='utf-8', newline='\n') as f:
    f.write(c)

print(f'Success: prompts_card_assist.py updated safely in UTF-8 ({count} replacements)')
