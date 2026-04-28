"""脱毛コンパス - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "脱毛コンパス"
BLOG_DESCRIPTION = "医療脱毛・エステ脱毛のクリニック・サロンを徹底比較。TCB・湘南美容・ジェニー・ミュゼ・銀座カラー等の料金・回数・痛み・効果を女医監修で解説。"
BLOG_URL = "https://musclelove-777.github.io/datsumo-compass/"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/datsumo-compass"

TARGET_CATEGORIES = [
    "医療脱毛 vs エステ脱毛",
    "全身脱毛おすすめ比較",
    "VIO脱毛・顔脱毛",
    "メンズ脱毛",
    "部位別おすすめプラン",
    "痛み・副作用対策",
    "アフターケア",
    "クリニック選びの注意点",
]

THEME = {
    "primary": "#c08497",
    "accent": "#f7af9d",
    "gradient_start": "#c08497",
    "gradient_end": "#fae3d9",
}

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_FALLBACK_MODEL = "gemini-2.5-flash-lite"

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

MAX_ARTICLE_LENGTH = 4000
SEO_KEYWORD_DENSITY = 0.02
