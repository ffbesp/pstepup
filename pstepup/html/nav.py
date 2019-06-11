"""Utility functions for website navigation
"""

import appdata


def get_last_four_banners(banner_type):
    """Find last 4 banners in reverse chronological order

    Args:
        banner_type (str): types of banner to return (single, multi, or all)
    """
    banner_list = []
    for banner_id, banner_details in appdata.banner_info.items():
        combined_banner_info = banner_details
        combined_banner_info['banner_id'] = banner_id
        banner_list.append(combined_banner_info)

    banner_sort = sorted(
        banner_list, key=lambda k: k['duration']['start'].replace('-', ''), reverse=True)

    if banner_type == 'single':
        return [x for x in banner_sort if len(x['banner_icon']) == 1][:4]
    elif banner_type == 'multi':
        return [x for x in banner_sort if len(x['banner_icon']) > 1][:4]
    else: #all
        return banner_sort[:4]
