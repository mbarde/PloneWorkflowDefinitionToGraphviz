# PloneWorkflowDefinitionToGraphviz
Simple python script to create [Graphviz](http://www.graphviz.org/) graph from a [Plone workflow](https://docs.plone.org/4/en/old-reference-manuals/archgenxml/basic-features/workflows.html) definition

Usage: `python wtg.py definition.xml`

Optionally you can also pass the name of a permission (for example `View`) to the script as second argument. Then all roles having this specified permission will be displayed as well (in the label of the corresponding state): `python wtg.py definition.xml View`

Output will be Graphviz graph as pdf file

Dependencies:

*  Graphviz: http://www.graphviz.org/Download..php
*  Simple Python interface for Graphviz: https://pypi.python.org/pypi/graphviz
