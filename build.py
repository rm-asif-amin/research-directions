"""Builds index.html for the research-directions page. Edit the IDEAS list, then run: python build.py"""
import html
import pathlib

HERE = pathlib.Path(__file__).parent
PROJECT = "https://rm-asif-amin.github.io/zerograv-manipulation-site/"
SCHOLAR = "https://scholar.google.com/citations?user=d04IKHkAAAAJ&hl=en"


def ref(label, url):
    return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'


# Each idea: number, short id, title, status (label, css class), one-line idea, flow steps [(title, detail)],
# flow note (optional), prior work (html), novel angle (html), loop (draw a feedback arrow under the flow).
IDEAS = [
    dict(n=1, id="zero-g", title="Zero-gravity training for better performance on Earth",
         status=("in progress", "real"),
         idea=f"Train robot experts with gravity switched off until they touch the object, then distill their "
              f"spatially diverse demonstrations into VLAs to improve ordinary, Earth-gravity manipulation. "
              f"{ref('Project page', PROJECT)}.",
         flow=[("Zero-G RL experts", "objects float until touched; gravity then switches on"),
               ("Diverse demonstrations", "reaching, grasping and pushing throughout 3D space"),
               ("VLA distillation", "fine-tune a VLA (π0.5) on the demonstrations"),
               ("Earth-gravity tests", "spatially harder versions of the same tasks")],
         note="Compared against fixed and adaptive gravity randomization (OpenAI-style ADR) at the same cost.",
         prior=f"Domain randomization varies physics as a robustness perturbation, around Earth gravity "
               f"({ref('OpenAI et al., 2019', 'https://arxiv.org/abs/1910.07113')}).",
         novel="Gravity as a controllable distribution shift that is used as the main training regime, not as a "
               "perturbation. Preliminary results: at heights only the zero-gravity experts trained on, they reach the "
               "object 3.4&times; and grasp it 4.2&times; as often as the best gravity-trained or gravity-randomized "
               "expert."),
    dict(n=2, id="earth-to-space", title="Adapting Earth-trained VLAs to microgravity",
         status=("planned", "wip"),
         idea="The reverse direction: take a VLA trained on Earth-gravity data and make it work when the physics "
              "changes, as in orbit.",
         flow=[("Earth-trained VLA", "pretrained, terrestrial data"),
               ("Microgravity tasks", "same scenes, different dynamics"),
               ("Adaptation", "few-shot fine-tuning, dynamics-aware conditioning"),
               ("Altered-gravity evaluation", "measure what breaks and what transfers")],
         prior=f"Space-domain work has so far adapted models to visual or task shift under Earth-like dynamics: "
               f"OpenVLA fine-tuned for in-orbit inspection "
               f"({ref('VLMs as Operator Agents in the Space Domain, 2025', 'https://arxiv.org/abs/2501.07802')}); lunar autonomy with a "
               f"fine-tuned vision-language agent and lighting adaptation "
               f"({ref('SELENE', 'https://doi.org/10.3390/astronautics1030015')}).",
         novel="A <b>dynamics</b> shift rather than a visual one, with VLA manipulation actually evaluated under "
               "altered gravity."),
    dict(n=3, id="corrector", title="A corrector VLA: actor and critic co-trained",
         status=("proposed", "wip"),
         idea="A second VLA watches the first one act and corrects it, either in language (&ldquo;move left&rdquo;) "
              "or directly in embedding space. The two are trained together.",
         flow=[("Actor VLA", "proposes an action chunk"),
               ("Corrector VLA", "sees the observation and the proposed chunk"),
               ("Correction", "language (&ldquo;lower, then left&rdquo;) or an embedding-level adjustment"),
               ("Corrected action", "executed; outcomes train both models")],
         loop="outcomes feed back into both models",
         prior=f"Adversarial imitation trains a discriminator against the policy "
               f"({ref('GAIL', 'https://arxiv.org/abs/1606.03476')}, "
               f"{ref('DAC', 'https://arxiv.org/abs/1809.02925')}). Language corrections from <i>humans</i> steer "
               f"policies at run time ({ref('&ldquo;No, to the Right&rdquo;', 'https://arxiv.org/abs/2301.02555')}; "
               f"{ref('CorrectVLA', 'https://correctvla.github.io/')}), and an expert teacher can distill into a VLA "
               f"on-policy ({ref('VLA-OPD', 'https://arxiv.org/abs/2603.26666')}).",
         novel="A co-trained <i>peer</i> that fixes failures from out-of-distribution physics, where no human or "
               "ground-truth teacher is available. Zero gravity is the driving case."),
    dict(n=4, id="metric", title="Metric language grounding inside containment volumes",
         status=("proposed", "wip"),
         idea="Train VLAs on commands with real units and 3D references, such as &ldquo;move 2 inches left&rdquo; "
              "or &ldquo;go to the top-right front corner of the box&rdquo;, to sharpen their spatial ability.",
         flow=[("Containment volume", "a known 3D frame around the workspace"),
               ("Metric commands", "distances, directions and volume-relative positions"),
               ("Auto-labeled demonstrations", "labels computed from end-effector motion"),
               ("Metric-supervised VLA", "tested on ordinary, non-metric spatial tasks")],
         prior=f"Direction-only language motions ({ref('RT-H', 'https://arxiv.org/abs/2403.01823')}); metric "
               f"spatial reasoning in vision-language models rather than action models "
               f"({ref('SpatialVLM', 'https://arxiv.org/abs/2401.12168')}, "
               f"{ref('RoboTracer', 'https://arxiv.org/abs/2512.13660')}); language-to-slot placement through a "
               f"rendered visual goal ({ref('AnySlot', 'https://arxiv.org/abs/2604.10432')}).",
         novel="End-to-end metric supervision of the action model, tested for transfer to non-metric tasks, plus "
               "references relative to a 3D volume. Without a table or a &ldquo;down&rdquo;, volume-relative "
               "metric commands are how you would instruct a robot in space."),
    dict(n=5, id="space-vla", title="A generalist VLA for space manipulation",
         status=("long-term vision", "wip"),
         idea="A pretrained, multi-task VLA for manipulation in space: a &ldquo;π0.5 for space&rdquo;.",
         flow=[("Space-manipulation dataset", "simulation plus analog hardware"),
               ("Benchmark", "tasks &times; gravity &times; lighting"),
               ("Multi-task pretraining", "one model across tasks and conditions"),
               ("Space operations", "servicing, assembly, sampling")],
         prior=f"Existing space work fine-tunes for single tasks "
               f"({ref('VLMs as Operator Agents in the Space Domain, 2025', 'https://arxiv.org/abs/2501.07802')}; "
               f"{ref('SELENE', 'https://doi.org/10.3390/astronautics1030015')}).",
         novel="To my knowledge no generalist exists yet. The bottleneck is data, so a space-manipulation dataset "
               "and benchmark is the most valuable first step."),
    dict(n=6, id="curriculum", title="Physics curricula",
         status=("early idea", "wip"),
         idea="Schedule the physics itself during training: start where exploration is easy (zero gravity, low "
              "friction) and move toward the target physics as the policy improves.",
         flow=[("Zero gravity", "easy exploration of 3D space"),
               ("Reduced gravity", "partial support"),
               ("Earth gravity", "the target task"),
               ("Varied friction and mass", "robustness at the end")],
         prior=f"Automatic domain randomization widens physics ranges as performance improves "
               f"({ref('OpenAI et al., 2019', 'https://arxiv.org/abs/1910.07113')}).",
         novel="Ordering physics regimes by how much they help exploration, rather than widening one range "
               "around Earth values."),
    dict(n=7, id="energy", title="Energy-aware action trajectories",
         status=("early idea", "wip"),
         idea="Train VLAs to avoid redundant motion: score demonstrations and action chunks by energy and wasted "
              "movement, and prefer efficient ones.",
         flow=[("Demonstrations", "from experts or teleoperation"),
               ("Efficiency scoring", "joint work, jerk, path length, idle motion"),
               ("Filtering and regularization", "keep or up-weight efficient behavior"),
               ("Efficient VLA", "smoother, faster, lower-power execution")],
         prior="Smoothness and energy terms are common in RL reward shaping and trajectory optimization, while VLA "
               "training data is usually left unfiltered for efficiency.",
         novel="Efficiency as a data-quality axis for VLA training, which matters most where power is scarce, as "
               "in space."),
    dict(n=8, id="minigames", title="World-model &ldquo;zero-g minigames&rdquo; for VLA practice",
         status=("early idea", "wip"),
         idea="Learn a world model of zero-gravity dynamics, then let VLAs practice short, game-like tasks inside it.",
         flow=[("World model", "learned zero-gravity dynamics"),
               ("Minigames", "catch, stabilize, push to a target"),
               ("Practice in imagination", "cheap rollouts for the VLA"),
               ("Transfer", "to simulation, then hardware")],
         prior=f"Agents trained inside learned world models "
               f"({ref('DreamerV3', 'https://arxiv.org/abs/2301.04104')}); learned interactive simulators "
               f"({ref('UniSim', 'https://arxiv.org/abs/2310.06114')}, "
               f"{ref('Genie', 'https://arxiv.org/abs/2402.15391')}).",
         novel="Targeted, game-like curricula for an unfamiliar physics regime, where real data is hardest to get."),
    dict(n=9, id="imagineact", title="ImagineAct: visualize before acting",
         status=("early idea", "wip"),
         idea="A VLA that first imagines the outcome, as a predicted image or subgoal, and then acts toward it.",
         flow=[("Instruction and observation", ""),
               ("Imagine", "predict a future frame or subgoal image"),
               ("Act", "action chunk conditioned on the imagined goal"),
               ("Check", "compare imagination with what happened")],
         prior=f"Goal-image generation for control ({ref('SuSIE', 'https://arxiv.org/abs/2310.10639')}); video "
               f"prediction as a policy ({ref('UniPi', 'https://arxiv.org/abs/2302.00111')}); video-pretrained "
               f"manipulation policies ({ref('GR-1', 'https://arxiv.org/abs/2312.13139')}).",
         novel="Using the gap between imagination and outcome as a signal, for example to detect when the physics "
               "differs from what the model expects."),
    dict(n=10, id="vlm-judge", title="VLMs as judges of agent-generated environments",
         status=("early idea", "wip"),
         idea="Let language-model agents generate simulation environments and tasks, and use a vision-language "
              "model to judge which ones are valid, solvable and useful.",
         flow=[("Agent-generated environments", "scenes and tasks written as code"),
               ("Rendered rollouts", "what the environment actually does"),
               ("VLM judge", "physically valid? solvable? diverse?"),
               ("Curated library", "training environments for VLAs")],
         prior=f"Generative simulation and task generation "
               f"({ref('RoboGen', 'https://arxiv.org/abs/2311.01455')}, "
               f"{ref('GenSim', 'https://arxiv.org/abs/2310.01361')}); LLM-written reward code "
               f"({ref('Eureka', 'https://arxiv.org/abs/2310.12931')}).",
         novel="Visual verification of generated environments, catching the physics and geometry bugs that "
               "text-only checks miss."),
]


def flow_html(steps, loop=None):
    parts = []
    for i, (t, d) in enumerate(steps):
        if i:
            parts.append('<div class="arrow" aria-hidden="true"></div>')
        parts.append(f'<div class="step{" first" if i == 0 else ""}"><div class="k">{i + 1}</div>'
                     f'<div class="t">{t}</div>' + (f'<div class="d">{d}</div>' if d else "") + "</div>")
    out = '<div class="flow" role="img">' + "".join(parts) + "</div>"
    if loop:
        out += f'<div class="loop"><span>&#8634; {loop}</span></div>'
    return out


def idea_html(x):
    label, cls = x["status"]
    note = f'<p class="flow-note">{x["note"]}</p>' if x.get("note") else ""
    return f'''
<section id="{x["id"]}">
  <div class="container">
    <p class="rq">Idea {x["n"]}</p>
    <h3 class="idea-title">{x["title"]} <span class="badge {cls}">{label}</span></h3>
    <p class="idea-line">{x["idea"]}</p>
    {flow_html(x["flow"], x.get("loop"))}
    {note}
    <div class="pn">
      <div><h4>Prior work</h4><p>{x["prior"]}</p></div>
      <div><h4>What would be new</h4><p>{x["novel"]}</p></div>
    </div>
  </div>
</section>'''


core = [x for x in IDEAS if x["n"] <= 5]
more = [x for x in IDEAS if x["n"] > 5]
toc = "".join(f'<a href="#{x["id"]}">{x["n"]}. {html.unescape(x["title"]).split(":")[0]}</a>' for x in IDEAS)

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Research Directions</title>
  <meta name="description" content="Research directions in robot learning under altered physics: zero-gravity training, space manipulation and spatially grounded vision-language-action models.">
  <meta name="robots" content="noindex">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Castoro&family=Noto+Sans:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="static/css/style.css?v=1">
  <link rel="stylesheet" href="static/css/ideas.css?v=1">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='13' fill='%232a78d6'/%3E%3Ccircle cx='16' cy='16' r='5' fill='white'/%3E%3C/svg%3E">
</head>
<body>
<header class="hero">
  <div class="container">
    <h1>Robot learning <span class="accent">beyond Earth&rsquo;s physics</span></h1>
    <div class="authors"><span><a href="{SCHOLAR}" target="_blank" rel="noopener">Asif Amin</a></span></div>
    <div class="affils"><span>University of California, Riverside</span></div>
    <div class="links">
      <a class="btn" href="{PROJECT}" target="_blank" rel="noopener">Current project: Learning in Zero Gravity</a>
      <a class="btn" href="{SCHOLAR}" target="_blank" rel="noopener">Google Scholar</a>
    </div>
    <div class="tldr">
      Vision-language-action models (VLAs) learn from data collected under Earth&rsquo;s physics, mostly on a
      tabletop. I study what happens when that physics changes, and how to use altered physics on purpose:
      as a source of more diverse training data, as a test of how well VLAs adapt, and as the setting for
      robots that will one day work in space.
    </div>
  </div>
</header>

<main>
<section id="arc">
  <div class="container">
    <h2>How the ideas fit together</h2>
    <div class="arc">
      <div class="col"><div class="h">The problem</div><p>VLAs break under altered physics, and altered physics can also help train them.</p><div class="chips"><a href="#zero-g">1</a><a href="#earth-to-space">2</a></div></div>
      <div class="arrow" aria-hidden="true"></div>
      <div class="col"><div class="h">Methods</div><p>Correcting failures without a teacher, and grounding language in metric 3D space.</p><div class="chips"><a href="#corrector">3</a><a href="#metric">4</a></div></div>
      <div class="arrow" aria-hidden="true"></div>
      <div class="col"><div class="h">The vision</div><p>A generalist VLA for manipulation in space.</p><div class="chips"><a href="#space-vla">5</a></div></div>
    </div>
    <p class="arc-note">Ideas 6&ndash;10 are earlier-stage directions that support this arc: curricula, efficiency,
      world models, imagination and environment generation.</p>
    <nav class="toc ideas-toc" aria-label="Ideas">{toc}</nav>
  </div>
</section>
{"".join(idea_html(x) for x in core)}
<section class="divider"><div class="container"><h2>Further directions</h2>
  <p class="center muted">Earlier-stage ideas. Each one connects to the arc above.</p></div></section>
{"".join(idea_html(x) for x in more)}
</main>
<footer><div class="container">Asif Amin &middot; University of California, Riverside &middot;
  <a href="{SCHOLAR}" target="_blank" rel="noopener">Google Scholar</a></div></footer>
</body>
</html>
'''
(HERE / "index.html").write_text(page)
print("wrote", HERE / "index.html")
