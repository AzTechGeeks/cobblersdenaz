"""Build index.html from src/template.html by inlining every image as a data URI.

Run from the repo root:  python src/build.py
"""
import base64, mimetypes, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
IMAGES = {
    "{{HERO}}":      SRC / "images/photos/hero.jpg",
    "{{SHOES}}":     SRC / "images/photos/shoes.jpg",
    "{{BOOTS}}":     SRC / "images/photos/boots.jpg",
    "{{BAGS}}":      SRC / "images/photos/bags.jpg",
    "{{LUGGAGE}}":   SRC / "images/photos/luggage.jpg",
    "{{LEATHER}}":   SRC / "images/photos/leather.jpg",
    "{{SHINE}}":     SRC / "images/photos/shine.jpg",
    "{{STORY}}":     SRC / "images/photos/story.jpg",
    "{{BENCH}}":     SRC / "images/photos/bench.jpg",
    "{{AWARD2012}}": SRC / "images/client/scottsdale2012.jpg",
    "{{AWARD2013}}": SRC / "images/client/scottsdale2013.jpg",
    "{{AWARD2015}}": SRC / "images/client/scottsdale2015.jpg",
    "{{LOGO_MP}}":   SRC / "images/client/mplogo.jpg",
    "{{LOGO_TC}}":   SRC / "images/client/tcl.jpg",
    "{{LOGO_SPENCO}}": SRC / "images/client/spenco.gif",
    "{{LOGO_REMO}}": SRC / "images/client/remo.png",
}

def data_uri(path: pathlib.Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()

html = (SRC / "template.html").read_text(encoding="utf-8")
for token, path in IMAGES.items():
    if token not in html:
        raise SystemExit(f"token {token} missing from template")
    html = html.replace(token, data_uri(path))
if "{{" in html:
    raise SystemExit("unreplaced token left in output")
out = ROOT / "index.html"
out.write_text(html, encoding="utf-8")
print(f"wrote {out} ({out.stat().st_size // 1024} KB)")
