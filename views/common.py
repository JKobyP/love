# -*- coding: utf-8 -*-
from logic.employee import employees_matching_prefix
from util.render import make_json_response


def autocomplete(request):
    """This is the implementation of the autocomplete API endpoint. It's shared between
    the api view and web view that is called from Javascript, only the authorization
    checks are different.
    """
    matches = employees_matching_prefix(request.args.get('term', None))
    users = [
        {
            'label': u'{} ({})'.format(full_name, username),
            'value': unicode(username)
        }
        for full_name, username
        in matches
    ]
    return make_json_response(users)
