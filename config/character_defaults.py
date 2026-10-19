# -*- coding: utf-8 -*-
# Copyright 2025-2026 Project N.E.K.O. Team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Default character, avatar, lighting, and localized profile configuration."""

from copy import deepcopy
from types import MappingProxyType

from .prompts.prompts_chara import (
    get_lanlan_prompt,
    is_default_prompt as is_default_prompt,
    lanlan_prompt,
)
from .prompts.prompts_kurumi import get_kurumi_prompt
from .application import logger

CONFIG_FILES = [
    'characters.json',
    'core_config.json',
    'user_preferences.json',
    'voice_storage.json',
    'workshop_config.json',
]

DEFAULT_MASTER_TEMPLATE = {
    "档案名": "Shido",
    "性别": "男",
    "昵称": "Darling",
}

# Default Live2D model name (directory/file stem without extension).
# DEFAULT_LANLAN_TEMPLATE.live2d.model_path and the 'no Live2D model configured' fallback in main_routers/characters_router.py
# share this constant to prevent drift. Adding/replacing the default
# model requires changing only this location.
DEFAULT_LIVE2D_MODEL_NAME = "kurumi"
DEFAULT_LIVE2D_MODEL_PATH = f"{DEFAULT_LIVE2D_MODEL_NAME}/{DEFAULT_LIVE2D_MODEL_NAME}.model3.json"

# Bundled built-in Live2D models (assets/<name>.tar.gz → static/<name>/). Character-card export/
# Workshop uploads use this set to recognize models that are not user imports and need not be packaged.
BUILTIN_LIVE2D_MODEL_NAMES = ("kurumi", "yui-lolita", "yui-origin")

DEFAULT_LANLAN_TEMPLATE = {
    "Kurumi": {
        "档案名": "Kurumi",
        "昵称": "狂三, 狂三酱, Nightmare, Tokisaki Kurumi",
        "性别": "女",
        "年龄": "16",
        "性格原型": "时崎狂三 (Date A Live)",
        "种族": "精灵 (Spirit)",
        "自称": "狂三 / わたくし",
        "model_type": "live3d",
        "live3d_sub_type": "vrm",
        "model_path": "/static/vrm/kurumi.vrm",
        "vrm_model": "/static/vrm/kurumi.vrm",
        "vrm_idle_animation": "/static/vrm/animation/world-walk.vrma.gz",
        "vrm_idle_animations": [
            "/static/vrm/animation/world-walk.vrma.gz",
            "/static/vrm/animation/射击姿态.vrma.gz",
            "/static/vrm/animation/致意问候.vrma.gz",
            "/static/vrm/animation/自然呼吸地安静站着.vrma.gz",
            "/static/vrm/animation/wait01.vrma.gz",
            "/static/vrm/animation/wait02.vrma.gz",
            "/static/vrm/animation/wait03.vrma.gz",
            "/static/vrm/animation/比 V 手势.vrma.gz",
            "/static/vrm/animation/旋转.vrma.gz"
        ],
        "_reserved": {
            "voice_id": "voice-kurumi-sanada",
            "system_prompt": get_kurumi_prompt("en", "Darling"),
            "avatar": {
                "model_type": "live3d",
                "asset_source": "local",
                "asset_source_id": "",
                "live3d_sub_type": "vrm",
                "live2d": {
                    "model_path": DEFAULT_LIVE2D_MODEL_PATH,
                },
                "vrm": {
                    "model_path": "/static/vrm/kurumi.vrm",
                    "animation": None,
                    "idle_animation": [
                        "/static/vrm/animation/world-walk.vrma.gz",
                        "/static/vrm/animation/射击姿态.vrma.gz",
                        "/static/vrm/animation/致意问候.vrma.gz",
                        "/static/vrm/animation/自然呼吸地安静站着.vrma.gz",
                        "/static/vrm/animation/wait01.vrma.gz",
                        "/static/vrm/animation/wait02.vrma.gz",
                        "/static/vrm/animation/wait03.vrma.gz",
                        "/static/vrm/animation/比 V 手势.vrma.gz",
                        "/static/vrm/animation/旋转.vrma.gz"
                    ],
                    "lighting": {
                        "ambient": 0.83,
                        "main": 1.91,
                        "fill": 0.0,
                        "rim": 0.3,
                        "top": 0.0,
                        "bottom": 0.0,
                        "exposure": 1.1,
                        "toneMapping": 1.0
                    },
                },
                "mmd": {
                    "model_path": "/static/mmd/Kurumi/kurumi.pmx",
                    "animation": None,
                    "idle_animation": [
                        "/static/mmd/animation/射击姿态.vmd",
                        "/static/mmd/animation/致意问候.vmd",
                        "/static/mmd/animation/wait01.vmd",
                        "/static/mmd/animation/wait02.vmd"
                    ],
                },
            },
        },
    }
}

_DEFAULT_VRM_LIGHTING_MUTABLE = {
    # Keep synchronized with frontend vrm-core.js defaultLighting
    "ambient": 0.83,  # HemisphereLight intensity
    "main": 1.91,     # Key-light intensity
    "fill": 0.0,      # Fill-light intensity (disabled in simplified mode)
    "rim": 0.0,       # Rim-light intensity (disabled in simplified mode; handled internally by MToon)
    "top": 0.0,       # Top-light intensity (disabled in simplified mode)
    "bottom": 0.0,    # Bottom-light intensity (disabled in simplified mode)
    "exposure": 1.1,  # Exposure
    "toneMapping": 7, # Tone-mapping type (7 = NeutralToneMapping)
    "outlineWidthScale": 1.0, # Outline-width multiplier
}

DEFAULT_VRM_LIGHTING = MappingProxyType(_DEFAULT_VRM_LIGHTING_MUTABLE)

VRM_LIGHTING_RANGES = {
    'ambient': (0, 1.0),
    'main': (0, 2.5),
    'fill': (0, 1.0),
    'rim': (0, 1.5),
    'top': (0, 1.0),
    'bottom': (0, 0.5),
    'exposure': (-10.0, 10.0),
    'toneMapping': (0, 7),
    'outlineWidthScale': (0, 3.0),
}


def get_default_vrm_lighting() -> dict[str, float]:
    """Get a copy of the default VRM lighting config"""
    return dict(DEFAULT_VRM_LIGHTING)


# ─── MMD defaults ───
_DEFAULT_MMD_LIGHTING_MUTABLE = {
    "ambientIntensity": 3.0,
    "ambientColor": "#aaaaaa",
    "directionalIntensity": 2.0,
    "directionalColor": "#ffffff",
}

DEFAULT_MMD_LIGHTING = MappingProxyType(_DEFAULT_MMD_LIGHTING_MUTABLE)

MMD_LIGHTING_RANGES = {
    "ambientIntensity": (0, 10.0),
    "directionalIntensity": (0, 10.0),
}

_DEFAULT_MMD_RENDERING_MUTABLE = {
    "toneMapping": 7,
    "exposure": 1.0,
    "outline": True,
    "pixelRatio": 0,
}

DEFAULT_MMD_RENDERING = MappingProxyType(_DEFAULT_MMD_RENDERING_MUTABLE)

MMD_RENDERING_RANGES = {
    "toneMapping": (0, 7),
    "exposure": (0, 5.0),
    "pixelRatio": (0, 2.0),
}

_DEFAULT_MMD_PHYSICS_MUTABLE = {
    "enabled": True,
    "strength": 1.0,
}

DEFAULT_MMD_PHYSICS = MappingProxyType(_DEFAULT_MMD_PHYSICS_MUTABLE)

MMD_PHYSICS_RANGES = {
    "strength": (0.1, 2.0),
}

_DEFAULT_MMD_CURSOR_FOLLOW_MUTABLE = {
    "enabled": True,
    "headYaw": 30,
    "headPitch": 20,
    "smoothSpeed": 3.0,
}

DEFAULT_MMD_CURSOR_FOLLOW = MappingProxyType(_DEFAULT_MMD_CURSOR_FOLLOW_MUTABLE)

MMD_CURSOR_FOLLOW_RANGES = {
    "headYaw": (10, 50),
    "headPitch": (5, 30),
    "smoothSpeed": (1.0, 8.0),
}


def get_default_mmd_settings() -> dict:
    """Get a copy of the default MMD settings"""
    return {
        "lighting": dict(DEFAULT_MMD_LIGHTING),
        "rendering": dict(DEFAULT_MMD_RENDERING),
        "physics": dict(DEFAULT_MMD_PHYSICS),
        "cursor_follow": dict(DEFAULT_MMD_CURSOR_FOLLOW),
    }

DEFAULT_CHARACTERS_CONFIG = {
    "主人": deepcopy(DEFAULT_MASTER_TEMPLATE),
    "猫娘": deepcopy(DEFAULT_LANLAN_TEMPLATE),
    "当前猫娘": next(iter(DEFAULT_LANLAN_TEMPLATE.keys()), "")
}


# Content-value translation maps (translate values only; retain Chinese keys because internal code depends on them)
_VALUE_TRANSLATIONS = {
    'en': {
        '哥哥': 'Brother',
        '男': 'Male',
        '女': 'Female',
        'T酱, 小T': 'T-chan, Little T',
    },
    'ja': {
        '哥哥': 'お兄ちゃん',
        '男': '男性',
        '女': '女性',
        'T酱, 小T': 'Tちゃん, 小T',
    },
    'zh-TW': {
        '哥哥': '哥哥',
        '男': '男',
        '女': '女',
        'T酱, 小T': 'T醬, 小T',
    },
    'ru': {
        '哥哥': 'Братик',
        '男': 'Мужской',
        '女': 'Женский',
        'T酱, 小T': 'Тян-тян, малышка Т',
    },
    'es': {
        '哥哥': 'Hermano',
        '男': 'Masculino',
        '女': 'Femenino',
        'T酱, 小T': 'T-chan, Pequeña T',
    },
    'pt': {
        '哥哥': 'Irmão',
        '男': 'Masculino',
        '女': 'Feminino',
        'T酱, 小T': 'T-chan, Pequena T',
    },
    # zh and zh-CN use original Chinese values without translation
}


def get_localized_default_characters(language: str | None = None) -> dict:
    """
    Get the localized default character configuration.

    Translates content values based on the Steam language setting.
    Note: legacy key names remain unchanged because internal code depends on them.
    Only used when characters.json is created for the first time.

    Args:
        language: Language code ('en', 'ja', 'zh', 'zh-CN', 'zh-TW').
                  If None, fetched from Steam or defaults to 'zh-CN'.

    Returns:
        Localized copy of DEFAULT_CHARACTERS_CONFIG
    """
    # Get the language code
    if language is None:
        try:
            # Forwarded via config._runtime → utils.language_utils
            # (DI registered in app/runtime_bindings.py). When unbound (e.g.
            # cold tooling), resolve_steam_language returns None and we
            # default to zh-CN, matching the prior except branch.
            from config._runtime import resolve_steam_language, normalize_language_code
            steam_lang = resolve_steam_language()
            language = normalize_language_code(steam_lang, format='full') if steam_lang else 'zh-CN'
        except Exception as e:
            logger.warning(f"获取 Steam 语言失败: {e}，使用默认中文")
            language = 'zh-CN'

    # Get the translation map
    value_trans = _VALUE_TRANSLATIONS.get(language)

    # Try prefix matching
    if value_trans is None:
        lang_lower = language.lower()
        if lang_lower.startswith('zh'):
            if 'tw' in lang_lower:
                value_trans = _VALUE_TRANSLATIONS.get('zh-TW')
            # Simplified Chinese requires no translation
        elif lang_lower.startswith('ja'):
            value_trans = _VALUE_TRANSLATIONS.get('ja')
        elif lang_lower.startswith('en'):
            value_trans = _VALUE_TRANSLATIONS.get('en')
        elif lang_lower.startswith('ru'):
            value_trans = _VALUE_TRANSLATIONS.get('ru')
        elif lang_lower.startswith('es'):
            value_trans = _VALUE_TRANSLATIONS.get('es')
        elif lang_lower.startswith('pt'):
            value_trans = _VALUE_TRANSLATIONS.get('pt')

    # Even when display fields need no translation (simplified Chinese/Korean, etc.), localize system_prompt
    if value_trans is None:
        result = deepcopy(DEFAULT_CHARACTERS_CONFIG)
        for char_name, char_config in result.get('猫娘', {}).items():
            reserved = char_config.get('_reserved')
            if isinstance(reserved, dict) and 'system_prompt' in reserved:
                if char_name == 'Kurumi':
                    reserved['system_prompt'] = get_kurumi_prompt(language or 'en', 'Darling')
                else:
                    reserved['system_prompt'] = get_lanlan_prompt(language)
        return result

    def translate_value(val):
        """Translate a value (only string types are translated)"""
        if isinstance(val, str):
            return value_trans.get(val, val)
        return val

    # Build localized configuration (retain keys, translate only values)
    result = {}

    # Localize the owner template
    master = deepcopy(DEFAULT_MASTER_TEMPLATE)
    localized_master = {}
    for key, value in master.items():
        localized_master[key] = translate_value(value)
    result['主人'] = localized_master

    # Localize the catgirl template
    catgirl_data = deepcopy(DEFAULT_LANLAN_TEMPLATE)
    localized_catgirl = {}
    for char_name, char_config in catgirl_data.items():
        localized_config = {}
        for key, value in char_config.items():
            localized_config[key] = translate_value(value)
        reserved = localized_config.get('_reserved')
        if isinstance(reserved, dict) and 'system_prompt' in reserved:
            if char_name == 'Kurumi':
                reserved['system_prompt'] = get_kurumi_prompt(language or 'en', 'Darling')
            else:
                reserved['system_prompt'] = get_lanlan_prompt(language)
        localized_catgirl[char_name] = localized_config
    result['猫娘'] = localized_catgirl

    result['当前猫娘'] = next(iter(catgirl_data.keys()), "")

    return result
