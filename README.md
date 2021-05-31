* Why Dia

  I try to find a simple flow chart tool under Ubuntu for taking notes in Emacs org-mode. I have the following requirements:
  1. It shall be simple and easy to use.
  2. It shall provide native support to LaTex formula
  3. It shall produce charts of high quality. 
  
  I have tried several options: Inkscape, LibreOffice Draw, and Dia. Inkscape is an excellent tool and I often use it
  for free drawing. It also provides native support to LaTex formula. However, it isn't good for drawing flow chart, for
  example, I can't create snapped connection between objects. Libreoffice Draw is simple and has an extension to support
  LaTex, but it is lack of features to create complicate charts. I end up with Dia for its easy-to-use features, high
  quality figures, and native support to LaTex formula.
  

* Install Dia

  ```
  sudo apt update
  sudo apt install dia
  ```

* Export in Dia
  There are many export options in Dia, for example, PNG, EPS, PDF and etc. Most of these options work out of box.

* Export charts with Latex formula

  Dia can export Latex PGF files so you can include them in your Tex file. This has several advantages: 1) you can edit
  Tex file later in Emacs, 2) the file size is very small, and 3) it produces high quality figures and etc. To do so,
  go to the menu File->Export and save as LaTex PGF *.tex file. You can then include the Tex file in your LaTex file. If
  you use Emacs org-mode, It is as easy as:
  
  ```
  #+LATEX_HEADER: \usepackage{tikz}
  #+LATEX_HEADER: \usepackage{adjustbox}

  #+BEGIN_LATEX
  \begin{adjustbox}{max width=\textwidth}
  \input{"/home/cgliu/figs/fixed/DoubleQ.tex"}
  \end{adjustbox}
  #+END_LATEX
  ```
  I use adjustbox environment to control the size of the figure. 

  According to Dia help document, the LaTex formula should be enclosed between two '$'. When exporting to LaTex PGF or
  TikZ, Dia assumes that every special character you have inserted are supposed to be that way, and escapes the
  characters. So your math dollars will be escaped \$, your backslashes will be escaped \ensuremath{\backslash}. As a
  result, when you include the Tex and export pdf, the figures don't show up as you expect, for example, it looks like.

  ![before fix](./before_fix.png)    

  I wrote a Python script to un-escaped the special characters in Tex PGF export. You can run as follows: 

  ```
  >>> fix_formula.py <source_folder> 
  ```

  After running this script, it should work as expected, e.g.
  ![after fix](./after_fix.png)
  
  Note: My Dia version is 0.97+git, 
