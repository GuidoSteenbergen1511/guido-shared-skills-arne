import argparse
from pathlib import Path

REQUIRED_DIRS = {"Prompts", "Demo_Docs", "Backup_Outputs"}


def find_demo_dirs(root: Path) -> list[Path]:
    return sorted([p for p in root.iterdir() if p.is_dir() and p.name.startswith("Demo_")])


def read_text_safe(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="Demo_Package root")
    parser.add_argument("--project-root", required=False, help="Project root for README checks")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    demos = find_demo_dirs(root)
    errors = []
    warnings = []

    for demo in demos:
        missing = [d for d in REQUIRED_DIRS if not (demo / d).exists()]
        if missing:
            errors.append(f"{demo.name}: missing required dirs: {', '.join(missing)}")

        gpt_config = demo / "GPT_Configuration.md"
        knowledge_dir = demo / "Custom_GPT_Knowledge_Docs"
        if gpt_config.exists():
            if not knowledge_dir.exists():
                errors.append(f"{demo.name}: GPT_Configuration.md present but Custom_GPT_Knowledge_Docs/ missing")
            demo_docs_readme = demo / "Demo_Docs" / "README.md"
            if demo_docs_readme.exists():
                if "Custom_GPT_Knowledge_Docs" not in read_text_safe(demo_docs_readme):
                    warnings.append(f"{demo.name}: Demo_Docs README should reference Custom_GPT_Knowledge_Docs")
            else:
                warnings.append(f"{demo.name}: Demo_Docs/README.md missing")

    qa_checklist = root / "_Analysis" / "Prompt_QA_Checklist.md"
    if not qa_checklist.exists():
        warnings.append("Prompt_QA_Checklist.md missing in Demo_Package/_Analysis")

    if args.project_root:
        project_root = Path(args.project_root).expanduser().resolve()
        readme = project_root / "README.md"
        sequence = root / "Master_Demo_Sequence_Guide.md"
        portfolio = root / "_Analysis" / "Use_Case_Portfolio.md"
        for demo in demos:
            name = demo.name
            for doc in [readme, sequence, portfolio]:
                if doc.exists() and name not in read_text_safe(doc):
                    warnings.append(f"{name}: not referenced in {doc.name}")

    print("VALIDATION RESULTS")
    print("Errors:")
    if errors:
        for e in errors:
            print(f"- {e}")
    else:
        print("- None")

    print("Warnings:")
    if warnings:
        for w in warnings:
            print(f"- {w}")
    else:
        print("- None")

    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
