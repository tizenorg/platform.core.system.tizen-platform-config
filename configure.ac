 
AC_INIT([libtzplatform-config], [1.0])
AC_PREREQ([2.59])
AM_INIT_AUTOMAKE([1.10 -Wall no-define])
 

AC_CONFIG_HEADERS([config.h ])
AC_PROG_CC
AM_PROG_AR
LT_INIT([disable-static])
 

AC_SUBST([LIBTZPLATFORM_CONFIG_SO_VERSION], [1:0:0])
AC_SUBST([LIBTZPLATFORM_CONFIG_VERSION], [1.0])
 

AC_CONFIG_FILES([
Makefile
src/Makefile
libtzplatform-config.pc:libtzplatform-config.pc.in])
AC_OUTPUT

