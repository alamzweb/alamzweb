"""Shared profile content and visual tokens."""

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


@dataclass(frozen=True)
class Theme:
    background: str
    panel: str
    foreground: str
    muted: str
    border: str
    cyan: str
    blue: str
    accent: str


THEMES = {
    "dark": Theme(
        background="#08111F",
        panel="#101C2C",
        foreground="#F2F7FC",
        muted="#A7B6C8",
        border="#26384D",
        cyan="#52E5F2",
        blue="#5896FF",
        accent="#9AB9FF",
    ),
    "light": Theme(
        background="#F4F8FC",
        panel="#FFFFFF",
        foreground="#122238",
        muted="#53677E",
        border="#D8E3EF",
        cyan="#087E9B",
        blue="#245DE0",
        accent="#435D9E",
    ),
}


@dataclass(frozen=True)
class Project:
    name: str
    url: str
    logo: str
    category: str
    description: str
    lines: tuple[str, str]


PROJECTS = (
    Project(
        name="GridLeap",
        url="https://gridleap.vercel.app/",
        logo="gridleap.png",
        category="DATA DASHBOARDS",
        description="Transforms CSV files and spreadsheets into professional, mobile-friendly dashboards.",
        lines=(
            "Transforms CSV files and spreadsheets into professional,",
            "mobile-friendly dashboards.",
        ),
    ),
    Project(
        name="LinkFilo",
        url="https://linkfilo.vercel.app/",
        logo="linkfilo.png",
        category="FILE SHARING",
        description="Upload files, generate shareable links, and track views and downloads.",
        lines=(
            "Upload files, generate shareable links, and track",
            "views and downloads.",
        ),
    ),
    Project(
        name="Sitecroft",
        url="https://sitecroftdev.vercel.app/",
        logo="sitecroft.png",
        category="WEB DEVELOPMENT",
        description="A web development studio specializing in WordPress, WooCommerce, and custom websites.",
        lines=(
            "A web development studio specializing in WordPress,",
            "WooCommerce, and custom websites.",
        ),
    ),
    Project(
        name="Qovila",
        url="https://qovila.vercel.app/",
        logo="qovila.png",
        category="CLIENT PORTAL",
        description="A client request portal that helps agencies organize requests and project progress.",
        lines=(
            "A client request portal that helps agencies organize",
            "client requests and project progress.",
        ),
    ),
)


@dataclass(frozen=True)
class Technology:
    name: str
    slug: str
    color: str
    dark_color: str | None = None
    icon_url: str | None = None


TECHNOLOGY_GROUPS = (
    (
        "Languages & frontend",
        (
            Technology("HTML5", "html5", "E34F26"),
            Technology(
                "CSS3",
                "css3",
                "1572B6",
                icon_url="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg",
            ),
            Technology("JavaScript", "javascript", "F7DF1E"),
            Technology("TypeScript", "typescript", "3178C6"),
            Technology("React", "react", "61DAFB"),
            Technology("Next.js", "nextdotjs", "000000", "FFFFFF"),
            Technology("Tailwind CSS", "tailwindcss", "06B6D4"),
            Technology("Python", "python", "3776AB"),
        ),
    ),
    (
        "CMS & data",
        (
            Technology("WordPress", "wordpress", "21759B"),
            Technology("WooCommerce", "woocommerce", "96588A"),
            Technology("Supabase", "supabase", "3FCF8E"),
            Technology("PostgreSQL", "postgresql", "4169E1"),
        ),
    ),
    (
        "Automation & developer tools",
        (
            Technology("n8n", "n8n", "EA4B71"),
            Technology("Git", "git", "F05032"),
            Technology("GitHub", "github", "181717", "FFFFFF"),
            Technology("Vercel", "vercel", "000000", "FFFFFF"),
            Technology(
                "VS Code",
                "visualstudiocode",
                "007ACC",
                icon_url="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg",
            ),
        ),
    ),
)


SNAKE_URL = "https://raw.githubusercontent.com/alamzweb/alamzweb/output/snake.svg"
