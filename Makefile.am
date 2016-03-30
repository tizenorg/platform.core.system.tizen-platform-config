ACLOCAL_AMFLAGS = ${ACLOCAL_FLAGS}

SUBDIRS = src

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = libtzplatform-config.pc
 
dist_noinst_SCRIPTS = autogen.sh

gumd_useradddir = $(sysconfdir)/gumd/useradd.d
gumd_useradd_DATA = gumd/useradd.d/90_user-content-permissions.post
