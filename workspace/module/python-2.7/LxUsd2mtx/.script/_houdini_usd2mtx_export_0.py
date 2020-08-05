# coding:utf-8
# noinspection PyUnresolvedReferences
import hou

from LxMtx import mtxObjects

from LxUsd import usdCommands

from LxUsd import usdObjects

from LxUsd2mtx import usd2mtxObjects

buttonScript = '''
kwargs["node"].hdaModule().set_mtx_file_export_cmd(kwargs["node"])
'''


def set_cache_init():
    mtxObjects.GRH_OBJ_QUEUE.restore()
    usdObjects.GRH_OBJ_QUEUE.restore()
    usd2mtxObjects.GRH_TRS_OBJ_QUEUE.restore()


def set_parm_value_validation(parm_obj):
    parm_template_obj = parm_obj.parmTemplate()
    parm_label_str = parm_template_obj.label()
    return hou.ui.displayMessage(
        u'''parameter "{} : {}" must not be empty, please check it.'''.format(parm_label_str, parm_obj.name())
    )


def get_mtx_file_export_list(node_obj):
    exporter_count = node_obj.parm(u'usd2mtx_exporter_configure').eval()
    lis = []

    for exporter_index in xrange(exporter_count):
        export_file_path_parm_obj = node_obj.parm(u'usd2mtx_export_file_path_{}'.format(exporter_index + 1))
        export_file_path_str = export_file_path_parm_obj.eval()
        if not export_file_path_str:
            return set_parm_value_validation(export_file_path_parm_obj)

        look_count = node_obj.parm(u'usd2mtx_look_configure_{}'.format(exporter_index + 1)).eval()
        look_arg_list = []
        for look_index in xrange(look_count):
            look_enable_parm_obj = node_obj.parm(u'usd2mtx_look_enable_{}_{}'.format(exporter_index + 1, look_index + 1))
            look_enable = look_enable_parm_obj.eval()
            if look_enable:
                look_name_parm_obj = node_obj.parm(u'usd2mtx_look_name_{}_{}'.format(exporter_index + 1, look_index + 1))
                look_name_str = look_name_parm_obj.eval()
                if not look_name_str:
                    return set_parm_value_validation(look_name_parm_obj)

                assign_path_parm_obj = node_obj.parm(u'usd2mtx_assign_path_{}_{}'.format(exporter_index + 1, look_index + 1))
                assign_path_str = assign_path_parm_obj.eval()
                if not assign_path_str:
                    return set_parm_value_validation(assign_path_parm_obj)

                look_arg_list.append(
                    (look_name_str, assign_path_str)
                )
        #
        lis.append(
            (export_file_path_str, look_arg_list)
        )
    return lis


def set_mtx_file_export_cmd(node_obj):
    set_cache_init()

    mtxObjects.GRH_OBJ_QUEUE.restore()
    export_list = get_mtx_file_export_list(node_obj)
    if isinstance(export_list, list):
        if export_list:
            for export_arg in export_list:
                export_file_path_str, look_arg_list = export_arg
                _file = usd2mtxObjects.File(export_file_path_str)
                if look_arg_list:
                    for look_name_str, assign_path_str in look_arg_list:
                        #
                        usdObjects.GRH_OBJ_QUEUE.restore()
                        usd2mtxObjects.GRH_TRS_OBJ_QUEUE.restore()
                        #
                        s = hou.node(assign_path_str).stage()
                        _s = usdCommands.loadScene(s)
                        root = usdObjects.Node(u'/')
                        _look = _file.addLook(look_name_str)
                        _look.addSrcGeometries(
                            root.allChildren(include=u'Mesh', asString=True)
                        )

                    _file.save()
                    hou.ui.displayMessage(
                        '''result: export materialx file "{}".'''.format(
                            export_file_path_str
                        )
                    )


def set_module_update():
    from LxScheme import shmOutput
    shmOutput.Scheme().loadActiveModules()
