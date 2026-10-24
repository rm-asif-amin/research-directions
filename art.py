"""Small schematic drawings for the method graphics (same visual language as the Zero-G project's pipeline overview).

Every drawing is a 160 x 90 SVG. ART[key] returns the inner SVG markup; svg(key) wraps it.
"""
BLUE, ORANGE, RED, GREEN, GRAY, DARK, WOOD, WALL = "#2a78d6", "#eb6834", "#d64545", "#3bb36b", "#8a929c", "#39414a", "#a0773f", "#7aa7e0"


def table(y=80, x1=12, x2=148):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{WOOD}" stroke-width="5"/>'


def cube(x, y, s=14, c=RED, rot=0):
    return f'<rect x="{x - s / 2}" y="{y - s / 2}" width="{s}" height="{s}" fill="{c}" transform="rotate({rot} {x} {y})"/>'


def walls(x=38, y=14, w=84, h=64):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{WALL}" stroke-dasharray="4 3"/>'


def shadow(x, y=77, rx=9):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="2.4" fill="#00000022"/>'


def floating(x=80, y=40, rot=18, c=RED):
    return cube(x, y, 14, c, rot) + f'<path d="M{x} {y + 11} V{y + 33}" stroke="#bbb" stroke-dasharray="2 3"/>' + shadow(x)


def arm(base=(22, 80), elbow=(42, 34), hand=(74, 44), c="#b9bec5"):
    (bx, by), (ex, ey), (hx, hy) = base, elbow, hand
    return (f'<polyline points="{bx},{by} {ex},{ey} {hx},{hy}" fill="none" stroke="{c}" stroke-width="7" '
            f'stroke-linecap="round" stroke-linejoin="round"/>'
            f'<circle cx="{ex}" cy="{ey}" r="4" fill="{DARK}"/><rect x="{bx - 8}" y="{by - 6}" width="16" height="6" fill="{DARK}"/>'
            f'<path d="M{hx} {hy - 6} v12 M{hx} {hy - 6} h6 M{hx} {hy + 6} h6" stroke="{DARK}" stroke-width="2.4" fill="none"/>')


def vla(x=50, y=30, w=60, h=26, label="VLA", fill=DARK):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}"/>'
            f'<text x="{x + w / 2}" y="{y + h / 2 + 4.5}" text-anchor="middle" font-size="12.5" font-weight="700" fill="#fff">{label}</text>')


def label(x, y, t, size=10.5, c="#39414a", weight=400, anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{c}">{t}</text>'


def dots(pts, c=BLUE, r=3, op=.8):
    return f'<g fill="{c}" opacity="{op}">' + "".join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y in pts) + "</g>"


def cards(x=46, y=20, w=58, h=40, n=3):
    out = ""
    for i in reversed(range(n)):
        ox, oy = x + i * 7, y + i * 6
        out += (f'<rect x="{ox}" y="{oy}" width="{w}" height="{h}" rx="4" fill="#fff" stroke="{GRAY}"/>'
                f'<path d="M{ox + 8} {oy + 12} h{w - 16} M{ox + 8} {oy + 20} h{w - 24} M{ox + 8} {oy + 28} h{w - 20}" stroke="#cfd4da" stroke-width="3"/>')
    return out


def post(x, top, w=16, base=80, c="#c9ced5"):
    return f'<rect x="{x - w / 2}" y="{top}" width="{w}" height="{base - top}" fill="{c}"/>'


def bubble(x, y, w, h, text, size=10.5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="#fff" stroke="{BLUE}" stroke-width="1.4"/>'
            f'<path d="M{x + 14} {y + h} l-4 9 l12 -9" fill="#fff" stroke="{BLUE}" stroke-width="1.4"/>'
            f'<rect x="{x + 9}" y="{y + h - 2}" width="14" height="4" fill="#fff"/>'
            + label(x + w / 2, y + h / 2 + 4, text, size, BLUE, 600))


def check(x, y, s=1.0, c=GREEN):
    return f'<path d="M{x - 7 * s} {y} l{5 * s} {6 * s} l{10 * s} {-12 * s}" stroke="{c}" stroke-width="{3.2 * s}" fill="none" stroke-linecap="round"/>'


def cross(x, y, s=1.0, c=RED):
    return f'<path d="M{x - 6 * s} {y - 6 * s} l{12 * s} {12 * s} M{x + 6 * s} {y - 6 * s} l{-12 * s} {12 * s}" stroke="{c}" stroke-width="{3 * s}" stroke-linecap="round"/>'


def g_arrow(x, y, length, txt="g", c=DARK):
    if length <= 0:
        return label(x, y + 8, "g = 0", 11, BLUE, 700)
    return (f'<path d="M{x} {y} v{length}" stroke="{c}" stroke-width="2.4"/>'
            f'<path d="M{x - 5} {y + length - 6} l5 7 l5 -7" fill="none" stroke="{c}" stroke-width="2.4"/>'
            + label(x + 10, y + length / 2 + 4, txt, 11, c, 700, "start"))


def planet(x, y, r, c="#4f8fdc", land=GREEN):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'
            f'<path d="M{x - r * .5} {y - r * .3} q{r * .3} -{r * .4} {r * .6} 0 q-{r * .1} {r * .4} -{r * .6} 0z '
            f'M{x + r * .1} {y + r * .3} q{r * .3} -{r * .2} {r * .5} {r * .1} q-{r * .2} {r * .3} -{r * .5} -{r * .1}z" fill="{land}"/>')


def satellite(x, y):
    return (f'<rect x="{x - 6}" y="{y - 5}" width="12" height="10" fill="#c9ced5" stroke="{DARK}"/>'
            f'<rect x="{x - 22}" y="{y - 3}" width="14" height="6" fill="{BLUE}"/><rect x="{x + 8}" y="{y - 3}" width="14" height="6" fill="{BLUE}"/>')


def curve(x=34, y=14, w=92, h=60, pts=(0, .1, .3, .55, .72, .82, .88)):
    n = len(pts) - 1
    poly = " ".join(f"{x + w * i / n:.1f},{y + h - h * p:.1f}" for i, p in enumerate(pts))
    return (f'<path d="M{x} {y} V{y + h} H{x + w}" stroke="{GRAY}" fill="none" stroke-width="1.4"/>'
            f'<polyline points="{poly}" fill="none" stroke="{BLUE}" stroke-width="2.6"/>')


def ruler(x, y, w=80):
    ticks = "".join(f'<path d="M{x + i * w / 8} {y} v{6 if i % 2 else 10}" stroke="{DARK}" stroke-width="1.2"/>' for i in range(9))
    return f'<rect x="{x}" y="{y}" width="{w}" height="14" fill="#f3e2b8" stroke="{WOOD}"/>' + ticks


def wire_box(x=48, y=18, s=46, d=16, corner=True):
    a = (x, y + d)
    b = (x + s, y + d)
    out = (f'<rect x="{a[0]}" y="{a[1]}" width="{s}" height="{s}" fill="none" stroke="{WALL}" stroke-width="1.6"/>'
           f'<rect x="{x + d}" y="{y}" width="{s}" height="{s}" fill="none" stroke="{WALL}" stroke-width="1.2" stroke-dasharray="3 2"/>'
           f'<path d="M{a[0]} {a[1]} l{d} -{d} M{b[0]} {b[1]} l{d} -{d} M{a[0]} {a[1] + s} l{d} -{d} M{b[0]} {b[1] + s} l{d} -{d}" stroke="{WALL}" stroke-width="1.2"/>')
    if corner:
        out += f'<circle cx="{b[0]}" cy="{b[1]}" r="5" fill="{ORANGE}"/>'
    return out


def cloud(x, y, w, h):
    """Thought bubble: rounded box with two small trailing circles at the lower left."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h - 10}" rx="18" fill="#fff" stroke="{BLUE}" stroke-width="1.4"/>'
            f'<circle cx="{x + 10}" cy="{y + h - 4}" r="4" fill="#fff" stroke="{BLUE}" stroke-width="1.2"/>'
            f'<circle cx="{x + 3}" cy="{y + h + 4}" r="2.4" fill="#fff" stroke="{BLUE}" stroke-width="1.1"/>')


def frame(x, y, w, h, inner=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="#fff" stroke="{DARK}" stroke-width="1.4"/>' + inner


def magnifier(x, y, r=13):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffffffaa" stroke="{DARK}" stroke-width="2.6"/>'
            f'<path d="M{x + r * .7} {y + r * .7} l{r * .7} {r * .7}" stroke="{DARK}" stroke-width="4" stroke-linecap="round"/>')


def battery(x, y, frac=.85):
    return (f'<rect x="{x}" y="{y}" width="44" height="22" rx="3" fill="#fff" stroke="{DARK}" stroke-width="2"/>'
            f'<rect x="{x + 44}" y="{y + 7}" width="4" height="8" fill="{DARK}"/>'
            f'<rect x="{x + 3}" y="{y + 3}" width="{38 * frac}" height="16" fill="{GREEN}"/>')


def funnel(x, y):
    return f'<path d="M{x} {y} h50 l-18 22 v16 l-14 6 v-22 z" fill="#eef0f3" stroke="{DARK}" stroke-width="1.6"/>'


def cylinder(x, y, w=44, h=40, c="#e8f1fc"):
    return (f'<path d="M{x} {y} v{h} a{w / 2} 6 0 0 0 {w} 0 v-{h}" fill="{c}" stroke="{BLUE}" stroke-width="1.6"/>'
            f'<ellipse cx="{x + w / 2}" cy="{y}" rx="{w / 2}" ry="6" fill="#fff" stroke="{BLUE}" stroke-width="1.6"/>'
            f'<path d="M{x} {y + h * .45} a{w / 2} 6 0 0 0 {w} 0" fill="none" stroke="{BLUE}" stroke-width="1.2"/>')


def grid(x, y, n=3, s=16):
    marks = [(0, 0, 1), (1, 0, 1), (2, 0, 0), (0, 1, 1), (1, 1, 0), (2, 1, 1), (0, 2, 0), (1, 2, 1), (2, 2, 1)]
    out = ""
    for i, j, ok in marks[: n * n]:
        cx, cy = x + i * (s + 3), y + j * (s + 3)
        out += f'<rect x="{cx}" y="{cy}" width="{s}" height="{s}" rx="2" fill="{"#e6f6ee" if ok else "#fbe6e4"}" stroke="#c9ced5"/>'
    return out


ART = {
    # 1 zero-G training
    "zg_expert": lambda: walls() + table() + floating() + arm((22, 80), (30, 30), (62, 34)) + label(124, 30, "g = 0", 10, BLUE, 700, "start"),
    "zg_demos": lambda: walls() + table() + dots([(52, 26), (70, 38), (104, 24), (92, 50), (58, 56), (110, 60), (78, 22), (96, 36), (66, 48)])
        + dots([(64, 74), (80, 75), (96, 74)], ORANGE),
    "vla_distill": lambda: frame(18, 18, 34, 26, cube(35, 33, 9)) + label(35, 56, "images", 9.5) + label(35, 67, "+ language", 9.5)
        + '<path d="M56 31 h14" stroke="#8a929c" stroke-width="2"/><path d="M66 27 l5 4 l-5 4" fill="none" stroke="#8a929c" stroke-width="2"/>'
        + vla(76, 18, 66, 26, "VLA") + label(109, 60, "fine-tune", 10),
    "platform_test": lambda: table() + post(56, 46) + post(108, 30) + cube(56, 39, 13) + '<circle cx="108" cy="22" r="6" fill="#3bb36b"/>'
        + label(82, 12, "Earth gravity", 9.5, DARK, 600),
    # 2 Earth -> space
    "earth_vla": lambda: planet(44, 46, 26) + vla(84, 32, 56, 26),
    "micro_tasks": lambda: f'<ellipse cx="80" cy="46" rx="62" ry="22" fill="none" stroke="{GRAY}" stroke-dasharray="3 3"/>'
        + planet(80, 46, 14) + satellite(132, 34) + cube(34, 30, 14, RED, 25) + label(34, 58, "g ≈ 0", 10, BLUE, 700),
    "adapt_curve": lambda: curve() + label(80, 88, "few-shot adaptation", 9.5),
    "gravity_eval": lambda: g_arrow(34, 18, 0) + g_arrow(76, 18, 18, "") + g_arrow(118, 18, 36, "")
        + check(34, 70) + check(76, 70) + cross(118, 70),
    # 3 corrector
    "actor": lambda: table() + arm((24, 80), (36, 32), (70, 40)) + cube(92, 72, 12) + vla(98, 14, 52, 22, "Actor"),
    "corrector": lambda: vla(14, 30, 64, 26, "Corrector", BLUE) + magnifier(112, 40) + cube(112, 40, 9),
    "correction": lambda: bubble(16, 16, 128, 34, "“lower, then left”", 12) + label(80, 80, "or an embedding-level nudge", 9.5),
    "corrected": lambda: table() + arm((24, 80), (36, 34), (82, 62)) + cube(96, 72, 12) + check(130, 30, 1.3),
    # 4 metric grounding
    "volume": lambda: wire_box() + label(130, 36, "corner", 9.5, ORANGE, 600, "start"),
    "metric_cmd": lambda: bubble(14, 6, 132, 30, "“move 2 inches left”", 11) + ruler(40, 62),
    "auto_label": lambda: cards(36, 14) + label(80, 86, "labels from end-effector motion", 9.5),
    "metric_vla": lambda: vla(16, 14, 56, 24) + '<path d="M76 26 h14" stroke="#8a929c" stroke-width="2"/><path d="M86 22 l5 4 l-5 4" fill="none" stroke="#8a929c" stroke-width="2"/>'
        + table(80, 96, 150) + post(108, 50) + cube(108, 43, 12) + label(44, 62, "non-metric", 9.5) + label(44, 74, "spatial tasks", 9.5),
    # 5 space generalist
    "space_data": lambda: cylinder(22, 26) + cube(112, 34, 14, RED, 25) + satellite(112, 66),
    "benchmark": lambda: grid(46, 14) + label(80, 86, "tasks × gravity × lighting", 9.5),
    "pretrain": lambda: vla(48, 34, 64, 26, "VLA") + cube(32, 18, 10) + '<circle cx="80" cy="16" r="6" fill="#3bb36b"/>'
        + cube(128, 18, 10, BLUE, 30) + f'<path d="M36 26 L60 34 M80 23 V34 M124 26 L100 34" stroke="{GRAY}" stroke-width="1.4"/>',
    "space_ops": lambda: planet(36, 62, 22) + satellite(104, 30) + arm((76, 76), (90, 52), (100, 40), "#c9ced5"),
    # 6 curriculum
    "c_zero": lambda: table() + walls(46, 14, 68, 64) + floating(80, 36) + g_arrow(130, 22, 0),
    "c_low": lambda: table() + cube(80, 54, 14) + shadow(80) + g_arrow(124, 26, 16, "g/6"),
    "c_earth": lambda: table() + cube(80, 72, 14) + g_arrow(124, 18, 40, "g"),
    "c_vary": lambda: table() + cube(56, 72, 14) + cube(104, 70, 18, BLUE) + label(56, 50, "μ", 13, DARK, 700) + label(104, 50, "kg", 12, DARK, 700)
        + f'<path d="M44 82 h24" stroke="{DARK}" stroke-width="1.4" stroke-dasharray="2 2"/>',
    # 7 energy
    "demos": lambda: cards(36, 14),
    "eff_score": lambda: f'<polyline points="16,70 30,30 44,62 58,22 72,58 86,20 100,52 116,26 144,40" fill="none" stroke="{RED}" stroke-width="2" opacity=".8"/>'
        + f'<path d="M16 70 C 60 70, 100 40, 144 40" fill="none" stroke="{BLUE}" stroke-width="3"/>' + label(80, 88, "wasted motion vs efficient path", 9.5),
    "filter": lambda: funnel(55, 12) + dots([(62, 6), (76, 8), (92, 6), (104, 9)], GRAY, 3) + dots([(80, 62)], BLUE, 4),
    "efficient": lambda: vla(18, 32, 56, 26) + battery(94, 34),
    # 8 world-model minigames
    "world_model": lambda: vla(26, 20, 108, 34, "world model", "#4b525a") + label(80, 74, "learned from robot video", 9.5),
    "minigame": lambda: f'<circle cx="122" cy="40" r="16" fill="none" stroke="{RED}" stroke-width="3"/><circle cx="122" cy="40" r="8" fill="none" stroke="{RED}" stroke-width="3"/>'
        + f'<path d="M30 70 Q 70 6 112 38" fill="none" stroke="{GRAY}" stroke-dasharray="3 3"/>' + '<circle cx="30" cy="70" r="6" fill="#2a78d6"/>',
    "imagined_practice": lambda: cloud(26, 12, 108, 56) + vla(58, 32, 44, 20, "VLA") + label(80, 86, "cheap imagined rollouts", 9.5),
    "transfer": lambda: table() + arm((24, 80), (40, 30), (84, 48)) + cube(98, 72, 12) + label(124, 24, "sim → real", 10, DARK, 600),
    # 9 imagine-act
    "instruction": lambda: frame(16, 34, 54, 40, table(68, 20, 66) + cube(44, 60, 10)) + bubble(78, 8, 70, 26, "“stack it”", 10.5),
    "imagine": lambda: cloud(26, 10, 108, 64) + frame(58, 28, 44, 32, cube(80, 48, 9) + cube(80, 39, 9, BLUE)),
    "act": lambda: table() + arm((24, 80), (40, 30), (88, 56)) + cube(102, 72, 12) + cube(102, 60, 12, BLUE),
    "check_imag": lambda: frame(16, 22, 50, 38, cube(41, 46, 10) + cube(41, 36, 10, BLUE)) + frame(94, 22, 50, 38, cube(119, 46, 10) + cube(124, 37, 10, BLUE, 20))
        + label(80, 46, "≈ ?", 13, DARK, 700),
    # 10 VLM judge
    "agent_envs": lambda: frame(18, 16, 56, 44, label(46, 44, "&lt;/&gt;", 16, BLUE, 700)) + frame(86, 28, 56, 44, label(114, 56, "&lt;/&gt;", 16, BLUE, 700)),
    "rollouts": lambda: frame(26, 14, 108, 62, table(68, 32, 128) + cube(70, 60, 10) + f'<path d="M96 32 l14 9 l-14 9 z" fill="{BLUE}"/>'),
    "vlm_judge": lambda: vla(14, 30, 58, 26, "VLM", BLUE) + check(100, 30) + cross(130, 30) + check(100, 64) + check(130, 64),
    "library": lambda: cylinder(58, 18, 46, 46) + label(80, 88, "curated environments", 9.5),
}


def moon(x, y, r):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#c9ced5" stroke="#8a929c"/>'
            f'<circle cx="{x - r * .35}" cy="{y - r * .2}" r="{r * .22}" fill="#b1b7bf"/>'
            f'<circle cx="{x + r * .3}" cy="{y + r * .3}" r="{r * .15}" fill="#b1b7bf"/>')


def module(x, y, w, h):
    """ISS-like module interior: rounded tube with handrails and racks."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2.6}" fill="#eef0f3" stroke="{DARK}" stroke-width="1.4"/>'
            + "".join(f'<rect x="{x + 10 + i * (w - 20) / 4}" y="{y + 6}" width="{(w - 20) / 4 - 4}" height="{h * .32}" fill="#d5d9de"/>'
                      for i in range(4))
            + f'<path d="M{x + 12} {y + h * .62} h{w - 24}" stroke="#e0a63a" stroke-width="2.4"/>')


ART.update({
    "space_footage": lambda: frame(14, 12, 132, 66, module(22, 20, 116, 50) + cube(96, 56, 9, RED, 25)
        + f'<path d="M60 48 l12 7 l-12 7 z" fill="{BLUE}"/>') + label(80, 88, "real ISS footage", 9.5),
    "action_labels": lambda: "".join(frame(14 + i * 46, 22, 38, 28, cube(33 + i * 46, 38, 8)) + label(33 + i * 46, 66, "a = ?", 10, ORANGE, 700)
        for i in range(3)) + label(80, 86, "inferred actions", 9.5),
    "space_wm": lambda: vla(14, 30, 86, 30, "world model", "#4b525a") + moon(128, 44, 18),
    "space_practice": lambda: module(12, 24, 82, 42) + vla(104, 30, 48, 24, "VLA") + cube(52, 50, 8, RED, 20),
})


def checklist(x, y, rows=(1, 1, 0)):
    out = ""
    for i, ok in enumerate(rows):
        yy = y + i * 18
        out += f'<rect x="{x}" y="{yy}" width="12" height="12" rx="2" fill="#fff" stroke="{GRAY}"/>'
        out += (check(x + 7, yy + 7, .55) if ok else cross(x + 6, yy + 6, .45))
        out += f'<path d="M{x + 18} {yy + 6} h34" stroke="#cfd4da" stroke-width="3"/>'
    return out


ART.update({
    "env_tests": lambda: frame(12, 16, 70, 56, walls(20, 24, 54, 40) + table(66, 18, 76) + cube(46, 40, 9)) + checklist(94, 20)
        + label(80, 86, "environment + behavioral tests", 9.5),
    "redteam": lambda: "".join(f'<circle cx="{26 + i * 36}" cy="32" r="10" fill="#eef0f3" stroke="{DARK}" stroke-width="1.4"/>'
        + label(26 + i * 36, 36, t, 9, DARK, 700) for i, t in enumerate(["0", "rnd", "scr", "RL"]))
        + f'<path d="M20 52 H140" stroke="{GRAY}" stroke-dasharray="3 3"/>' + label(80, 68, "reward exploit found?", 10, RED, 700)
        + label(80, 84, "probe policies", 9.5),
})


def svg(key):
    return f'<svg class="art" viewBox="0 0 160 90" role="img" aria-hidden="true">{ART[key]()}</svg>'


# >>> metric-grounding cards (2026-10-23) >>>
def target(x, y, r=7):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{GREEN}" stroke-width="2" stroke-dasharray="3 2"/>'
            f'<path d="M{x - 3} {y} h6 M{x} {y - 3} v6" stroke="{GREEN}" stroke-width="1.6"/>')


ART.update({
    "scripted_label": lambda: table() + arm((22, 80), (36, 32), (70, 40))
    + f'<path d="M74 40 L118 24" stroke="{BLUE}" stroke-width="2" stroke-dasharray="4 3"/>'
    + f'<path d="M112 22 l7 2 l-5 5" fill="none" stroke="{BLUE}" stroke-width="2"/>'
    + label(108, 54, "5 cm", 10.5, BLUE, 700),
    "iss_float": lambda: module(10, 18, 140, 56) + cube(96, 40, 13, RED, 22),
    "space_metric_cmd": lambda: bubble(8, 6, 144, 30, "“10 cm in front of the rack”", 10.5) + module(30, 52, 100, 32),
    "goal_episode": lambda: module(10, 18, 140, 56) + cube(52, 50, 10, RED, 20) + target(112, 36)
    + f'<path d="M58 46 L104 38" stroke="{GRAY}" stroke-width="1.6" stroke-dasharray="3 3"/>',
    "placed_check": lambda: module(10, 18, 140, 56) + cube(112, 36, 10, RED, 0) + target(112, 36, 10) + check(52, 50, 1.3),
})
# <<< metric-grounding cards <<<
