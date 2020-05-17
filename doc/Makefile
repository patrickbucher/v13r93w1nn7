.PHONY: all clean

all: portfolio.pdf

portfolio.pdf: portfolio.tex pics/vier-gewinnt.jpg pics/rotation-papier.jpg
	xelatex portfolio.tex && xelatex portfolio.tex

clean:
	rm -f portfolio.lof portfolio.aux portfolio.log portfolio.toc portfolio.out
