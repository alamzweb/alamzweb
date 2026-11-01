"""Generate individually theme-aware project card SVGs."""

import base64
from html import escape
from pathlib import Path

from theme import ASSETS, PROJECTS, Project, THEMES


CARD_HEIGHT = 170
CARD_WIDTH = 480
LOGO_SIZE = 68


def _logo_data(logo_path: Path) -> str:
    encoded = base64.b64encode(logo_path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def build_project_card(project: Project, theme_name: str) -> str:
    theme = THEMES[theme_name]
    name = escape(project.name)
    category = escape(project.category)
    description = tuple(escape(line) for line in project.lines)
    logo = _logo_data(ASSETS / project.logo)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{CARD_WIDTH}" height="{CARD_HEIGHT}" viewBox="0 0 {CARD_WIDTH} {CARD_HEIGHT}" role="img" aria-labelledby="title description">
  <title id="title">{name}</title>
  <desc id="description">{escape(project.description)}</desc>
  <defs>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{theme.cyan}"/>
      <stop offset="1" stop-color="{theme.blue}"/>
    </linearGradient>
  </defs>
  <rect x="1" y="1" width="478" height="168" rx="19" fill="{theme.panel}" stroke="{theme.border}" stroke-width="2"/>
  <rect x="1" y="20" width="4" height="130" rx="2" fill="url(#accent)"/>
  <rect x="22" y="51" width="{LOGO_SIZE}" height="{LOGO_SIZE}" rx="15" fill="#F5FAFD"/>
  <image href="{logo}" x="27" y="56" width="{LOGO_SIZE - 10}" height="{LOGO_SIZE - 10}" preserveAspectRatio="xMidYMid meet"/>
  <text x="108" y="47" fill="{theme.cyan}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="10" font-weight="700" letter-spacing="1.7">{category}</text>
  <text x="108" y="79" fill="{theme.foreground}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="23" font-weight="700">{name}</text>
  <text x="108" y="106" fill="{theme.muted}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="12">{description[0]}</text>
  <text x="108" y="124" fill="{theme.muted}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="12">{description[1]}</text>
  <text x="450" y="151" fill="{theme.accent}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="10" font-weight="600" text-anchor="end">OPEN PROJECT ↗</text>
</svg>
"""


def main() -> None:
    for project in PROJECTS:
        logo = ASSETS / project.logo
        if not logo.is_file():
            raise FileNotFoundError(f"Required project logo not found: {logo}")

    ASSETS.mkdir(parents=True, exist_ok=True)
    for project in PROJECTS:
        slug = project.name.lower()
        for theme_name in THEMES:
            output = ASSETS / f"{slug}-card-{theme_name}.svg"
            output.write_text(
                build_project_card(project, theme_name), encoding="utf-8"
            )
            print(f"Generated {output.relative_to(ASSETS.parent)}")


if __name__ == "__main__":
    main()
