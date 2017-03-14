LOCAL_PATH := $(my-dir)
include $(CLEAR_VARS)

LOCAL_MODULE := test-x2d
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_PATH:=$(TARGET_FS_BUILD)/$(TARGET_TESTSUIT_DIR)/$(LOCAL_MODULE)
LOCAL_SRC_FILES := dmmu.c x2d.c main.c x2d_api.c
LOCAL_CFLAGS := -DFAKE_LOG_DEVICE=1 -Werror -DHAVE_SYS_UIO_H -fpic
LOCAL_LDLIBS := -lc

include $(BUILD_EXECUTABLE)

