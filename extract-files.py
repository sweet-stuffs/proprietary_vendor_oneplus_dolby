#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2025 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)

blob_fixups: blob_fixups_user_type = {
    'odm/etc/vintf/manifest/vendor.dolby.media.c2@1.0-service.xml': blob_fixup()
        .regex_replace('            <instance>dolby</instance>\n', '')
        .regex_replace('            <instance>oplussoftware</instance>\n', '')
        .regex_replace('        <fqname>@1.0::IComponentStore/software</fqname>\n', '')
        .regex_replace('        <fqname>@1.1::IComponentStore/software</fqname>\n', '')
        .regex_replace('        <fqname>@1.2::IComponentStore/software</fqname>\n', '')
        .regex_replace('        <fqname>@1.0::IComponentStore/default2</fqname>\n', ''),
}  # fmt: skip

module = ExtractUtilsModule(
    'dolby',
    'oneplus',
    blob_fixups=blob_fixups,
    device_rel_path='vendor/oneplus/dolby',
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
