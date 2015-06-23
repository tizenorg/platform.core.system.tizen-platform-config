%define libname libtzplatform-config
%define keepstatic 1

Name:           tizen-platform-config
Version:        2.0
Release:        0
Summary:        Tizen Platform Configuration
License:        MIT
Url:            http://www.tizen.org
Group:          System/Configuration
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Source1001:     %{name}.manifest
BuildRequires:  tizen-platform-wrapper >= 2
Requires(post): smack
Requires(post): coreutils

# the main package only contains a config file but other dependent packages
# will contain binary. So, we can't build a noarch package and have to avoid
# a rpmlint warning using a filter in xxx-rpmlintrc

%description
Tizen Platform Configuration - variables definitions

%package -n %{libname}
Summary:        Tizen Platform Configuration - helper library
Group:          System/Libraries
License:        LGPL-2.0
Requires:       %{name} = %{version}
%description -n %{libname}
Tizen Platform Configuration - helper library to lookup Tizen variables easily

%package -n %{libname}-devel
Summary:        Tizen Platform Configuration - helper libray headers, RPM macros
Group:          Development/Libraries
License:        LGPL-2.0
Requires:       %{libname} = %{version}
%description -n %{libname}-devel
Tizen Platform Configuration - helper library headers to include in source code,
RPM macros to call in spec files

%package -n %{name}-tools
Summary:        Tizen Platform Configuration - tools
Group:          System/Utilities
License:        LGPL-2.0
Requires:       %{libname} = %{version}
%description -n %{name}-tools
Tizen Platform Configuration - helper program to lookup Tizen variables easily

%prep
%setup -q
cp %{SOURCE1001} .

%build
%reconfigure --enable-static
%__make %{?_smp_mflags}

%check
%__make check

%install
%make_install

%post
##############################################
# BEGIN - setting of predefined directories (also /etc/skel)
##############################################
saveHOME="$HOME"
HOME="%{_sysconfdir}/skel"
. "%{_sysconfdir}/tizen-platform.conf"
cat << ENDOFCAT |
MODE 777
SMACK System::Shared true
$TZ_SYS_STORAGE
$TZ_SYS_MEDIA

MODE 700
SMACK User::Home true
$TZ_USER_HOME
$TZ_USER_APPROOT
$TZ_USER_CONTENT

SMACK User::App::Shared true
$TZ_USER_CAMERA
$TZ_USER_DOCUMENTS
$TZ_USER_DOWNLOADS
$TZ_USER_GAMES
$TZ_USER_IMAGES
$TZ_USER_OTHERS
$TZ_USER_SOUNDS
$TZ_USER_VIDEOS
$TZ_USER_SHARE
$TZ_USER_HOME/.pki/nssdb
$TZ_USER_APP/xwalk-service

SMACK System::Shared true
$TZ_USER_DB
$TZ_USER_DESKTOP
$TZ_USER_APP
$TZ_USER_ICONS

SMACK User false
$TZ_USER_PACKAGES
ENDOFCAT
while read s1 s2 s3; do
  case "$s1" in
    MODE) m="$s2";;
    SMACK) c="$s2"; t="$s3";;
    "") ;;
    *) echo "$s1 ${m:-700} ${c:-_} ${t:-false}";;
  esac
done |
LANG=C sort |
while read dirname mode context transmute; do
        mkdir -p -m "$mode" "$dirname"
        if [ "$transmute" = true ]; then
                chsmack -a "$context" "$dirname"
        else
                chsmack -t -a "$context" "$dirname"
        fi >&2
done
HOME="$saveHOME"
##############################################
# END - setting of predefined directories (also /etc/skel)
##############################################

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%license MIT
%config %{_sysconfdir}/tizen-platform.conf

%files -n %{libname}
%manifest %{name}.manifest
%{_libdir}/*.so.*

%files -n %{libname}-devel
%manifest %{name}.manifest
%license LGPL_2.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h
%config %{_sysconfdir}/rpm/macros.tizen-platform
%{_libdir}/*.a

%files -n %{name}-tools
%manifest %{name}.manifest
%{_bindir}/*
