PROJ = eclab-beamer
TEX = $(PROJ).tex
CLS = $(PROJ).cls
PDF = $(PROJ).pdf
RM = rm -rf

all: $(PDF)

$(PDF): $(TEX) $(CLS)
	xelatex $<
	xelatex $<

clean-misc:
	$(RM) *.aux *.out *.toc *.nav *.log *.snm

clean: clean-misc
	$(RM) $(PDF)

.PHONY: all clean
