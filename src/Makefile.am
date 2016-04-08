lib_LTLIBRARIES = libtzplatform-config-@LIBTZPLATFORM_CONFIG_VERSION@.la

lib_LIBRARIES = libtzplatform-config-static.a

bin_PROGRAMS = tzplatform-get

wrappersrcdir=$(shell pkg-config --variable=datadir tizen-platform-wrapper)

SRC_FROMWRAPPER_STATIC= \
	static-api.c \
	isadmin.h \
	isadmin.c

SRC_FROMWRAPPER_SHARED= \
	buffer.h \
	buffer.c \
	foreign.h \
	foreign.c \
	heap.h \
	heap.c \
	parser.h \
	parser.c \
	passwd.h \
	passwd.c \
	scratch.h \
	scratch.c \
	context.c \
	context.h \
	hashing.c \
	hashing.h \
	init.c \
	init.h \
	shared-api.c \
	shared-api.h \
	tzplatform_config.sym \
	tzplatform_config.h

SRC_FROMWRAPPER=$(SRC_FROMWRAPPER_SHARED) $(SRC_FROMWRAPPER_STATIC)

SRC_FROMTOOL= \
	tzplatform_variables.h \
	signup.inc \
	hash.inc

CFLAGS += -fPIC

BUILT_SOURCES=$(SRC_FROMWRAPPER) $(SRC_FROMTOOL)

CLEANFILES=$(SRC_FROMWRAPPER) $(SRC_FROMTOOL)

libtzplatform_config_static_a_SOURCES = $(SRC_FROMWRAPPER_STATIC)

libtzplatform_config_@LIBTZPLATFORM_CONFIG_VERSION@_la_SOURCES = \
	$(SRC_FROMWRAPPER_SHARED) \
	$(SRC_FROMTOOL)

tizen-platform.conf: ../tizen-platform.meta
	tzplatform-tool pretty $< >$@

$(SRC_FROMWRAPPER) tzplatform_get.c:
	cp $(wrappersrcdir)/tizen-platform-wrapper/$@ .

tzplatform_variables.h: tizen-platform.conf
	tzplatform-tool h $< >$@

hash.inc: tizen-platform.conf
	tzplatform-tool c $< >$@

signup.inc: tizen-platform.conf
	tzplatform-tool signup $< >$@

libtzplatform_config_@LIBTZPLATFORM_CONFIG_VERSION@_la_LDFLAGS = -version-info $(LIBTZPLATFORM_CONFIG_SO_VERSION)
libtzplatform_config_@LIBTZPLATFORM_CONFIG_VERSION@_la_LDFLAGS += -Wl,--version-script=tzplatform_config.sym
libtzplatform_config_@LIBTZPLATFORM_CONFIG_VERSION@_la_LDFLAGS += -Wl,-O3
libtzplatform_config_@LIBTZPLATFORM_CONFIG_VERSION@_la_LDFLAGS += -lpthread

libtzplatform_config_includedir = $(includedir)/
nobase_libtzplatform_config_include_HEADERS = tzplatform_variables.h tzplatform_config.h

dist_sysconf_DATA=tizen-platform.conf

macros.tizen-platform: tizen-platform.conf
	tzplatform-tool rpm $< | grep -v TZ_USER_ > $@

tzplatform_config_sysconfdir= $(sysconfdir)/rpm
dist_tzplatform_config_sysconf_DATA=macros.tizen-platform

tzplatform_get_SOURCES = tzplatform_get.c
tzplatform_get_LDADD = libtzplatform-config-static.a libtzplatform-config-@LIBTZPLATFORM_CONFIG_VERSION@.la



