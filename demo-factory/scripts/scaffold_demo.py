import argparse
from pathlib import Path

DEMO_TYPES = {"gpt", "swarm", "prompt", "hybrid"}


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, help="Demo folder name (Demo_XX_Name)")
    parser.add_argument("--type", required=True, choices=sorted(DEMO_TYPES))
    parser.add_argument("--root", required=True, help="Demo_Package root")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    demo_dir = root / args.name
    demo_dir.mkdir(parents=True, exist_ok=True)

    (demo_dir / "Prompts").mkdir(exist_ok=True)
    (demo_dir / "Demo_Docs").mkdir(exist_ok=True)
    (demo_dir / "Backup_Outputs").mkdir(exist_ok=True)

    assets_dir = Path(__file__).resolve().parent.parent / "assets"
    demo_instructions_template = assets_dir / "demo-instructions-template.md"

    if demo_instructions_template.exists():
        write_if_missing(demo_dir / "Demo_Instructions.md", demo_instructions_template.read_text(encoding="utf-8"))
    else:
        write_if_missing(demo_dir / "Demo_Instructions.md", "# Demo Instructions\n")

    if args.type in {"gpt", "hybrid"}:
        (demo_dir / "Custom_GPT_Knowledge_Docs").mkdir(exist_ok=True)
        write_if_missing(demo_dir / "Custom_GPT_Knowledge_Docs" / "README.md", "# Custom GPT Knowledge Docs\n")
        write_if_missing(demo_dir / "GPT_Configuration.md", "# GPT Configuration\n")

    if args.type == "swarm":
        write_if_missing(demo_dir / "Agentic_Swarm_Architecture.md", "# Agentic Swarm Architecture\n")

    demo_docs_readme = demo_dir / "Demo_Docs" / "README.md"
    if not demo_docs_readme.exists():
        demo_docs_readme.write_text("# Demo Docs\n", encoding="utf-8")


if __name__ == "__main__":
    main()
