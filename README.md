# XEN-GEN1-T-PLAN

Planning-specialized XEN text model trained from scratch.

## Purpose
Task decomposition, project planning, dependency analysis, roadmaps, troubleshooting plans, milestones and verification.

## Skills
Built-in skills in skills/*/SKILL.md are loaded at inference time for users who do not want or cannot afford additional training. Skills do not change model parameters; training a specialized checkpoint can improve capability beyond skills alone.

## Train
```bash
python training/train.py --data datasets/train.jsonl --output outputs/xen --steps 1000
```

## Generate
```bash
python inference/generate.py --model-dir outputs/xen --prompt "Plan a small Roblox game from prototype to release"
```

Use `--no-skills` to disable the skill layer.

Windows, Linux and macOS are supported.

## License
MIT
