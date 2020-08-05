# coding:utf-8
# noinspection PyUnresolvedReferences
import hou

import lynxi.materialx

open_asset_file_button_script = '''
kwargs["node"].hdaModule().set_asset_file_open(kwargs)
'''


analysis_asset_button_script = '''
kwargs["node"].hdaModule().set_asset_analysis(kwargs["node"])
'''

export_file_button_script = '''
kwargs["node"].hdaModule().set_asset_export(kwargs)
'''

update_module_button_script = '''
kwargs["node"].hdaModule().set_module_update()
'''


def set_asset_file_open(kwargs):
    reload(lynxi.materialx)
    lynxi.materialx.hou2mtx_set_asset_file_open_cmd(kwargs)


def set_asset_analysis(kwargs):
    reload(lynxi.materialx)
    lynxi.materialx.hou2mtx_set_asset_analysis_cmd(kwargs)


def set_asset_export(kwargs):
    reload(lynxi.materialx)
    lynxi.materialx.hou2mtx_set_asset_export_cmd(kwargs)


def set_module_update():
    from LxScheme import shmOutput
    shmOutput.Scheme().loadActiveModules()
