#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from the proprietary version
$(call inherit-product, vendor/oneplus/dolby/dolby-vendor.mk)

DOLBY_PATH := vendor/oneplus/dolby

# Configs
PRODUCT_COPY_FILES += \
    $(DOLBY_PATH)/configs/media/media_codecs_c2_dolby_audio.xml:$(TARGET_COPY_OUT_VENDOR)/etc/media_codecs_c2_dolby_audio.xml \
    $(DOLBY_PATH)/configs/dolby/multimedia_dolby_dax_default.xml:$(TARGET_COPY_OUT_ODM)/etc/dolby/multimedia_dolby_dax_default.xml

# Sepolicy
BOARD_VENDOR_SEPOLICY_DIRS += \
    $(DOLBY_PATH)/sepolicy/vendor

# Properties
TARGET_ODM_PROP += $(DOLBY_PATH)/odm.prop

# VINTF
DEVICE_FRAMEWORK_COMPATIBILITY_MATRIX_FILE += $(DOLBY_PATH)/configs/hidl/dolby_framework_matrix.xml
