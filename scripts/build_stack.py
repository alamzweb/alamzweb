"""Build a GitHub-compatible technology icon grid."""

from html import escape

from theme import TECHNOLOGY_GROUPS, Technology


ICON_BASE_URL = "https://cdn.simpleicons.org"
ICONS_PER_ROW = 4


def _icon_url(slug: str, color: str) -> str:
    return f"{ICON_BASE_URL}/{slug}/{color}"


def _technology_cell(technology: Technology) -> str:
    light_url = technology.icon_url or _icon_url(technology.slug, technology.color)
    dark_url = _icon_url(technology.slug, technology.dark_color or technology.color)
    if technology.dark_color:
        icon = (
            f'<picture><source media="(prefers-color-scheme: dark)" srcset="{dark_url}">'
            f'<img src="{light_url}" width="30" height="30" alt="{escape(technology.name)}"></picture>'
        )
    else:
        icon = (
            f'<img src="{light_url}" width="30" height="30" '
            f'alt="{escape(technology.name)}">'
        )
    return (
        '<td align="center" width="120">'
        f"{icon}<br><sub>{escape(technology.name)}</sub></td>"
    )


def build_stack() -> str:
    sections = []
    for group_name, technologies in TECHNOLOGY_GROUPS:
        rows = []
        for start in range(0, len(technologies), ICONS_PER_ROW):
            cells = "".join(
                _technology_cell(item)
                for item in technologies[start : start + ICONS_PER_ROW]
            )
            rows.append(f"  <tr>{cells}</tr>")
        sections.append(
            f"### {group_name}\n\n<table align=\"center\">\n{chr(10).join(rows)}\n</table>"
        )
    return "\n\n".join(sections)


if __name__ == "__main__":
    print(build_stack())
