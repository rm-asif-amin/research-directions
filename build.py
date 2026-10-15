"""Builds index.html for the research-directions page. Edit the IDEAS list, then run: python build.py"""
import html
import pathlib

from art import svg

HERE = pathlib.Path(__file__).parent
PROJECT = "https://rm-asif-amin.github.io/zerograv-manipulation-site/"
SCHOLAR = "https://scholar.google.com/citations?user=d04IKHkAAAAJ&hl=en"


def ref(label, url):
    return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'


# Each idea: number, short id, title, status (label, css class), one-line idea, flow steps [(title, detail)],
# flow note (optional), prior work (html), novel angle (html), loop (draw a feedback arrow under the flow).
IDEAS = [
    dict(n=1, group="main", id="zero-g", title="Zero-gravity training for better performance on Earth",
         status=("in progress", "real"),
         art=['zg_expert', 'zg_demos', 'vla_distill', 'platform_test'],
         sim="Change the simulator's physics: switching gravity off turns ordinary tabletop tasks into data that covers the whole 3D workspace.",
         idea=f"Train robot experts with gravity switched off until they touch the object, then distill their "
              f"spatially diverse demonstrations into VLAs to improve ordinary, Earth-gravity manipulation. "
              f"{ref('Project page', PROJECT)}.",
         mech="Switching gravity off is not enough on its own: a floating object drifts out of reach, and in pure "
              "zero gravity policies exploit the floating object instead of learning the skill. I built two mechanisms "
              "that make it trainable. <b>Selective containment volumes</b>: thin walls that block the floating object "
              "but not the robot arm (separate collision groups), are invisible to cameras, and can release when the "
              "task needs it. <b>Gravity that switches on at contact or grasp</b>: the object floats while the robot "
              "explores, and the task itself is finished under normal gravity. Gravity is controlled per environment "
              "inside one GPU-simulated batch, so thousands of parallel environments each switch at their own moment.",
         flow=[("Zero-G RL experts", "objects float until touched; gravity then switches on"),
               ("Diverse demonstrations", "reaching, grasping and pushing throughout 3D space"),
               ("VLA distillation", "fine-tune a VLA (π0.5) on the demonstrations"),
               ("Earth-gravity tests", "spatially harder versions of the same tasks")],
         note="Compared against fixed and adaptive gravity randomization (OpenAI-style ADR) at the same cost. Next step: a "
              "<b>physics curriculum</b> that schedules the simulator&rsquo;s physics (zero gravity, then reduced, then Earth "
              "gravity, then varied friction and mass) by how much each regime helps exploration, rather than widening one "
              "range around Earth values.",
         prior=f"Domain randomization varies physics as a robustness perturbation, around Earth gravity "
               f"({ref('OpenAI et al., 2019', 'https://arxiv.org/abs/1910.07113')}).",
         novel="Gravity as a controllable distribution shift that is used as the main training regime, not as a "
               "perturbation. Preliminary results: at heights only the zero-gravity experts trained on, they reach the "
               "object 3.4&times; and grasp it 4.2&times; as often as the best gravity-trained or gravity-randomized "
               "expert."),
    dict(n=2, group="main", id="metric", title="Metric language grounding inside containment volumes",
         status=("proposed", "wip"),
         art=['volume', 'metric_cmd', 'auto_label', 'metric_vla'],
         sim="The simulator knows exact positions, so metric language labels come for free from its state.",
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
    dict(n=3, group="main", id="minigames", title="World-model minigames for agile skills",
         status=("early idea", "wip"),
         art=['world_model', 'minigame', 'imagined_practice', 'transfer'],
         sim="World models make game content cheap: endless scenes and tasks from a prompt or an image, where a "
             "hand-built simulator needs every scene and asset authored.",
         idea="Use learned world models to generate short, game-like tasks that demand speed and reaction (catching, "
              "intercepting a moving target, stabilizing a tumbling object) and let VLAs practice them. Such skills are "
              "richer than the slow, quasi-static tasks most robot data contains.",
         flow=[("World model", "action-conditioned, learned from robot video"),
               ("Minigames", "catch, intercept, stabilize"),
               ("Practice in imagination", "fast, cheap rollouts for the VLA"),
               ("Transfer", "to simulation, then hardware")],
         prior=f"Imitation policies trained entirely on demonstrations collected inside a learned world simulator, "
               f"on tasks such as pushing, rope routing, grasping and sweeping "
               f"({ref('Interactive World Simulator, RSS 2026', 'https://arxiv.org/abs/2603.08546')}); controllable "
               f"world models for policy evaluation and improvement "
               f"({ref('Ctrl-World', 'https://arxiv.org/abs/2510.10125')}); policy refinement inside diffusion world "
               f"models ({ref('World4RL', 'https://arxiv.org/abs/2509.19080')}); synthetic robot trajectories from "
               f"video world models ({ref('DreamGen', 'https://arxiv.org/abs/2505.12705')}). Generated, playable game "
               f"worlds exist, but for 2D platformer games rather than robots "
               f"({ref('Genie', 'https://arxiv.org/abs/2402.15391')}).",
         novel=f"Agile skills are starting to get attention, as policies for moving targets "
               f"({ref('DynamicWAM', 'https://arxiv.org/abs/2608.00793')}) and as world models for state estimation in "
               f"agile humanoid tasks ({ref('HAIC', 'https://arxiv.org/abs/2602.11758')}), but not as practice generated "
               f"inside a world model. The open question is whether world models capture fast dynamics faithfully "
               f"enough to train on: they already struggle to follow actions unlike their training data "
               f"({ref('Do Robotic World Models Really Follow Actions?', 'https://arxiv.org/abs/2608.24885')})."),
    dict(n=4, group="main", id="vlm-judge", title="Behavior-verified environment generation",
         status=("proposed", "wip"),
         art=['agent_envs', 'env_tests', 'redteam', 'library'],
         sim="Generated environments become a trustworthy source of experience: each one comes with evidence that "
             "it behaves as intended and cannot be gamed.",
         idea="An agent that generates simulation environments together with executable behavioral tests, and "
              "red-teams each environment&rsquo;s reward with cheap probe policies before any policy trains on it. "
              "Environments are kept only when they behave as intended.",
         exp="I designed the zero-gravity versions of eight ManiSkill3 tasks for my current project: containment "
             "walls that block the floating object but not the robot arm, and gravity that switches on at contact or "
             "grasp. The hardest bugs were behavioral, and none were visible in the scene itself: objects tunneling "
             "through thin walls, a physics material silently shared between objects and walls, a contact trigger "
             "firing on stale data right after a reset, and two reward exploits (a pose reward collectible while the "
             "object simply floated, and a lifting task counted as solved without the object ever being grasped). "
             "Each of these maps to an automatic test or a probe policy. Agent-generated environments will have the "
             "same kinds of bugs, at a scale no person can audit by hand.",
         flow=[("Task in language", "the environment to build"),
               ("Environment and tests", "scene, physics and executable behavioral checks"),
               ("Red-team probes", "zero, random, scripted and short-RL policies try to game the reward"),
               ("Verified library", "environments that pass, each with its evidence")],
         prior=f"Agentic environment generation that checks the specification and layout of evaluation scenes "
               f"({ref('Isaac Lab-Arena, experimental, 2026', 'https://github.com/isaac-sim/IsaacLab-Arena')}); task and scene generation "
               f"({ref('RoboGen', 'https://arxiv.org/abs/2311.01455')}, "
               f"{ref('GenSim', 'https://arxiv.org/abs/2310.01361')}), where people still check generated tasks by "
               f"watching rendered videos; critics that review generated scenes and data for layout, silent failures "
               f"and static physical plausibility ({ref('SceneSmith', 'https://arxiv.org/abs/2602.09153')}, "
               f"{ref('V-CAGE', 'https://arxiv.org/abs/2604.09036')}, "
               f"{ref('Code2Worlds-2', 'https://arxiv.org/abs/2610.17651')}); LLM-written reward code "
               f"({ref('Eureka', 'https://arxiv.org/abs/2310.12931')}).",
         novel="Checking how a generated environment <b>behaves</b>, not only how it looks: executable invariants "
               "plus reward red-teaming before training, for any simulator and any physics. Because the tests state "
               "the physics an environment is meant to have, unusual physics such as zero gravity is checked "
               "correctly instead of being flagged as a bug. A natural first project builds on the open-source "
               "Isaac Lab-Arena generator and measures how many hidden bugs and exploits the agent catches compared "
               "with a human audit, and whether policies trained on verified environments do better."),
    dict(n=5, group="main", id="imagineact", title="Imagination-guided experience generation",
         status=("early idea", "wip"),
         art=['imagine', 'act', 'check_imag', 'agent_envs'],
         sim="Spend simulation on the experience the model cannot yet predict, instead of sampling scenes "
             "uniformly.",
         idea="A VLA imagines the outcome before it acts. Where the imagined and the simulated outcome disagree, it "
              "has found experience it cannot yet predict, and that gap decides which environments, tasks and physics "
              "the generator of idea 4 produces next. At deployment, the same gap signals that the world itself has "
              "changed, for example a different gravity, and triggers adaptation.",
         flow=[("Imagine", "predict the outcome of an action chunk"),
               ("Act in simulation", "observe what actually happens"),
               ("Surprise", "the gap between imagination and outcome"),
               ("Generate more of it", "environments, tasks and physics where the gap is large")],
         loop="the improved model imagines again",
         prior=f"Imagining before acting with goal images or video ({ref('SuSIE', 'https://arxiv.org/abs/2310.10639')}, "
               f"{ref('UniPi', 'https://arxiv.org/abs/2302.00111')}, {ref('GR-1', 'https://arxiv.org/abs/2312.13139')}); "
               f"prediction error as curiosity for choosing actions "
               f"({ref('ICM', 'https://arxiv.org/abs/1705.05363')}, "
               f"{ref('Plan2Explore', 'https://arxiv.org/abs/2005.05960')}); generating training environments by "
               f"regret or novelty ({ref('PAIRED', 'https://arxiv.org/abs/2012.02096')}, "
               f"{ref('POET', 'https://arxiv.org/abs/1901.01753')}); world models that flag task failures "
               f"({ref('Foresight', 'https://arxiv.org/abs/2606.23085')}).",
         novel="Using a VLA&rsquo;s own imagination error to choose which <i>environments</i> to generate, at the "
               "level of tasks and physics rather than individual actions, so the simulator produces the experience "
               "the model most needs. The same signal doubles as a detector that the physics has changed at "
               "deployment, where world models have so far been used to flag task failures."),
    dict(n=6, group="space", id="earth-to-space", title="Adapting Earth-trained VLAs to microgravity",
         status=("planned", "wip"),
         art=['earth_vla', 'micro_tasks', 'adapt_curve', 'gravity_eval'],
         sim="Reuse the same simulated tasks with new dynamics, to measure and train adaptation before any orbital hardware exists.",
         idea="The reverse direction: take a VLA trained on Earth-gravity data and make it work when the physics "
              "changes, as in orbit.",
         flow=[("Earth-trained VLA", "pretrained, terrestrial data"),
               ("Microgravity tasks", "same scenes, different dynamics"),
               ("Adaptation", "few-shot fine-tuning, dynamics-aware conditioning"),
               ("Altered-gravity evaluation", "measure what breaks and what transfers")],
         prior=f"VLM and VLA work for space has so far been tested under Earth gravity: VLMs as operator agents, "
               f"including OpenVLA fine-tuned on a lab robot arm to inspect satellite hardware "
               f"({ref('Carrasco et al., 2025', 'https://arxiv.org/abs/2501.07802')}); a lunar autonomy architecture "
               f"whose VLA, adapted from 100 teleoperated demonstrations, succeeds on 29 of 30 in-domain trials on a "
               f"physical lunar robot prototype, with only its traversal policy trained in simulated lunar gravity "
               f"({ref('SELENE, Tsinghua, 2026', 'https://doi.org/10.3390/astronautics1030015')}).",
         novel="A <b>dynamics</b> shift rather than a visual one, with VLA manipulation actually evaluated under "
               "altered gravity."),
    dict(n=7, group="space", id="space-world-model", title="World models of the ISS and lunar workspaces",
         status=("proposed", "wip"),
         art=['space_footage', 'action_labels', 'space_wm', 'space_practice'],
         sim="Turn existing footage of space workspaces into an interactive practice environment, where building a "
             "faithful simulator by hand is the bottleneck.",
         idea="Learn action-conditioned world models of real space workspaces, such as the interior of the "
              "International Space Station or lunar terrain, so VLAs can practice where hand-built simulators are "
              "hardest to make.",
         flow=[("Real space footage", "ISS interior video, free-flyer cameras, lunar imagery"),
               ("Inferred actions", "inverse-dynamics or latent-action labels"),
               ("Workspace world model", "action-conditioned and visually faithful"),
               ("VLA practice", "a training ground for a generalist space VLA")],
         prior=f"Space robot learning so far relies on hand-built simulators: an RL controller trained in NVIDIA "
               f"Isaac Lab flew NASA&rsquo;s {ref('Astrobee', 'https://ntrs.nasa.gov/citations/20260001396')} free-flyer, "
               f"the first RL control of a free-flyer aboard the ISS ({ref('APIARY', 'https://arxiv.org/abs/2512.03729')}); "
               f"RL docking for JAXA&rsquo;s Int-Ball2 in an Isaac Sim model of an ISS module "
               f"({ref('Int-Ball2', 'https://arxiv.org/abs/2512.13514')}); photorealistic lunar simulation with a "
               f"synthetic-data pipeline ({ref('OmniLRS', 'https://arxiv.org/abs/2309.08997')}); RL grasping in "
               f"procedurally generated lunar scenes ({ref('Learning to Grasp on the Moon', 'https://arxiv.org/abs/2208.00818')}). "
               f"World models have only just reached the space domain, for spacecraft docking with the ISS, trained on "
               f"simulated flights ({ref('Out-of-this-World-Model, 2026', 'https://arxiv.org/abs/2609.03067')}). Video "
               f"world models can label unlabeled video with inferred actions "
               f"({ref('DreamGen', 'https://arxiv.org/abs/2505.12705')}).",
         novel="To my knowledge, no world model yet covers the inside of a station or a lunar worksite for "
               "manipulation, or is learned from real footage. ISS footage is plentiful but carries no robot actions; "
               "a world model built from it would give a generalist space VLA visually realistic practice that no "
               "hand-built simulator offers."),
    dict(n=8, group="space", id="space-vla", title="A generalist VLA for space manipulation",
         status=("long-term vision", "wip"),
         art=['space_data', 'benchmark', 'pretrain', 'space_ops'],
         sim="Build the space-manipulation dataset and benchmark from simulators with altered physics and lighting.",
         idea="A pretrained, multi-task VLA for manipulation in space: a &ldquo;π0.5 for space&rdquo;.",
         flow=[("Space-manipulation dataset", "simulation plus analog hardware"),
               ("Benchmark", "tasks &times; gravity &times; lighting"),
               ("Multi-task pretraining", "one model across tasks and conditions"),
               ("Space operations", "servicing, assembly, sampling")],
         prior=f"Existing space work adapts models to one platform and a few tasks: OpenVLA fine-tuned on 10 "
               f"episodes for lab inspection of satellite hardware "
               f"({ref('Carrasco et al., 2025', 'https://arxiv.org/abs/2501.07802')}); a VLA adapted from 100 "
               f"demonstrations on a lunar robot prototype "
               f"({ref('SELENE, Tsinghua, 2026', 'https://doi.org/10.3390/astronautics1030015')}). Steps toward a space "
               f"foundation model: a VLM adapted to extraterrestrial imagery, which reasons about images but does not "
               f"output actions ({ref('Space-LLaVA, Stanford, 2024', 'https://arxiv.org/abs/2408.05924')}), and "
               f"natural-language commands turned into constraint-satisfying spacecraft trajectories, also tested on a "
               f"free-flying robot platform ({ref('SAGES, Stanford, 2025', 'https://arxiv.org/abs/2512.09111')}).",
         novel="To my knowledge no generalist exists yet. The bottleneck is data, so a space-manipulation dataset "
               "and benchmark is the most valuable first step, with the workspace world models of idea 7 as one "
               "source of that data."),
]


def flow_html(steps, art, loop=None):
    parts = []
    for i, ((t, d), key) in enumerate(zip(steps, art)):
        if i:
            parts.append('<div class="arrow" aria-hidden="true"></div>')
        parts.append(f'<div class="step{" first" if i == 0 else ""}">{svg(key)}<div class="k">{i + 1}</div>'
                     f'<div class="t">{t}</div>' + (f'<div class="d">{d}</div>' if d else "") + "</div>")
    out = '<div class="flow">' + "".join(parts) + "</div>"
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
    <p class="sim-line"><b>More from the simulator:</b> {x["sim"]}</p>
    {f'<p class="exp-line"><b>From my own work:</b> {x["exp"]}</p>' if x.get("exp") else ""}
    {f'<p class="exp-line mech-line"><b>The enabling mechanism:</b> {x["mech"]}</p>' if x.get("mech") else ""}
    {flow_html(x["flow"], x["art"], x.get("loop"))}
    {note}
    <div class="pn">
      <div><h4>Prior work</h4><p>{x["prior"]}</p></div>
      <div><h4>What would be new</h4><p>{x["novel"]}</p></div>
    </div>
  </div>
</section>'''


core = [x for x in IDEAS if x["group"] == "main"]
space = [x for x in IDEAS if x["group"] == "space"]
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
  <link rel="stylesheet" href="static/css/style.css?v=2">
  <link rel="stylesheet" href="static/css/ideas.css?v=5">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='13' fill='%232a78d6'/%3E%3Ccircle cx='16' cy='16' r='5' fill='white'/%3E%3C/svg%3E">
</head>
<body>
<header class="hero">
  <div class="container">
    <h1>Extracting <span class="accent">richer</span> robot experience from simulation</h1>
    <div class="authors"><span><a href="{SCHOLAR}" target="_blank" rel="noopener">Asif Amin</a></span></div>
    <div class="affils"><span>University of California, Riverside</span></div>
    <div class="affils role"><b>Seeking doctoral and pre-doctoral research positions</b> &middot; available immediately</div>
    <div class="affils contact"><a href="mailto:ramin019@ucr.edu">ramin019@ucr.edu</a></div>
    <div class="links">
      <a class="btn" href="{PROJECT}" target="_blank" rel="noopener">Current project: Learning in Zero Gravity</a>
      <a class="btn" href="{SCHOLAR}" target="_blank" rel="noopener">Google Scholar</a>
    </div>
    <div class="tldr">
      Robot learning, and vision-language-action models (VLAs) in particular, is limited by data. Simulators are
      cheap, but we mostly use them to recreate ordinary scenes under Earth&rsquo;s physics and to train under regular
      task settings, so they give us far less than they could. My research is focused on coming up with imaginative
      ways to <b class="k">extract more useful experience out of simulators</b>.
      <br><br>
      My current work explores a <b class="k">space&ndash;Earth symbiosis</b> in robotics. The pattern has surfaced
      in many technologies before: work done for space, from the CMOS image sensors now in phone cameras to memory
      foam, came back to improve life on Earth. In robotics it can run both ways. Training under space-like physics
      such as zero gravity can give robots more diverse experience that makes them better on Earth, and robots trained on
      Earth are the starting point for robots that will work in space
      (see <a href="#space">Space applications</a>).
    </div>
    <nav class="toc ideas-toc" aria-label="Ideas">{toc}</nav>
  </div>
</header>

<main>
{"".join(idea_html(x) for x in core)}
<section id="space" class="divider space-head"><div class="container"><h2>Space applications <a class="anchor" href="#space" title="Link to this section" aria-label="Link to this section">#</a></h2>
  <p class="space-intro">These directions build on my current work, which trains robots under zero gravity in simulation
    to make them better on Earth (<a href="#zero-g">Idea 1</a>; <a href="{PROJECT}" target="_blank" rel="noopener">project
    page</a>). The same idea runs the other way. Robots for space are the extreme case of learning from simulation: real
    data from orbit or the Moon is almost nonexistent, so simulators with altered physics are where their experience has
    to come from, starting from models trained on Earth.</p></div></section>
{"".join(idea_html(x) for x in space)}
</main>
<footer><div class="container">Asif Amin &middot; University of California, Riverside &middot;
  <a href="mailto:ramin019@ucr.edu">ramin019@ucr.edu</a> &middot;
  <a href="{SCHOLAR}" target="_blank" rel="noopener">Google Scholar</a></div></footer>
</body>
</html>
'''
(HERE / "index.html").write_text(page)
print("wrote", HERE / "index.html")
