# This library was generated through introspection of
#     /usr/include/pulse/introspect.h and
#     /usr/include/pulse/mainloop.h.
#     (E.g.:
#         python /usr/share/pyshared/ctypeslib/h2xml.py /usr/include/pulse/introspect.h -o pa.xml
#         python /usr/share/pyshared/ctypeslib/xml2py.py pa.xml -k f -l /usr/lib/libpulse.so -o pa.py
#     )
#
# License according to the header files listed above:
# GNU Lesser General Public License
#
# This file is part of GNOME Shell Volume Mixer
# Copyright (C) 2014 Alexander Hofbauer <alex@derhofbauer.at>


from ctypes import *

try:
    lib = CDLL('libpulse.so.0')
except:
    lib = CDLL('libpulse.so')

STRING = c_char_p
WSTRING = c_wchar_p

class mainloop(Structure):
    pass

class mainloop_api(Structure):
    pass

class spawn_api(Structure):
    pass

class context(Structure):
    pass

class operation(Structure):
    pass

class proplist(Structure):
    pass

class card_profile_info(Structure):
    _fields_ = [
        ('name', STRING),
        ('description', STRING),
        ('n_sinks', c_uint32),
        ('n_sources', c_uint32),
        ('priority', c_uint32),
    ]

class card_profile_info2(Structure):
    _fields_ = [
        ('name', STRING),
        ('description', STRING),
        ('n_sinks', c_uint32),
        ('n_sources', c_uint32),
        ('priority', c_uint32),
        ('available', c_int),
    ]

class card_port_info(Structure):
    _fields_ = [
        ('name', STRING),
        ('description', STRING),
        ('priority', c_uint32),
        ('available', c_int),
        ('direction', c_int),
        ('n_profiles', c_uint32),
        ('profiles', POINTER(POINTER(card_profile_info))),
        ('proplist', POINTER(proplist)),
        ('latency_offset', c_int64),
        ('profiles2', POINTER(POINTER(card_profile_info2))),
    ]

class card_info(Structure):
    _fields_ = [
        ('index', c_uint32),
        ('name', STRING),
        ('owner_module', c_uint32),
        ('driver', STRING),
        ('n_profiles', c_uint32),
        ('profiles', POINTER(card_profile_info)),
        ('active_profile', POINTER(card_profile_info)),
        ('proplist', POINTER(proplist)),
        ('n_ports', c_uint32),
        ('ports', POINTER(POINTER(card_port_info))),
        ('profiles2', POINTER(POINTER(card_profile_info2))),
        ('active_profile2', POINTER(card_profile_info2)),
    ]

class sink_port_info(Structure):
    _fields_ = [
        ('name', STRING),
        ('description', STRING),
        ('priority', c_uint32),
        ('available', c_int),
        ('availability_group', STRING),
        ('type', c_uint32),
    ]

class format_info(Structure):
    _fields_ = [
        ('encoding', c_int),
        ('plist', POINTER(proplist)),
    ]

class sample_spec(Structure):
    _fields_ = [
        ('format', c_int),
        ('rate', c_uint32),
        ('channels', c_uint8),
    ]

class pa_channel_map(Structure):
    _fields_ = [
        ('channels', c_uint8),
        ('map', c_int * int(32)),
    ]

class pa_cvolume(Structure):
    _fields_ = [
        ('channels', c_uint8),
        ('values', c_uint32 * int(32)),
    ]

class sink_info(Structure):
    _fields_ = [
        ('name', STRING),
        ('index', c_uint32),
        ('description', STRING),
        ('sample_spec', sample_spec),
        ('channel_map', pa_channel_map),
        ('owner_module', c_uint32),
        ('volume', pa_cvolume),
        ('mute', c_int),
        ('monitor_source', c_uint32),
        ('monitor_source_name', STRING),
        ('latency', c_uint64),
        ('driver', STRING),
        ('flags', c_int),
        ('proplist', POINTER(proplist)),
        ('configured_latency', c_uint64),
        ('base_volume', c_uint32),
        ('state', c_int),
        ('n_volume_steps', c_uint32),
        ('card', c_uint32),
        ('n_ports', c_uint32),
        ('ports', POINTER(POINTER(sink_port_info))),
        ('active_port', POINTER(sink_port_info)),
        ('n_formats', c_uint8),
        ('formats', POINTER(POINTER(format_info))),
    ]

mainloop_new = lib.pa_mainloop_new
mainloop_new.restype = POINTER(mainloop)
mainloop_new.argtypes = []
mainloop_get_api = lib.pa_mainloop_get_api
mainloop_get_api.restype = POINTER(mainloop_api)
mainloop_get_api.argtypes = [POINTER(mainloop)]
mainloop_iterate = lib.pa_mainloop_iterate
mainloop_iterate.restype = c_int
mainloop_iterate.argtypes = [POINTER(mainloop), c_int, POINTER(c_int)]
mainloop_free = lib.pa_mainloop_free
mainloop_free.restype = None
mainloop_free.argtypes = [POINTER(mainloop)]

context_flags = c_int  # enum
context_flags_t = context_flags

context_state = c_int  # enum
context_state_t = context_state
# values for enumeration 'context_state'
CONTEXT_UNCONNECTED = 0
CONTEXT_CONNECTING = 1
CONTEXT_AUTHORIZING = 2
CONTEXT_SETTING_NAME = 3
CONTEXT_READY = 4
CONTEXT_FAILED = 5
CONTEXT_TERMINATED = 6

context_new = lib.pa_context_new
context_new.restype = POINTER(context)
context_new.argtypes = [POINTER(mainloop_api), STRING]
context_notify_cb_t = CFUNCTYPE(None, POINTER(context), c_void_p)
context_set_state_callback = lib.pa_context_set_state_callback
context_set_state_callback.restype = None
context_set_state_callback.argtypes = [POINTER(context), context_notify_cb_t, c_void_p]
context_connect = lib.pa_context_connect
context_connect.restype = c_int
context_connect.argtypes = [POINTER(context), STRING, context_flags_t, POINTER(spawn_api)]
context_disconnect = lib.pa_context_disconnect
context_disconnect.restype = None
context_disconnect.argtypes = [POINTER(context)]
context_unref = lib.pa_context_unref
context_unref.restype = None
context_unref.argtypes = [POINTER(context)]
context_get_state = lib.pa_context_get_state
context_get_state.restype = context_state_t
context_get_state.argtypes = [POINTER(context)]

operation_unref = lib.pa_operation_unref
operation_unref.restype = None
operation_unref.argtypes = [POINTER(operation)]

card_info_cb_t = CFUNCTYPE(None, POINTER(context), POINTER(card_info), c_int, c_void_p)
context_get_card_info_by_index = lib.pa_context_get_card_info_by_index
context_get_card_info_by_index.restype = POINTER(operation)
context_get_card_info_by_index.argtypes = [POINTER(context), c_uint32, card_info_cb_t, c_void_p]
context_get_card_info_by_name = lib.pa_context_get_card_info_by_name
context_get_card_info_by_name.restype = POINTER(operation)
context_get_card_info_by_name.argtypes = [POINTER(context), STRING, card_info_cb_t, c_void_p]
context_get_card_info_list = lib.pa_context_get_card_info_list
context_get_card_info_list.restype = POINTER(operation)
context_get_card_info_list.argtypes = [POINTER(context), card_info_cb_t, c_void_p]

sink_info_cb_t = CFUNCTYPE(None, POINTER(context), POINTER(sink_info), c_int, c_void_p)
context_get_sink_info_by_index = lib.pa_context_get_sink_info_by_index
context_get_sink_info_by_index.restype = POINTER(operation)
context_get_sink_info_by_index.argtypes = [POINTER(context), c_uint32, sink_info_cb_t, c_void_p]
context_get_sink_info_by_name = lib.pa_context_get_sink_info_by_name
context_get_sink_info_by_name.restype = POINTER(operation)
context_get_sink_info_by_name.argtypes = [POINTER(context), STRING, sink_info_cb_t, c_void_p]
context_get_sink_info_list = lib.pa_context_get_sink_info_list
context_get_sink_info_list.restype = POINTER(operation)
context_get_sink_info_list.argtypes = [POINTER(context), sink_info_cb_t, c_void_p]

proplist_gets = lib.pa_proplist_gets
proplist_gets.restype = STRING
proplist_gets.argtypes = [POINTER(proplist), STRING]

proplist_to_string = lib.pa_proplist_to_string
proplist_to_string.restype = STRING
proplist_to_string.argtypes = [POINTER(proplist)]
