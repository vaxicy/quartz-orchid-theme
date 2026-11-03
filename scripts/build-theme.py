# -*- coding: utf-8 -*-
"""Build the Claret Atelier Light / Dark color themes from one palette table.

    py -3 scripts/build-theme.py
"""

import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
THEMES = BASE / "themes"
NAME = "quartz-orchid-theme"
SLUG = "quartz-orchid"
DISPLAY = "Quartz Orchid Theme"
VERSION = "1.0.0"
REPO = "https://github.com/vaxicy/quartz-orchid-theme"

UI = {
    "foreground": ("#3A3440", "#E9E3EC"),
    "editor.foreground": ("#3A3440", "#E9E3EC"),
    "terminal.foreground": ("#3A3440", "#E9E3EC"),
    "input.foreground": ("#33303C", "#F0EBF3"),
    "dropdown.foreground": ("#33303C", "#F0EBF3"),
    "quickInput.foreground": ("#33303C", "#F0EBF3"),
    "editorWidget.foreground": ("#33303C", "#F0EBF3"),
    "editorHoverWidget.foreground": ("#33303C", "#F0EBF3"),
    "editorSuggestWidget.foreground": ("#33303C", "#F0EBF3"),
    "notifications.foreground": ("#33303C", "#F0EBF3"),
    "descriptionForeground": ("#8B8494", "#9A93A6"),
    "input.placeholderForeground": ("#8B8494", "#9A93A6"),
    "focusBorder": ("#8C76A3", "#D6C49E"),
    "inputOption.activeBorder": ("#5E4A78", "#E4D2AE"),
    "input.border": ("#E1DBE7", "#3E3B48"),
    "dropdown.border": ("#E1DBE7", "#3E3B48"),
    "editor.background": ("#F5F2F5", "#23212A"),
    "tab.activeBackground": ("#F5F2F5", "#23212A"),
    "titleBar.activeBackground": ("#EFEAF1", "#1C1A22"),
    "titleBar.activeForeground": ("#48414F", "#DCD5E2"),
    "titleBar.inactiveBackground": ("#ECE7EE", "#18161D"),
    "titleBar.inactiveForeground": ("#9A93A6", "#807889"),
    "activityBar.background": ("#E7E1EA", "#1A1820"),
    "activityBar.foreground": ("#8C76A3", "#B9A7CC"),
    "activityBar.activeBorder": ("#8C76A3", "#D6C49E"),
    "activityBar.inactiveForeground": ("#A79EB0", "#6A6376"),
    "sideBar.background": ("#F1EDF3", "#272530"),
    "sideBar.foreground": ("#4A4350", "#D5CEDC"),
    "sideBarSectionHeader.background": ("#E8E2EC", "#2F2C39"),
    "sideBarSectionHeader.foreground": ("#5A5263", "#E1DAE7"),
    "panel.background": ("#F4F1F5", "#201E27"),
    "terminal.background": ("#F4F1F5", "#201E27"),
    "panel.border": ("#E2DCE8", "#3A3744"),
    "editorGroup.border": ("#E2DCE8", "#3A3744"),
    "tab.border": ("#E2DCE8", "#3A3744"),
    "sideBar.border": ("#E2DCE8", "#3A3744"),
    "titleBar.border": ("#E2DCE8", "#3A3744"),
    "statusBar.background": ("#8C76A3", "#6E5C86"),
    "statusBar.noFolderBackground": ("#8C76A3", "#6E5C86"),
    "statusBar.foreground": ("#F7F3F8", "#EFE9F3"),
    "statusBar.noFolderForeground": ("#F7F3F8", "#EFE9F3"),
    "statusBarItem.hoverBackground": ("#7A6490", "#7E6B98"),
    "statusBar.debuggingBackground": ("#8A6A24", "#A87E2E"),
    "statusBar.debuggingForeground": ("#F8F4FA", "#FFF7E8"),
    "editorGroupHeader.tabsBackground": ("#EFEBF1", "#1F1D26"),
    "tab.inactiveBackground": ("#EFEBF1", "#1F1D26"),
    "tab.activeForeground": ("#38333F", "#EDE7F0"),
    "tab.activeBorderTop": ("#8C76A3", "#D6C49E"),
    "tab.inactiveForeground": ("#8B8494", "#7F7889"),
    "tab.hoverBackground": ("#E6E0EB", "#2E2B37"),
    "tab.activeModifiedBorder": ("#8A6A24", "#E4C88C"),
    "tab.inactiveModifiedBorder": ("#8A6A24", "#E4C88C"),
    "list.hoverBackground": ("#ECE6F0", "#312E3B"),
    "list.activeSelectionBackground": ("#E2D7EA", "#3E3A4A"),
    "editorSuggestWidget.selectedBackground": ("#E2D7EA", "#3E3A4A"),
    "list.activeSelectionForeground": ("#33303C", "#F0EBF3"),
    "list.inactiveSelectionForeground": ("#33303C", "#F0EBF3"),
    "editorSuggestWidget.selectedForeground": ("#33303C", "#F0EBF3"),
    "list.inactiveSelectionBackground": ("#EDE7F0", "#373442"),
    "list.highlightForeground": ("#5E4A78", "#CDB8E2"),
    "list.focusHighlightForeground": ("#5E4A78", "#CDB8E2"),
    "tree.indentGuidesStroke": ("#E0D9E7", "#383544"),
    "editorLineNumber.foreground": ("#ABA3B4", "#6A6376"),
    "editorLineNumber.activeForeground": ("#8C76A3", "#D6C49E"),
    "editor.lineHighlightBackground": ("#F0ECF3", "#2B2833"),
    "editor.lineHighlightBorder": ("#EAE3EE", "#332F3C"),
    "editorCursor.foreground": ("#8C76A3", "#D6C49E"),
    "selection.background": ("#E2D7EA", "#3E3A4A"),
    "editor.selectionBackground": ("#E2D7EA", "#3E3A4A"),
    "terminal.selectionBackground": ("#E2D7EA", "#3E3A4A"),
    "editor.inactiveSelectionBackground": ("#EDE7F0", "#373442"),
    "editor.wordHighlightBackground": ("#E2D7EA80", "#4B4660AA"),
    "editor.wordHighlightStrongBackground": ("#E2D7EA80", "#4B4660AA"),
    "editor.selectionHighlightBackground": ("#E2D7EA66", "#4B466088"),
    "editor.findMatchHighlightBackground": ("#EFE0C2", "#4A4152"),
    "editor.findMatchBackground": ("#E7CD9C", "#6B5B45"),
    "editor.findMatchBorder": ("#8C76A3", "#E4C88C"),
    "editorBracketMatch.background": ("#EDE7F0", "#33303D"),
    "editorBracketMatch.border": ("#8C76A3", "#D6C49E"),
    "editorIndentGuide.background1": ("#E5DFEB", "#343140"),
    "editorIndentGuide.activeBackground1": ("#A79EB0", "#5C5568"),
    "editorWhitespace.foreground": ("#E5DFEB", "#343140"),
    "editorRuler.foreground": ("#ECE6F0", "#302D39"),
    "textLink.foreground": ("#6B5490", "#CDB8E2"),
    "textLink.activeForeground": ("#8C76A3", "#E0CFEF"),
    "editorLink.activeForeground": ("#8C76A3", "#E0CFEF"),
    "quickInput.background": ("#FAF7FB", "#2A2833"),
    "editorHoverWidget.background": ("#FAF7FB", "#2A2833"),
    "notifications.background": ("#FAF7FB", "#2A2833"),
    "input.background": ("#FCFAFD", "#23212A"),
    "dropdown.background": ("#FCFAFD", "#23212A"),
    "editorWidget.background": ("#FAF7FB", "#2A2833"),
    "editorSuggestWidget.background": ("#FAF7FB", "#2A2833"),
    "editorWidget.border": ("#E2DCE8", "#423E4E"),
    "editorHoverWidget.border": ("#E2DCE8", "#423E4E"),
    "editorSuggestWidget.border": ("#E2DCE8", "#423E4E"),
    "notifications.border": ("#E2DCE8", "#423E4E"),
    "button.background": ("#8C76A3", "#D6C49E"),
    "button.foreground": ("#FAF7FB", "#241F1A"),
    "button.hoverBackground": ("#A088B5", "#E4D2AE"),
    "button.secondaryBackground": ("#E7E1EA", "#332F3C"),
    "button.secondaryForeground": ("#48414F", "#DFD8E4"),
    "button.secondaryHoverBackground": ("#DDD5E3", "#3E3A49"),
    "badge.background": ("#5E4A78", "#8C76A3"),
    "activityBarBadge.background": ("#5E4A78", "#8C76A3"),
    "badge.foreground": ("#F7F3F8", "#F7F3F8"),
    "activityBarBadge.foreground": ("#F7F3F8", "#F7F3F8"),
    "scrollbarSlider.background": ("#A79EB066", "#7A738888"),
    "scrollbarSlider.hoverBackground": ("#8B849488", "#948DA099"),
    "scrollbarSlider.activeBackground": ("#8C76A399", "#C0AAD299"),
    "errorForeground": ("#A34A63", "#E08FA4"),
    "editorError.foreground": ("#A34A63", "#E08FA4"),
    "problemsErrorIcon.foreground": ("#A34A63", "#E08FA4"),
    "gitDecoration.deletedResourceForeground": ("#A34A63", "#E08FA4"),
    "editorGutter.deletedBackground": ("#A34A63", "#E08FA4"),
    "editorWarning.foreground": ("#8A6A24", "#E4C88C"),
    "problemsWarningIcon.foreground": ("#8A6A24", "#E4C88C"),
    "editorInfo.foreground": ("#4A6E8C", "#9CC0DC"),
    "problemsInfoIcon.foreground": ("#4A6E8C", "#9CC0DC"),
    "gitDecoration.addedResourceForeground": ("#3E7A62", "#86C9A8"),
    "gitDecoration.untrackedResourceForeground": ("#3E7A62", "#86C9A8"),
    "editorGutter.addedBackground": ("#3E7A62", "#86C9A8"),
    "gitDecoration.modifiedResourceForeground": ("#8A6A24", "#E4C88C"),
    "editorGutter.modifiedBackground": ("#8A6A24", "#E4C88C"),
    "diffEditor.insertedTextBackground": ("#CFE4DCAA", "#2E4A4066"),
    "diffEditor.removedTextBackground": ("#F2D5DEAA", "#5A334366"),
    "diffEditor.insertedLineBackground": ("#CFE4DC66", "#2E4A4044"),
    "diffEditor.removedLineBackground": ("#F2D5DE66", "#5A334344"),
    "terminal.ansiBlack": ("#3A3440", "#221F28"),
    "terminal.ansiRed": ("#A34A63", "#E08FA4"),
    "terminal.ansiGreen": ("#3E7A62", "#86C9A8"),
    "terminal.ansiYellow": ("#8A6A24", "#E4C88C"),
    "terminal.ansiBlue": ("#4A6E8C", "#9CC0DC"),
    "terminal.ansiMagenta": ("#7A6490", "#C0AAD2"),
    "terminal.ansiCyan": ("#2F7A6E", "#8FD0BC"),
    "terminal.ansiWhite": ("#8B8494", "#CFC8D8"),
    "terminal.ansiBrightBlack": ("#6E6878", "#7E7789"),
    "terminal.ansiBrightRed": ("#C06078", "#F2A9BC"),
    "terminal.ansiBrightGreen": ("#55997C", "#A6DDC0"),
    "terminal.ansiBrightYellow": ("#B0883A", "#F2DDA6"),
    "terminal.ansiBrightBlue": ("#5E8CAE", "#B8D6EC"),
    "terminal.ansiBrightMagenta": ("#96789E", "#DCC8E4"),
    "terminal.ansiBrightCyan": ("#3E8E80", "#A8E2D2"),
    "terminal.ansiBrightWhite": ("#332F3A", "#F0EBF3"),
}

TOKENS = [
    ("comment", ("#9A93A6", "#7E7789"), "italic"),
    (("keyword", "storage"), ("#4A6E8C", "#9CC0DC"), None),
    ("string", ("#8A6A24", "#E4C88C"), None),
    (("entity.name.function", "support.function"), ("#2F7A6E", "#8FD0BC"), None),
    (("entity.name.type", "support.type", "support.class"), ("#6E6480", "#BDB2CE"), None),
    (("constant.numeric", "constant.language", "variable.other.constant"), ("#9A5A32", "#E2A279"), None),
    ("variable", ("#3A3440", "#E9E3EC"), None),
    ("variable.parameter", ("#6E6878", "#B4AEBD"), None),
    (("variable.other.property", "support.variable.property"), ("#7C6A52", "#CBB694"), None),
    ("keyword.operator", ("#857F8C", "#A29BAC"), None),
    ("punctuation", ("#9A93A6", "#857E90"), None),
    ("entity.name.tag", ("#4A6E8C", "#9CC0DC"), None),
    ("entity.other.attribute-name", ("#8A6A24", "#E4C88C"), None),
    ("string.regexp", ("#9A5A32", "#E2A279"), None),
    ("constant.character.escape", ("#8A6A24", "#E4C88C"), None),
    ("markup.heading", ("#332F3A", "#F2EDF4"), "bold"),
    ("markup.bold", ("#332F3A", "#F2EDF4"), "bold"),
    ("markup.italic", ("#332F3A", "#F2EDF4"), "italic"),
    ("invalid", ("#A34A63", "#E08FA4"), None),
]

SEMANTIC = {
    "variable": "#3A3440|#E9E3EC",
    "parameter": "#6E6878|#B4AEBD",
    "property": "#7C6A52|#CBB694",
    "function": "#2F7A6E|#8FD0BC",
    "method": "#2F7A6E|#8FD0BC",
    "type": "#6E6480|#BDB2CE",
    "class": "#6E6480|#BDB2CE",
    "interface": "#6E6480|#BDB2CE",
    "variable.readonly": "#9A5A32|#E2A279",
}

PACKAGE = {
    "name": NAME,
    "displayName": DISPLAY,
    "description": "A quiet mineral palette: quartz white, grey orchid and pale gold in the light variant, a warm ink room with muted lilac accents in the dark one.",
    "version": VERSION,
    "publisher": "lilinhuang",
    "engines": {"vscode": "^1.80.0"},
    "categories": ["Themes"],
    "keywords": ["theme", "light", "dark", "quartz", "orchid", "lilac", "stone", "minimal"],
    "icon": "assets/icon.png",
    "license": "SEE LICENSE IN LICENSE",
    "galleryBanner": {"color": "#23212A", "theme": "dark"},
    "repository": {"type": "git", "url": REPO},
    "contributes": {
        "themes": [
            {"label": f"{DISPLAY} Light", "uiTheme": "vs",
             "path": f"./themes/{SLUG}-light-color-theme.json"},
            {"label": f"{DISPLAY} Dark", "uiTheme": "vs-dark",
             "path": f"./themes/{SLUG}-dark-color-theme.json"},
        ]
    },
}


def build(variant, index):
    colors = {key: pair[index] for key, pair in UI.items()}
    tokens = []
    for scope, pair, style in TOKENS:
        settings = {"foreground": pair[index]}
        if style:
            settings["fontStyle"] = style
        tokens.append({"scope": [scope] if isinstance(scope, str) else list(scope),
                       "settings": settings})
    theme = {
        "name": f"{DISPLAY} {variant.title()}",
        "type": variant,
        "colors": colors,
        "semanticHighlighting": True,
        "semanticTokenColors": {k: v.split("|")[index] for k, v in SEMANTIC.items()},
        "tokenColors": tokens,
    }
    out = THEMES / f"{SLUG}-{variant}-color-theme.json"
    out.write_text(json.dumps(theme, indent=2) + "\n", encoding="utf-8")
    print("wrote", out.relative_to(BASE), len(colors), "UI colors")


def main():
    THEMES.mkdir(exist_ok=True)
    for index, variant in enumerate(("light", "dark")):
        build(variant, index)
    (BASE / "package.json").write_text(json.dumps(PACKAGE, indent=2) + "\n", encoding="utf-8")
    print("wrote package.json")


if __name__ == "__main__":
    main()
