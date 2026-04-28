#!/usr/bin/env python3
"""Generate the inverse Baustein -> fields mapping as markdown.

Reads the BSI-tagged questionnaire JSON and produces a documentation
artefact that lets a customer / auditor navigate from a BSI Baustein ID
to the questionnaire fields that satisfy it.
"""
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "supply-chain-questionnaire.json"
OUT_PATH = ROOT / "data" / "bsi-lieferketten-mapping.md"

BAUSTEIN_TITLES = {
    # Section titles from BSI NIS-2 Lieferketten-Checkliste v1.0 (5 June 2025)
    "ASST": "Asset-Schnittstellen / Datenuebertragung",
    "BES.1": "Beschaffungsmanagement Grundlagen",
    "BES.2": "Bedarf",
    "BES.3": "Lieferantenauswahl",
    "BES.4": "Vertragskriterien",
    "BES.5": "Vertragsinhalte",
    "BES.6": "Vertragsende",
    "BES.7": "Abnahme",
    "BES.8": "Resilience / Notfallvorsorge",
    "DEV.6": "Software-Entwicklung — SBOM",
    "DLS.2": "Dienstleistersteuerung — laufende Pruefung",
    "DLS.3": "Dienstleistersteuerung — Aussonderung",
    "DLS.5": "Dienstleistersteuerung — Schutzmassnahmen",
    "DLS.6": "Dienstleistersteuerung — Cloud-Profil",
}


def section_for(baustein: str) -> str:
    parts = baustein.split(".")
    if len(parts) >= 2:
        prefix = ".".join(parts[:2])
        if prefix in BAUSTEIN_TITLES:
            return prefix
    return parts[0]


def main() -> int:
    data = json.loads(DATA_PATH.read_text())
    inverse: dict[str, list[dict[str, str]]] = defaultdict(list)
    for field in data["fields"]:
        for baustein in field.get("bsiBausteine", []):
            inverse[baustein].append({
                "id": field["id"],
                "section": field["section"],
                "label": field["label"]["en"],
            })

    sections: dict[str, list[str]] = defaultdict(list)
    for baustein in inverse:
        sections[section_for(baustein)].append(baustein)
    for prefix in sections:
        sections[prefix].sort()

    out: list[str] = []
    out.append("# BSI NIS-2 Lieferketten-Checkliste — inverse mapping")
    out.append("")
    out.append(
        "Customer-facing view: given a Baustein from the "
        "[BSI NIS-2 Lieferketten-Checkliste v1.0 (5 June 2025)]"
        "(https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/NIS-2/nis-2-lieferkette_grundschutz-checkliste.pdf), "
        "which questionnaire fields help satisfy it.",
    )
    out.append("")
    out.append(
        "Generated from `data/supply-chain-questionnaire.json`. Do not edit by hand. "
        "Re-run `scripts/generate-bsi-mapping.py` after editing field tags.",
    )
    out.append("")
    total_bausteine = len(inverse)
    total_pairs = sum(len(v) for v in inverse.values())
    out.append(f"**Coverage:** {total_bausteine} Bausteine, {total_pairs} field-mappings, {len(data['fields'])} fields total.")
    out.append("")

    section_order = [
        "ASST", "BES.1", "BES.2", "BES.3", "BES.4", "BES.5", "BES.6", "BES.7", "BES.8",
        "DEV.6", "DLS.2", "DLS.3", "DLS.5", "DLS.6",
    ]
    for prefix in section_order:
        if prefix not in sections:
            continue
        title = BAUSTEIN_TITLES.get(prefix, prefix)
        out.append(f"## {prefix} — {title}")
        out.append("")
        out.append("| Baustein | Fields |")
        out.append("|----------|--------|")
        for baustein in sections[prefix]:
            field_strs = [f"`{e['id']}`" for e in inverse[baustein]]
            out.append(f"| `{baustein}` | {', '.join(field_strs)} |")
        out.append("")

    OUT_PATH.write_text("\n".join(out))
    print(f"OK: wrote {OUT_PATH} ({total_bausteine} Bausteine, {total_pairs} mappings)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
