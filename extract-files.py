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
    (
        'odm/lib/libdlbdsservice_sp.so',
        'odm/lib/libdlbpreg_sp.so',
        'odm/lib/soundfx/libdlbvol_sp.so',
        'odm/lib/soundfx/libswdap_sp.so',
        'odm/lib/soundfx/libswspatializer.so',
        'odm/lib64/libdlbdsservice_sp.so',
        'odm/lib64/libdlbpreg_sp.so',
        'odm/lib64/soundfx/libdlbvol_sp.so',
        'odm/lib64/soundfx/libswspatializer.so',
        'odm/lib64/libcodec2_soft_ac4dec_sp.so',
        'odm/lib64/libcodec2_soft_ddpdec_sp.so'
    ): blob_fixup().replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    # < 00146c60: 1f00 0071 e003 0091 f317 9f1a 4162 0494  ...q........Ab..
    # < 00146d80: 0900 0012 8902 090b 3f01 086b ca01 0054  ........?..k...T
    # ---
    # > 00146c60: 1f00 0071 e003 0091 1300 8052 4162 0494  ...q.......RAb..
    # > 00146d80: 0900 0012 8902 090b 3f01 086b 0e00 0014  ........?..k....
  'odm/lib64/soundfx/libswdap_sp.so': blob_fixup()
    .binary_regex_replace(b'\x1f\x00\x00\x71\xe0\x03\x00\x91\xf3\x17\x9f\x1a\x41\x62\x04\x94',
                          b'\x1f\x00\x00\x71\xe0\x03\x00\x91\x13\x00\x80\x52\x41\x62\x04\x94')
    .binary_regex_replace(rb'\x09\x00\x00\x12\x89\x02\x09\x0b\x3f\x01\x08\x6b\xca\x01\x00\x54',
                          b'\x09\x00\x00\x12\x89\x02\x09\x0b\x3f\x01\x08\x6b\x0e\x00\x00\x14')
    .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
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
