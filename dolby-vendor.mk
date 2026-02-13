#
# Automatically generated file. DO NOT MODIFY
#

PRODUCT_SOONG_NAMESPACES += \
    vendor/oneplus/dolby

PRODUCT_COPY_FILES += \
    vendor/oneplus/dolby/proprietary/odm/etc/init/vendor.dolby.media.c2@1.0-service.rc:$(TARGET_COPY_OUT_ODM)/etc/init/vendor.dolby.media.c2@1.0-service.rc \
    vendor/oneplus/dolby/proprietary/odm/etc/init/vendor.dolby_sp.hardware.dmssp@2.0-service.rc:$(TARGET_COPY_OUT_ODM)/etc/init/vendor.dolby_sp.hardware.dmssp@2.0-service.rc

PRODUCT_PACKAGES += \
    libdapparamstorage_sp \
    libdeccfg_sp \
    libdlbdsservice_sp \
    libdlbpreg_sp \
    libspatializerparamstorage \
    libdlbvol_sp \
    libswdap_sp \
    libswgamedap_sp \
    libswspatializer \
    vendor.dolby_sp.hardware.dmssp@2.0-impl \
    vendor.dolby_sp.hardware.dmssp@2.0 \
    libcodec2_soft_ac4dec_sp \
    libcodec2_soft_ddpdec_sp \
    libcodec2_store_dolby_sp \
    vendor.dolby.hardware.dms.xml \
    vendor.dolby.media.c2@1.0-service.xml \
    vendor.dolby_sp.hardware.dmssp@2.0-service \
    vendor.dolby_sp.media.c2@1.0-service
