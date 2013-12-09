lib_LTLIBRARIES = libtzplatform-config-@LIBTZPLATFORM_CONFIG_VERSION@.la

bin_PROGRAMS = tzplatform-get

SRC_FROMWRAPPER= \
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
	tzplatform_config.c \
	tzplatform_config.h 

SRC_FROMTOOL= \
	tzplatform_variables.h \
	hash.inc

BUILT_SOURCES=$(SRC_FROMWRAPPER) $(SRC_FROMTOOL)

CLEANFILES=$(SRC_FROMWRAPPER) $(SRC_FROMTOOL)

nodist_libtzplatform_config_@LIBTZPLATFORM_CONFIG_VERSION@_la_SOURCES = \
	$(SRC_FROMWRAPPER) \
	$(SRC_FROMTOOL)

tizen-platform.conf: ../tizen-platform.meta
	tzplatform-tool pretty $< >$@

$(SRC_FROMWRAPPER) tzplatform_get.c:
	cp $(datadir)/tizen-platform-wrapper/$@ .

tzplatform_variables.h: tizen-platform.conf
	tzplatform-tool h $< >$@

hash.inc: tizen-platform.conf
	tzplatform-tool c $< >$@

libtzplatform_config_@LIBTZPLATFORM_CONFIG_VERSION@_la_LDFLAGS = -version-info $(LIBTZPLATFORM_CONFIG_SO_VERSION)
libtzplatform_config_@LIBTZPLATFORM_CONFIG_VERSION@_la_LDFLAGS += -export-symbols-regex tzplatform_.*
libtzplatform_config_@LIBTZPLATFORM_CONFIG_VERSION@_la_LDFLAGS += -Wl,-O3
libtzplatform_config_@LIBTZPLATFORM_CONFIG_VERSION@_la_LDFLAGS += -lpthread 

libtzplatform_config_includedir = $(includedir)/
nobase_libtzplatform_config_include_HEADERS = tzplatform_variables.h tzplatform_config.h

dist_sysconf_DATA=tizen-platform.conf

macros.tizen-platform: tizen-platform.conf
	tzplatform-tool rpm $< | grep -v TZ_USER_ >$@

tzplatform_config_sysconfdir= $(sysconfdir)/rpm
dist_tzplatform_config_sysconf_DATA=macros.tizen-platform

tzplatform_get_SOURCES = tzplatform_get.c
tzplatform_get_LDADD = libtzplatform-config-@LIBTZPLATFORM_CONFIG_VERSION@.la


