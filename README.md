# SUURPh-summer-school

This is the web-page of the Simula Summer School in Computational Physiology

## Add section to web-page

To add a notebook or markdown document to the web-page, please open [\_toc.yml](_toc.yml), create a new section if needed and add the file-name (without file extension)

## Hide input/output for students

If you want to hide a cell (input) or the data produce by a cell (output), you can use `pre-commit` to collapse these in the jupyter notebook.
They will be collapsed on the jupyter-server (that uses jupyter-lab), and will be collapsed on the webpage.
Simply add the tags `hide-input` and/or `hide-output` to the cell tag in the Jupyter notebook.

To enforce this you can run `pre-commit` in the repository:

```bash
python3 -m pip install pre-commit
pre-commit autoupdate
pre-commit run
```

This will update the appropriate meta-data in the files (which in turn can be commited).
If you have any questions or issues with this, please contact [Jørgen S. Dokken](https://github.com/jorgensd/) or make an [issue](https://github.com/Simula-SSCP/SSCP_2024_lectures/issues/new).


# Installing the environment
[Pixi](https://pixi.sh/dev/installation/) is used to manage dependencies.
First install pixi (see above docs), 
for instance by calling
```bash
curl -fsSL https://pixi.sh/install.sh | sh
```
Pixi might ask you to modify your path, please do:
For instance, 
```bash
export PATH=/root/.pixi/bin:$PATH
```
then call
```bash
pixi install
```

To build the book call
```bash
pixi run python3 -m jupyter book build  .
```
Go to [_build/html/index.html](_build/html/index.html)


You can run any dependency in the `pixi` environment with `pixi run ....`

## Installation on a clean ubuntu machine (for instance a ubuntu:26.04 docker image)

```bash
apt-get update
apt-get install -y curl
curl -fsSL https://pixi.sh/install.sh | sh
export PIXI_BIN=$(pwd)/.pixi/bin
echo "export PATH=${PIXI_BIN}:${PATH}" >> ~/.bashrc
exec bash
```