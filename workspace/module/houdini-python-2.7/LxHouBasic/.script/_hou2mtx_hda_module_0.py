# coding:utf-8
# noinspection PyUnresolvedReferences
import hou
import lynxi
import lynxi.materialx
reload(lynxi)
reload(lynxi.materialx)


find_look_button_script = '''
kwargs["node"].hdaModule().set_look_find(kwargs["node"])
'''

export_file_button_script = '''
kwargs["node"].hdaModule().set_file_export(kwargs["node"])
'''

update_module_button_script = '''
kwargs["node"].hdaModule().set_module_update()
'''


def set_look_find(hou_node_obj):
    lynxi.materialx.hou2mtx_set_look_find_cmd(hou_node_obj)


def set_file_export(hou_node_obj):
    lynxi.materialx.hou2mtx_set_file_export_cmd(hou_node_obj)


def set_module_update():
    from LxScheme import shmOutput
    shmOutput.Scheme().loadActiveModules()
