LOCAL_PATH := $(my-dir)
include $(CLEAR_VARS)

LOCAL_MODULE=$(UBOOT_TARGET_FILE)
LOCAL_MODULE_TAGS := eng
LOCAL_MODULE_PATH := $(OUT_IMAGE_DIR)
LOCAL_MODULE_GEN_BINRARY_FILES=$(UBOOT_TARGET_FILE)
LOCAL_MODULE_CONFIG_FILES:=include/config.h
LOCAL_MODULE_CONFIG= make $(UBOOT_BUILD_CONFIG)
LOCAL_MODULE_COMPILE=make -j$(MAKE_JLEVEL)
LOCAL_MODULE_COMPILE_CLEAN=make distclean
include $(BUILD_THIRDPART)

