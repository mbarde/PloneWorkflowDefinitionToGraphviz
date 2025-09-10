# PloneWorkflowDefinitionToGraphviz

Simple python script to create [Graphviz](http://www.graphviz.org/) graph from a [Plone workflow](https://docs.plone.org/4/en/old-reference-manuals/archgenxml/basic-features/workflows.html) definition.

Usage examples:

```
python3 wtg.py definition.xml
python3 wtg.py definition.xml --use-ids --hide-guards --with-permissions --format=jpg
```

Optional parameters:

- `--use-ids`: Use ids as labels (default is title)
- `--hide-guards`: Do not display guard roles and permissions of transitions
- `--with-permissions`: Display permissions for each state
- `--format`: Output format, can be `pdf` (default), `jpg` or `png`

Dependencies:

- Graphviz: http://www.graphviz.org/Download..php
- Simple Python interface for Graphviz: https://pypi.python.org/pypi/graphviz
