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
    'odm/bin/hw/vendor.dolby_sp.media.c2@1.0-service': blob_fixup()
        .replace_needed('libcodec2_hidl@1.0.so', 'libcodec2_hidl@1.0_sp.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk_sp.so'),
    'odm/lib64/libcodec2_store_dolby_sp.so': blob_fixup()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk_sp.so'),
    ('odm/lib64/libcodec2_soft_ac4dec_sp.so', 'odm/lib64/libcodec2_soft_ddpdec_sp.so'): blob_fixup()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk_sp.so')
        .replace_needed('libcodec2_soft_common.so', 'libcodec2_soft_common_sp.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    ('odm/lib64/libcodec2_soft_common_sp.so', 'odm/lib64/libcodec2_hidl_plugin_sp.so'): blob_fixup()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk_sp.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    'odm/lib64/libcodec2_vndk_sp.so': blob_fixup()
        .replace_needed('libui.so', 'libui_sp.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    'odm/lib64/libcodec2_hidl@1.0_sp.so': blob_fixup()
        .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin_sp.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk_sp.so'),
    'odm/lib64/libui_sp.so': blob_fixup()
        .replace_needed('android.hardware.graphics.common-V3-ndk.so', 'android.hardware.graphics.common-V7-ndk.so')
        .replace_needed('android.hardware.graphics.allocator-V1-ndk.so', 'android.hardware.graphics.allocator-V2-ndk.so'),
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
        'odm/lib64/soundfx/libswdap_sp.so',
        'odm/lib64/soundfx/libswspatializer.so',
        'odm/lib64/libcodec2_soft_ac4dec_sp.so',
        'odm/lib64/libcodec2_soft_ddpdec_sp.so'
    ): blob_fixup().replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
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
