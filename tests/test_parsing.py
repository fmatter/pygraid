from pygraid import (
    parse_annotation,
    is_ref,
    is_pred,
    noun_pattern,
    ref_pattern,
    parse_graid_item,
)

import logging

# handler = colorlog.StreamHandler(None)
# handler.setFormatter(
#     colorlog.ColoredFormatter("%(log_color)s%(levelname)-7s%(reset)s %(message)s")
# )
log = logging.getLogger(__name__)
# log.propagate = False
# log.addHandler(handler)
# log.setLevel(logging.DEBUG)


test_dic = {
    "np:l:pred": {
        "func": "pred",
        "type": "pred",
        "form": "free",
        "pred": "np:l",
        "anim": "nh",
        "syn": "l",
        "formglosses": "",
        "funcglosses": "",
    },
    "v:pred": {
        "func": "pred",
        "pred": "v",
        "type": "pred",
        "form": "free",
        "functags": "",
        "formtags": "",
    },
    "aux": {
        "func": "aux",
        "type": "other",
        "form": "free",
        "functags": "",
        "formtags": "",
    },
    "np:g": {
        "type": "ref",
        "ref": "np",
        "anim": "nh",
        "syn": "g",
        "form": "free",
        "funcglosses": "",
        "formglosses": "",
    },
    "pro.h:a": {
        "type": "ref",
        "ref": "pro",
        "anim": "h",
        "syn": "a",
        "form": "free",
        "funcglosses": "",
        "formglosses": "",
    },
    "pro.h:s": {
        "type": "ref",
        "ref": "pro",
        "anim": "h",
        "syn": "s",
        "form": "free",
        "funcglosses": "",
        "formglosses": "",
    },
    "pro:p": {
        "type": "ref",
        "ref": "pro",
        "anim": "nh",
        "syn": "p",
        "form": "free",
        "formglosses": "",
        "funcglosses": "",
    },
    "0.h:a": {
        "type": "ref",
        "ref": "0",
        "anim": "h",
        "syn": "a",
        "form": "free",
        "funcglosses": "",
        "formglosses": "",
    },
    "0.h:p": {
        "type": "ref",
        "ref": "0",
        "anim": "h",
        "syn": "p",
        "form": "free",
        "funcglosses": "",
        "formglosses": "",
    },
    "np.h:a": {
        "type": "ref",
        "ref": "np",
        "anim": "h",
        "syn": "a",
        "form": "free",
        "funcglosses": "",
        "formglosses": "",
    },
    "pro.1:p": {
        "type": "ref",
        "ref": "pro",
        "anim": "1",
        "syn": "p",
        "form": "free",
        "funcglosses": "",
        "formglosses": "",
    },
    "np:p2": {
        "type": "ref",
        "ref": "np",
        "anim": "nh",
        "syn": "p2",
        "form": "free",
        "funcglosses": "",
        "formglosses": "",
    },
    "pro.h:a-v:pred-pro:p": [
        {
            "type": "ref",
            "ref": "pro",
            "anim": "h",
            "syn": "a",
            "form": "bound",
            "funcglosses": "",
            "formglosses": "",
        },
        {
            "func": "pred",
            "pred": "v",
            "type": "pred",
            "form": "free",
            "functags": "",
            "formtags": "",
        },
        {
            "type": "ref",
            "ref": "pro",
            "anim": "nh",
            "syn": "p",
            "form": "bound",
            "funcglosses": "",
            "formglosses": "",
        },
    ],
    "v:pred": {
        "func": "pred",
        "pred": "v",
        "type": "pred",
        "form": "free",
        "functags": "",
        "formtags": "",
    },
    # "aux=pro:p": [
    #     {
    #         "func": "aux",
    #         "type": "other",
    #         "form": "clitic",
    #         "functags": "",
    #         "formtags": "",
    #     },
    #     {
    #         "type": "ref",
    #         "form": "clitic",
    #         "anim": "nh",
    #         "syn": "p",
    #         "ref": "pro",
    #         "funcglosses": "",
    #         "formglosses": "",
    #     },
    # ],
    "pro.1:ncs": {
        "type": "ref",
        "ref": "pro",
        "anim": "1",
        "syn": "ncs",
        "form": "free",
        "funcglosses": "",
        "formglosses": "",
    },
    "pro:ncs": {
        "type": "ref",
        "ref": "pro",
        "anim": "nh",
        "syn": "ncs",
        "form": "free",
        "funcglosses": "",
        "formglosses": "",
    },
    "pro.h:s": {
        "type": "ref",
        "ref": "pro",
        "anim": "h",
        "syn": "s",
        "form": "free",
        "funcglosses": "",
        "formglosses": "",
    },
    "np:other": {
        "type": "ref",
        "ref": "np",
        "anim": "nh",
        "syn": "other",
        "form": "free",
        "funcglosses": "",
        "formglosses": "",
    },
    "v:predex": {
        "func": "predex",
        "pred": "v",
        "type": "pred",
        "form": "free",
        "functags": "",
        "formtags": "",
    },
    "other": {
        "type": "other",
        "form": "free",
        "functags": "",
        "formtags": "",
    },
    "adp": {
        "type": "other",
        "func": "adp",
        "form": "free",
        "functags": "",
        "formtags": "",
    },
}


def test_parse():
    for ann, res in test_dic.items():
        if not isinstance(res, list):
            res = [res]
        assert parse_graid_item(ann) == res


def test_id():
    assert is_pred("v:pred")
    assert is_ref("pro.h:a")
    assert is_pred("np:pred")
    assert not is_ref("np:pred")
    assert is_pred("np:predex")
    assert not is_ref("v:pred")
    assert is_pred("np.h:l:pred")
    for x in ["aux", "cop", "adp"]:
        assert not is_ref(x)
        assert not is_pred(x)


# l_aux
# r_aux
# v:pred
# v:predex
# aux
# cop
# other:pred
# vother:pred
# np:pred
# other:predex
# vother:predex
# np:predex
# 0.h:sv:pred
# np.h:pred
# np.l:pred
# vother:ncs
# vother:other
# vother:obl
# np.h:predex
