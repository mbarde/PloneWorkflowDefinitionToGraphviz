from copy import deepcopy
from graphviz import Digraph
from xml.etree.ElementTree import parse as parseXML

import sys


if len(sys.argv) < 2:
    sys.exit(0)

xmlfile = sys.argv[1]

useIdsAsLabels = '--use-ids' in sys.argv
hideGuards = '--hide-guards' in sys.argv

root = parseXML(xmlfile).getroot()

title = root.get('title')

dot = Digraph(comment=title)

transitions = dict()
for trans in root.findall('transition'):
    newTrans = dict()
    newTrans['id'] = trans.get('transition_id')
    newTrans['to'] = trans.get('new_state')
    if useIdsAsLabels is True:
        newTrans['label'] = trans.get('transition_id')
    else:
        newTrans['label'] = trans.get('title')

    if not hideGuards:
        guard_roles = []
        guard_permissions = []

        for guard in trans.findall('guard'):
            for guard_role in guard.findall('guard-role'):
                guard_roles.append(guard_role.text)

            for guard_permission in guard.findall('guard-permission'):
                guard_permissions.append(guard_permission.text)

        if len(guard_roles) > 0:
            newTrans['label'] += '\n(' + ',\n'.join(guard_roles) + ')'

        if len(guard_permissions) > 0:
            newTrans['label'] += '\n(' + ',\n'.join(guard_permissions) + ')'

    transitions[newTrans['id']] = newTrans

edges = []
include_permission_roles_of = ""

if len(sys.argv) > 2:
    include_permission_roles_of = sys.argv[2]

for state in root.findall('state'):
    node_id = state.get('state_id')
    if useIdsAsLabels is True:
        label = state.get('state_id')
    else:
        label = state.get('title')

    # if demanded include role names which have a certian permission
    # into state label
    if len(include_permission_roles_of) > 0:
        for trans_map in state.findall('permission-map'):
            name = trans_map.get('name')
            if name == include_permission_roles_of:
                roles = []
                for role in trans_map.findall('permission-role'):
                    roles.append(role.text)
                label += '\n[' + include_permission_roles_of + ']\n' + ',\n' \
                    .join(roles) + ''

    dot.node(node_id, label, shape='box')

    for exTrans in state.findall('exit-transition'):
        newEdge = deepcopy(transitions[exTrans.get('transition_id')])
        newEdge['from'] = node_id
        edges.append(newEdge)

for edge in edges:
    dot.edge(edge['from'], edge['to'], label=edge['label'])

dot.render(xmlfile + '.gv', view=True)
