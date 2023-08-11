from toml import load
import os

month = 8

editor_in_chief = ["Qing Gu, Undergraduate, 2018", "Hongxu Zhou, Undergraduate, 2019"]

editors = []

for file in os.listdir("files"):
    editors.append(load(os.path.join("files", file)))

associate_editor = []
journals = []
categories = {}
for editor in editors:
    associate_editor.append(
        editor["editor"]["name"] + ", " + editor["editor"]["degree"]
    )
    for key in editor["article"]:
        article = editor["article"][key]
        journal = article["journal"]
        if journal not in journals:
            journals.append(journal)
        category = article["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(article)

print(
    """\\documentclass{eclab-beamer}

\\usepackage{soul}

\\title{\\sffamily 东西情报}
"""
    + "\\subtitle{\\sffamily "
    + str(month)
    + "月刊}"
)


print(
    """
\\begin{document}

\\setbeamercolor{background canvas}{bg=Titlebg}
\\begin{frame}
  \\titlepage
\\end{frame}
\\setbeamercolor{background canvas}{bg=}

\\begin{frame}{\\sffamily Editor Board}

  \\begin{itemize}

    \\item \\sffamily Editor-in-Chief

      \\begin{itemize}
"""
)

for chief in editor_in_chief:
    print("\\item " + chief)

print(
    """
      \\end{itemize}

    \\item \\sffamily Associate Editor

      \\begin{itemize}
"""
)

for aeditor in associate_editor:
    print("\\item " + aeditor)

print(
    """
      \\end{itemize}

    \\item \\sffamily Consuling Editor
      \\begin{itemize}
        \\item \\sffamily Xia Fang, PhD, Professor
      \\end{itemize}

  \\end{itemize}

\\end{frame}

\\begin{frame}[allowframebreaks]{\\sffamily Journal List}
  \\begin{itemize}\\centering
"""
)

for journal in journals:
    print("\\item " + journal)

print(
    """
  \\end{itemize}
\\end{frame}

\\begin{frame}[allowframebreaks]{\\sffamily 卷首语}

\\begin{itemize}
"""
)

for category in categories:
    print("\\item " + category + "研究更新了" + str(len(categories[category])) + "篇")
    print("\\begin{enumerate}")
    for article in categories[category]:
        print(
            "\\item \\href{"
            + article["doi"]
            + "}{\\color{blue} \\ul{"
            + article["title"]
            + "}}"
        )
        print("\n\\footnotesize{" + article["authors"].replace("&", "\\&") + "}\n")
        print(article["summary"])
    print("\\end{enumerate}")
print(
    """
\\end{itemize}
\\end{frame}

"""
)

for category in categories:
    for article in categories[category]:
        print(
            "\\begin{frame}[allowframebreaks]{\\color{black} \\normalsize{\\ul{"
            + category
            + "}} \\hfill"
        )
        print("\\begin{tabular}{r}")
        print("\\textit{" + article["journal"] + ", " + article["publish"] + "}\\\\")
        print(
            "\\href{"
            + article["doi"]
            + "}{\\color{blue} \\footnotesize{\\ul{\\textit{"
            + article["doi"]
            + "}}}}"
        )
        print("\\end{tabular}}\n")
        print("\\textbf{\\Large{" + article["title"] + "}}\n\n\\vspace{1mm}")
        print(article["authors"].replace("&", "\\&"))
        print("\n\\hspace*{\\fill}\n")
        print("\n\\textbf{Abstract:}")
        print(article["abstract"])
        print("\n\\textbf{Keywords:} " + article["keywords"])
        print("\\end{frame}")

print("\\end{document}")
