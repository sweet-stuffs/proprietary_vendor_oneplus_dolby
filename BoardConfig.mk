#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from the proprietary version
include vendor/oneplus/dolby/BoardConfigVendor.mk

DOLBY_PATH := device/oneplus/dolby

# Properties
TARGET_ODM_PROP += $(DOLBY_PATH)/odm.prop
